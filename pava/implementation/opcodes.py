from collections import namedtuple
import jawa
import peak.util.assembler as asm
import sys

VERBOSE = True
DEBUG = False


def convert_ldc(code, java_pos, java_locals, value):
    code.LOAD_CONST(value)
    code.word_size = 1


def convert_ldc_w(code, java_pos, java_locals, value):
    code.LOAD_CONST(value)
    code.word_size = 1


def convert_ldc2_w(code, java_pos, java_locals, value):
    code.LOAD_CONST(value)
    code.word_size = 2


def convert_instanceof(code, java_pos, java_locals, class_):
    code.LOAD_GLOBAL('isinstance')
    code.ROT_TWO()
    class_reference(code, class_)
    code.CALL_FUNCTION(2)
    code.word_size = 1


def convert_arraylength(code, java_pos, java_locals):
    code.LOAD_GLOBAL('len')
    code.ROT_TWO()
    code.CALL_FUNCTION(1)
    code.word_size = 1


def convert_getstatic(code, java_pos, java_locals, class_, descriptor, field):
    class_reference(code, class_)
    code.LOAD_ATTR(field)
    code.word_size = get_word_size(descriptor)


def convert_putstatic(code, java_pos, java_locals, class_, descriptor, field):
    class_reference(code, class_)
    code.STORE_ATTR(field)
    code.word_size = 0


def get_word_size(descriptor):
    if descriptor[0] == '(':
        descriptor = descriptor[descriptor.index(')') + 1:]
    if descriptor == 'D' or descriptor == 'J':
        return 2
    return 1

def class_reference(code, class_, load=True):
    fragments = str(class_).split('/')
    asm.Global(fragments[0], code)
    for fragment in fragments[1:]:
        if load:
            code.LOAD_ATTR(fragment)
        else:
            code.STORE_ATTR(fragment)

    module_name = fragments[0]
    load_module(code, module_name)
    for fragment in fragments[1:-1]:
        module_name += '.' + fragment
        load_module(code, module_name)


def load_module(code, name):
    # print 'load module', name
    code.module_names.add(name)
    # __import__(name)


def convert_new(code, java_pos, java_locals, class_):
    class_reference(code, class_)
    code.word_size = 1


def convert_anewarray(code, java_pos, java_locals, class_):
    code([])
    code.word_size = 1


def convert_checkcast(code, java_pos, java_locals, class_):
    if class_:
        # TODO: implement checkcast for a type
        code.DUP_TOP()
        code.POP_TOP()
    else:
        # TODO: implement checkcast for null
        code.DUP_TOP()
        code.POP_TOP()
    code.word_size = 0


def convert_invokevirtual(code, java_pos, java_locals, clazz_, name, descriptor, argument_count):
    invoke(code, java_pos, java_locals, name, descriptor, argument_count)


def convert_invokeinterface(code, java_pos, java_locals, clazz_, name, descriptor, argument_count, X):
    invoke(code, java_pos, java_locals, name, descriptor, argument_count)


def convert_invokespecial(code, java_pos, java_locals, clazz_, name, descriptor, argument_count):
    invoke(code, java_pos, java_locals, name, descriptor, argument_count, special=True)


def invoke(code, java_pos, java_locals, name, descriptor, argument_count, special=False):
    # put the function itself on the stack at the right spot
    def load_function():
        code.LOAD_ATTR(name)

    if argument_count:
        inject(code, argument_count, load_function)
    else:
        load_function()

    if special:
        code.LOAD_GLOBAL('super')
        code.ROT_TWO()
        code.CALL_FUNCTION(1)

    code.CALL_FUNCTION(argument_count)

    if descriptor.endswith('V'):
        # Python methods always return something, so remove that value
        code.POP_TOP()

    code.word_size = get_word_size(descriptor)


def inject(code, block_count, fn):
    '''Go back in the current code by <block_count> blocks. Run fn there. '''
    if DEBUG:
        print 'inject %d blocks' % block_count
    target = code.get_stack_size() - 1
    index = get_insertion_index(code, block_count, target)
    if DEBUG:
        print 'inject at %d' % index
    co_code = code.co_code
    code_len = len(co_code)
    fn()
    code.co_code = co_code[:index] + co_code[code_len:] + co_code[index:code_len]
    update_code(code, index, len(co_code) - code_len)


def get_insertion_index(code, block_count, target):
    if DEBUG:
        print 'target = %d' % target
        for n in range(0, len(code.stack_depth)):
            print n, code.stack_depth[n]
    for n in range(len(code.stack_depth) - 1, -1, -1):
        if DEBUG:
            print 'Try', n, code.stack_depth[n]
        index, depth = code.stack_depth[n]
        if depth == target:
            block_count -= 1
            if block_count < 1:
                return index
    return 0


def update_code(code, insert_index, inserted_count):
    for n in range(0, len(code.stack_depth)):
        index, depth = code.stack_depth[n]
        if index >= insert_index:
            code.stack_depth[n] = index + inserted_count, depth
    for n in range(0, len(code.java_bytecodes)):
        index, info = code.java_bytecodes[n]
        if index >= insert_index:
            code.java_bytecodes[n] = index + inserted_count, info


def convert_invokestatic(code, java_pos, java_locals, clazz_, name, descriptor, argument_count):
    # put the function itself on the stack at the right spot
    def load_function():
        class_reference(code, clazz_)
        code.LOAD_ATTR(name)
    inject(code, argument_count, load_function)
    code.CALL_FUNCTION(argument_count)
    code.word_size = get_word_size(descriptor)


def convert_pop(code, java_pos, java_locals):
    code.POP_TOP()
    code.word_size = 0


def convert_pop2(code, java_pos, java_locals):
    code.POP_TOP()
    if code.word_size == 1:
        code.POP_TOP()
    code.word_size = 0


def convert_areturn(code, java_pos, java_locals):
    code.RETURN_VALUE()
    code.set_stack_size(0)
    code.word_size = 0


def convert_dup(code, java_pos, java_locals):
    code.DUP_TOP()


def convert_dup_x1(code, java_pos, java_locals):
    # before: word1, word2, ...
    code.DUP_TOP()
    code.ROT_THREE()
    # after: word1, word2, word1, ...


def convert_dup_x2(code, java_pos, java_locals):
    # before: word1, word2, ...
    code.DUP_TOP()
    code.ROT_THREE()
    # after: word1, word2, word1, ...


def convert_dup2(code, java_pos, java_locals):
    if code.word_size == 2:
        # before: word1, ...
        code.DUP_TOP()
        # after: word1, word1, ...
    else:
        # before: word1, word2, ...
        code.ROT_TWO()
        code.DUP_TOP()
        code.ROT_THREE()
        # now: word2, word1, word2, ...
        code.ROT_TWO()
        code.DUP_TOP()
        code.ROT_THREE()
        # after: word1, word2, word1, word2, ...


def convert_dup2_x1(code, java_pos, java_locals):
    if code.word_size == 2:
        # before: word1, word2, ...
        code.DUP_TOP()
        code.ROT_THREE()
        # after: word1, word2, word1, ...
    else:
        # before: word1, word2, word3, ...
        code.ROT_TWO()
        code.DUP_TOP()
        code.ROT_FOUR()
        # now: word2, word1, word3, word2, ...
        code.ROT_TWO()
        code.DUP_TOP()
        code.ROT_FOUR()
        # after: word1, word2, word3, word1, word2, ...

def convert_ireturn(code, java_pos, java_locals):
    code.RETURN_VALUE()
    code.set_stack_size(0)
    code.word_size = 0


def convert_dreturn(code, java_pos, java_locals):
    code.RETURN_VALUE()
    code.set_stack_size(0)
    code.word_size = 0


def convert_freturn(code, java_pos, java_locals):
    code.RETURN_VALUE()
    code.set_stack_size(0)
    code.word_size = 0


def convert_lreturn(code, java_pos, java_locals):
    code.RETURN_VALUE()
    code.set_stack_size(0)
    code.word_size = 0


def convert_return(code, java_pos, java_locals):
    # an empty return in Java means return None in Python
    code.LOAD_CONST(0)
    code.RETURN_VALUE()
    code.set_stack_size(0)
    code.word_size = 0


def convert_aastore(code, java_pos, java_locals):
    # Java uses [array, index, value, AASTORE}
    # Python uses [value, index, array, STORE_SUBSCR}
    code.ROT_THREE()
    code.STORE_SUBSCR()
    code.word_size = 0


def convert_aaload(code, java_pos, java_locals):
    # Java uses [array, index, AALOAD}
    # Python uses [array, index, BINARY_SUBSCR}
    code.BINARY_SUBSCR()
    code.word_size = 1


def convert_iastore(code, java_pos, java_locals):
    # Java uses [array, index, value, IASTORE}
    # Python uses [value, index, array, STORE_SUBSCR}
    code.ROT_THREE()
    code.STORE_SUBSCR()
    code.word_size = 0


def convert_fastore(code, java_pos, java_locals):
    # Java uses [array, index, value, FASTORE}
    # Python uses [value, index, array, STORE_SUBSCR}
    code.ROT_THREE()
    code.STORE_SUBSCR()
    code.word_size = 0


def convert_dastore(code, java_pos, java_locals):
    # Java uses [array, index, value, DASTORE}
    # Python uses [value, index, array, STORE_SUBSCR}
    code.ROT_THREE()
    code.STORE_SUBSCR()
    code.word_size = 0


def convert_lastore(code, java_pos, java_locals):
    # Java uses [array, index, value, LASTORE}
    # Python uses [value, index, array, STORE_SUBSCR}
    code.ROT_THREE()
    code.STORE_SUBSCR()
    code.word_size = 0


def convert_sastore(code, java_pos, java_locals):
    # Java uses [array, index, value, SASTORE}
    # Python uses [value, index, array, STORE_SUBSCR}
    code.ROT_THREE()
    code.STORE_SUBSCR()
    code.word_size = 0


def convert_bastore(code, java_pos, java_locals):
    # Java uses [array, index, value, BASTORE}
    # Python uses [value, index, array, STORE_SUBSCR}
    code.ROT_THREE()
    code.STORE_SUBSCR()
    code.word_size = 0


def convert_iaload(code, java_pos, java_locals):
    # Java uses [array, index, IALOAD}
    # Python uses [array, index, BINARY_SUBSCR}
    code.BINARY_SUBSCR()
    code.word_size = 1


def convert_saload(code, java_pos, java_locals):
    # Java uses [array, index, SALOAD}
    # Python uses [array, index, BINARY_SUBSCR}
    code.BINARY_SUBSCR()
    code.word_size = 1


def convert_baload(code, java_pos, java_locals):
    # Java uses [array, index, AALOAD}
    # Python uses [array, index, BINARY_SUBSCR}
    code.BINARY_SUBSCR()
    code.word_size = 1


def convert_laload(code, java_pos, java_locals):
    # Java uses [array, index, AALOAD}
    # Python uses [array, index, BINARY_SUBSCR}
    code.BINARY_SUBSCR()
    code.word_size = 2


def convert_daload(code, java_pos, java_locals):
    # Java uses [array, index, DALOAD}
    # Python uses [array, index, BINARY_SUBSCR}
    code.BINARY_SUBSCR()
    code.word_size = 2


def convert_faload(code, java_pos, java_locals):
    # Java uses [array, index, FALOAD}
    # Python uses [array, index, BINARY_SUBSCR}
    code.BINARY_SUBSCR()
    code.word_size = 1


def convert_castore(code, java_pos, java_locals):
    # Java uses [array, index, value, AASTORE}
    # Python uses [value, index, array, STORE_SUBSCR}
    code.ROT_THREE()
    code.STORE_SUBSCR()
    code.word_size = 1


def convert_caload(code, java_pos, java_locals):
    # Java uses [array, index, AALOAD}
    # Python uses [array, index, BINARY_SUBSCR}
    code.BINARY_SUBSCR()
    code.word_size = 1


def convert_athrow(code, java_pos, java_locals):
    code.RAISE_VARARGS(1)
    code.word_size = 0


##########


def convert_iinc(code, java_pos, java_locals, index, value):
    asm.Local(java_locals[index], code)
    code(asm.Const(value))
    code.BINARY_ADD()
    asm.LocalAssign(java_locals[index], code)
    code.word_size = 1


##########


def convert_aload(code, java_pos, java_locals, index):
    asm.Local(java_locals[index], code)
    code.word_size = 1


def convert_astore(code, java_pos, java_locals, index):
    asm.LocalAssign(java_locals[index], code)
    code.word_size = 1


##########


def convert_iload(code, java_pos, java_locals, index):
    asm.Local(java_locals[index], code)
    code.word_size = 1


def convert_istore(code, java_pos, java_locals, index):
    asm.LocalAssign(java_locals[index], code)
    code.word_size = 0


##########


def convert_fload(code, java_pos, java_locals, index):
    asm.Local(java_locals[index], code)
    code.word_size = 1


def convert_fstore(code, java_pos, java_locals, index):
    asm.LocalAssign(java_locals[index], code)
    code.word_size = 0


##########


def convert_dload(code, java_pos, java_locals, index):
    asm.Local(java_locals[index], code)
    code.word_size = 1


def convert_dstore(code, java_pos, java_locals, index):
    asm.LocalAssign(java_locals[index], code)
    code.word_size = 0


##########


def convert_lload(code, java_pos, java_locals, index):
    asm.Local(java_locals[index], code)
    code.word_size = 1


def convert_lstore(code, java_pos, java_locals, index):
    asm.LocalAssign(java_locals[index], code)
    code.word_size = 0


##########


def convert_aload_0(code, java_pos, java_locals):
    asm.Local(java_locals[0], code)
    code.word_size = 1


def convert_astore_0(code, java_pos, java_locals):
    asm.LocalAssign(java_locals[0], code)
    code.word_size = 0


def convert_aload_1(code, java_pos, java_locals):
    asm.Local(java_locals[1], code)
    code.word_size = 1


def convert_astore_1(code, java_pos, java_locals):
    asm.LocalAssign(java_locals[1], code)
    code.word_size = 0


def convert_aload_2(code, java_pos, java_locals):
    asm.Local(java_locals[2], code)
    code.word_size = 1


def convert_astore_2(code, java_pos, java_locals):
    asm.LocalAssign(java_locals[2], code)
    code.word_size = 0


def convert_aload_3(code, java_pos, java_locals):
    asm.Local(java_locals[3], code)
    code.word_size = 1


def convert_astore_3(code, java_pos, java_locals):
    asm.LocalAssign(java_locals[3], code)
    code.word_size = 0


##########


def convert_iload_0(code, java_pos, java_locals):
    asm.Local(java_locals[0], code)
    code.word_size = 1


def convert_istore_0(code, java_pos, java_locals):
    asm.LocalAssign(java_locals[0], code)
    code.word_size = 0


def convert_iload_1(code, java_pos, java_locals):
    asm.Local(java_locals[1], code)
    code.word_size = 1


def convert_istore_1(code, java_pos, java_locals):
    asm.LocalAssign(java_locals[1], code)
    code.word_size = 0


def convert_iload_2(code, java_pos, java_locals):
    asm.Local(java_locals[2], code)
    code.word_size = 1


def convert_istore_2(code, java_pos, java_locals):
    asm.LocalAssign(java_locals[2], code)
    code.word_size = 0


def convert_iload_3(code, java_pos, java_locals):
    asm.Local(java_locals[3], code)
    code.word_size = 1


def convert_istore_3(code, java_pos, java_locals):
    asm.LocalAssign(java_locals[3], code)
    code.word_size = 0


##########


def convert_lload_0(code, java_pos, java_locals):
    asm.Local(java_locals[0], code)
    code.word_size = 2


def convert_lstore_0(code, java_pos, java_locals):
    asm.LocalAssign(java_locals[0], code)
    code.word_size = 0


def convert_lload_1(code, java_pos, java_locals):
    asm.Local(java_locals[1], code)
    code.word_size = 2


def convert_lstore_1(code, java_pos, java_locals):
    asm.LocalAssign(java_locals[1], code)
    code.word_size = 0


def convert_lload_2(code, java_pos, java_locals):
    asm.Local(java_locals[2], code)
    code.word_size = 2


def convert_lstore_2(code, java_pos, java_locals):
    asm.LocalAssign(java_locals[2], code)
    code.word_size = 0


def convert_lload_3(code, java_pos, java_locals):
    asm.Local(java_locals[3], code)
    code.word_size = 2


def convert_lstore_3(code, java_pos, java_locals):
    asm.LocalAssign(java_locals[3], code)
    code.word_size = 0


##########


def convert_dload_0(code, java_pos, java_locals):
    asm.Local(java_locals[0], code)
    code.word_size = 2


def convert_dstore_0(code, java_pos, java_locals):
    asm.LocalAssign(java_locals[0], code)
    code.word_size = 0


def convert_dload_1(code, java_pos, java_locals):
    asm.Local(java_locals[1], code)
    code.word_size = 2


def convert_dstore_1(code, java_pos, java_locals):
    asm.LocalAssign(java_locals[1], code)
    code.word_size = 0


def convert_dload_2(code, java_pos, java_locals):
    asm.Local(java_locals[2], code)
    code.word_size = 2


def convert_dstore_2(code, java_pos, java_locals):
    asm.LocalAssign(java_locals[2], code)
    code.word_size = 0


def convert_dload_3(code, java_pos, java_locals):
    asm.Local(java_locals[3], code)
    code.word_size = 2


def convert_dstore_3(code, java_pos, java_locals):
    asm.LocalAssign(java_locals[3], code)
    code.word_size = 0


##########


def convert_fload_0(code, java_pos, java_locals):
    asm.Local(java_locals[0], code)
    code.word_size = 1


def convert_fstore_0(code, java_pos, java_locals):
    asm.LocalAssign(java_locals[0], code)
    code.word_size = 0


def convert_fload_1(code, java_pos, java_locals):
    asm.Local(java_locals[1], code)
    code.word_size = 1


def convert_fstore_1(code, java_pos, java_locals):
    asm.LocalAssign(java_locals[1], code)
    code.word_size = 0


def convert_fload_2(code, java_pos, java_locals):
    asm.Local(java_locals[2], code)
    code.word_size = 1


def convert_fstore_2(code, java_pos, java_locals):
    asm.LocalAssign(java_locals[2], code)
    code.word_size = 0


def convert_fload_3(code, java_pos, java_locals):
    asm.Local(java_locals[3], code)
    code.word_size = 1


def convert_fstore_3(code, java_pos, java_locals):
    asm.LocalAssign(java_locals[3], code)
    code.word_size = 0


##########


def convert_lload_0(code, java_pos, java_locals):
    asm.Local(java_locals[0], code)
    code.word_size = 2


def convert_lload_1(code, java_pos, java_locals):
    asm.Local(java_locals[1], code)
    code.word_size = 2


def convert_lload_2(code, java_pos, java_locals):
    asm.Local(java_locals[2], code)
    code.word_size = 2


def convert_lload_3(code, java_pos, java_locals):
    asm.Local(java_locals[3], code)
    code.word_size = 2


def convert_aconst_null(code, java_pos, java_locals):
    code(asm.Const(None))
    code.word_size = 1


######


def convert_dconst_0(code, java_pos, java_locals):
    code(asm.Const(0))
    code.word_size = 2


def convert_dconst_1(code, java_pos, java_locals):
    code(asm.Const(1))
    code.word_size = 2


######


def convert_fconst_0(code, java_pos, java_locals):
    code(asm.Const(0.0))
    code.word_size = 1


def convert_fconst_1(code, java_pos, java_locals):
    code(asm.Const(1.0))
    code.word_size = 1


def convert_fconst_2(code, java_pos, java_locals):
    code(asm.Const(2.0))
    code.word_size = 1


######


def convert_lconst_0(code, java_pos, java_locals):
    code(asm.Const(0))
    code.word_size = 2


def convert_lconst_1(code, java_pos, java_locals):
    code(asm.Const(1))
    code.word_size = 2


######


def convert_iconst_m1(code, java_pos, java_locals):
    code(asm.Const(-1))
    code.word_size = 1


def convert_iconst_0(code, java_pos, java_locals):
    code(asm.Const(0))
    code.word_size = 1


def convert_iconst_1(code, java_pos, java_locals):
    code(asm.Const(1))
    code.word_size = 1


def convert_iconst_2(code, java_pos, java_locals):
    code(asm.Const(2))
    code.word_size = 1


def convert_iconst_3(code, java_pos, java_locals):
    code(asm.Const(3))
    code.word_size = 1


def convert_iconst_4(code, java_pos, java_locals):
    code(asm.Const(4))
    code.word_size = 1


def convert_iconst_5(code, java_pos, java_locals):
    code(asm.Const(5))
    code.word_size = 1


def convert_getfield(code, java_pos, java_locals, class_name, descriptor, name):
    code.LOAD_ATTR(name)
    code.word_size = get_word_size(descriptor)


def convert_putfield(code, java_pos, java_locals, class_name, descriptor, name):
    code.ROT_TWO()
    code.STORE_ATTR(name)
    code.word_size = 0


def convert_bipush(code, java_pos, java_locals, value):
    code.LOAD_CONST(value)
    code.word_size = 1


def convert_sipush(code, java_pos, java_locals, value):
    code.LOAD_CONST(value)
    code.word_size = 1


def convert_i2d(code, java_pos, java_locals):
    # TODO: fix magnitude/sign during conversion
    code.word_size = 2


def convert_i2l(code, java_pos, java_locals):
    # TODO: fix magnitude/sign during conversion
    code.word_size = 2


def convert_f2i(code, java_pos, java_locals):
    # TODO: fix magnitude/sign during conversion
    code.word_size = 1


def convert_f2l(code, java_pos, java_locals):
    # TODO: fix magnitude/sign during conversion
    code.word_size = 2


def convert_l2i(code, java_pos, java_locals):
    # TODO: fix magnitude/sign during conversion
    code.word_size = 1


def convert_l2d(code, java_pos, java_locals):
    # TODO: fix magnitude/sign during conversion
    code.word_size = 2


def convert_d2l(code, java_pos, java_locals):
    # TODO: fix magnitude/sign during conversion
    code.word_size = 2


def convert_i2c(code, java_pos, java_locals):
    # TODO: fix magnitude/sign during conversion
    code.word_size = 1


def convert_c2i(code, java_pos, java_locals):
    # TODO: fix magnitude/sign during conversion
    code.word_size = 1


def convert_s2i(code, java_pos, java_locals):
    # TODO: fix magnitude/sign during conversion
    code.word_size = 1


def convert_i2s(code, java_pos, java_locals):
    # TODO: fix magnitude/sign during conversion
    code.word_size = 1


def convert_d2f(code, java_pos, java_locals):
    # TODO: fix magnitude/sign during conversion
    code.word_size = 1


def convert_l2f(code, java_pos, java_locals):
    # TODO: fix magnitude/sign during conversion
    code.word_size = 1


def convert_d2i(code, java_pos, java_locals):
    # TODO: fix magnitude/sign during conversion
    code.word_size = 1


def convert_f2d(code, java_pos, java_locals):
    # TODO: fix magnitude/sign during conversion
    code.word_size = 2


def convert_i2f(code, java_pos, java_locals):
    # TODO: fix magnitude/sign during conversion
    code.word_size = 1


def convert_i2b(code, java_pos, java_locals):
    # TODO: fix magnitude/sign during conversion
    code.word_size = 1


convert_ib2 = convert_i2b  # handle typo in jawa/util/bytecode.py


def convert_imul(code, java_pos, java_locals):
    code.BINARY_MULTIPLY()
    code.word_size = 1


def convert_dmul(code, java_pos, java_locals):
    code.BINARY_MULTIPLY()
    code.word_size = 2


def convert_fmul(code, java_pos, java_locals):
    code.BINARY_MULTIPLY()
    code.word_size = 1


def convert_fsub(code, java_pos, java_locals):
    code.BINARY_SUBTRACT()
    code.word_size = 1


def convert_iadd(code, java_pos, java_locals):
    code.BINARY_ADD()
    code.word_size = 1


def convert_fadd(code, java_pos, java_locals):
    code.BINARY_ADD()
    code.word_size = 1


def convert_ladd(code, java_pos, java_locals):
    code.BINARY_ADD()
    code.word_size = 2


def convert_lmul(code, java_pos, java_locals):
    code.BINARY_MULTIPLY()
    code.word_size = 2


def convert_dadd(code, java_pos, java_locals):
    code.BINARY_ADD()
    code.word_size = 2


def convert_idiv(code, java_pos, java_locals):
    # TODO: check divide op
    code.BINARY_DIVIDE()
    code.word_size = 1


def convert_fdiv(code, java_pos, java_locals):
    # TODO: check divide op
    code.BINARY_DIVIDE()
    code.word_size = 1


def convert_ineg(code, java_pos, java_locals):
    code.UNARY_NEGATIVE()
    code.word_size = 1


def convert_fneg(code, java_pos, java_locals):
    code.UNARY_NEGATIVE()
    code.word_size = 1


def convert_dneg(code, java_pos, java_locals):
    code.UNARY_NEGATIVE()
    code.word_size = 2


def convert_lneg(code, java_pos, java_locals):
    code.UNARY_NEGATIVE()
    code.word_size = 2


def convert_isub(code, java_pos, java_locals):
    code.BINARY_SUBTRACT()
    code.word_size = 1


def convert_dsub(code, java_pos, java_locals):
    code.BINARY_SUBTRACT()
    code.word_size = 1


def convert_lsub(code, java_pos, java_locals):
    code.BINARY_SUBTRACT()
    code.word_size = 2


def convert_ldiv(code, java_pos, java_locals):
    code.BINARY_DIVIDE()
    code.word_size = 2


def convert_ddiv(code, java_pos, java_locals):
    code.BINARY_DIVIDE()
    code.word_size = 2


def convert_ixor(code, java_pos, java_locals):
    code.BINARY_XOR()
    code.word_size = 1


def convert_lxor(code, java_pos, java_locals):
    code.BINARY_XOR()
    code.word_size = 2


def convert_iand(code, java_pos, java_locals):
    code.BINARY_AND()
    code.word_size = 1


def convert_ior(code, java_pos, java_locals):
    code.BINARY_OR()
    code.word_size = 1


def convert_irem(code, java_pos, java_locals):
    code.BINARY_MODULO()
    code.word_size = 1


def convert_lrem(code, java_pos, java_locals):
    code.BINARY_MODULO()
    code.word_size = 2


def convert_lor(code, java_pos, java_locals):
    code.BINARY_OR()
    code.word_size = 2


def convert_land(code, java_pos, java_locals):
    code.BINARY_AND()
    code.word_size = 2


def convert_ishl(code, java_pos, java_locals):
    code(31)    # number with lowest 5 bits set
    code.BINARY_AND()
    code.BINARY_LSHIFT()
    code.word_size = 1


def convert_ishr(code, java_pos, java_locals):
    code(31)    # number with lowest 5 bits set
    code.BINARY_AND()
    code.BINARY_RSHIFT()
    code.word_size = 1


def convert_iushl(code, java_pos, java_locals):
    code(31)    # number with lowest 5 bits set
    code.BINARY_AND()
    code.BINARY_LSHIFT()
    code.word_size = 1


def convert_iushr(code, java_pos, java_locals):
    code(31)    # number with lowest 5 bits set
    code.BINARY_AND()
    code.BINARY_RSHIFT()
    code.word_size = 1


def convert_lshl(code, java_pos, java_locals):
    code(63)    # number with lowest 6 bits set
    code.BINARY_AND()
    code.BINARY_LSHIFT()
    code.word_size = 2


def convert_lshr(code, java_pos, java_locals):
    code(63)    # number with lowest 6 bits set
    code.BINARY_AND()
    code.BINARY_RSHIFT()
    code.word_size = 2


def convert_lushl(code, java_pos, java_locals):
    code(63)    # number with lowest 6 bits set
    code.BINARY_AND()
    code.BINARY_LSHIFT()
    code.word_size = 2


def convert_lushr(code, java_pos, java_locals):
    code(63)    # number with lowest 6 bits set
    code.BINARY_AND()
    code.BINARY_RSHIFT()
    code.word_size = 2


JumpTarget = namedtuple('JumpTarget', ['python_offset', 'java_pos', 'python_stack_size'])


def convert_goto(code, java_pos, java_locals, offset):
    add_forward_jump(code, java_pos + offset)


def add_forward_jump(code, java_pos):
    current = len(code.co_code)
    code.jumps.append(JumpTarget(current, java_pos, code.get_stack_size()))
    code.JUMP_FORWARD(current + 3)
    code.set_stack_size(0)


def handle_jumps(code, java_pos):
    for jump in code.jumps:
        if DEBUG: print '###', jump, java_pos
        if jump.java_pos == java_pos:
            if DEBUG: print '### fix', jump, len(code.co_code)
            code.patch_arg(jump.python_offset, 0, len(code.co_code))
            if not code.get_stack_size():
                code.set_stack_size(jump.python_stack_size)


def convert_lookupswitch(code, java_pos, java_locals, lookup_dict, default):
    # key is on the stack
    # lookup_dict looks like {0: 68, 1: 74, 2: 80, 5: 86, 47: 92, 59: 98, 61: 104}
    # keys compared with the top of the stack, values are offset from current pos
    # default looks like 107
    key_to_compare_with = '$lookup$%d' % java_pos
    code(asm.LocalAssign(key_to_compare_with))
    for key, offset in lookup_dict.iteritems():
        code(asm.Local(key_to_compare_with))
        code(key)
        handle_comparison(code, java_pos + offset, None, '==')
    add_forward_jump(code, java_pos + default)
    # TODO: optimize first case, which could avoid a jump


def convert_tableswitch(code, java_pos, java_locals, *table):
    stack_size = code.get_stack_size()
    default, low, high = table[:3]
    jumps = table[3:]
    for n, target in enumerate(jumps):
        code.DUP_TOP()
        handle_comparison(code, java_pos + default, low + n, '==')
    code.POP_TOP()
    add_forward_jump(code, java_pos + default)
    code.set_stack_size(stack_size - 1)


def convert_newarray(code, java_pos, java_locals, size):
    code(None)
    code.BUILD_LIST(1)
    code(size)
    code.BINARY_MULTIPLY()
    code.word_size = 1

def convert_ifnull(code, java_pos, java_locals, offset):
    handle_comparison(code, java_pos + offset, asm.Const(None), '==')


def convert_ifnonnull(code, java_pos, java_locals, offset):
    handle_comparison(code, java_pos + offset, asm.Const(None), '!=')

##############

def convert_ifeq(code, java_pos, java_locals, offset):
    handle_comparison(code, java_pos + offset, asm.Const(0), '==')


def convert_ifne(code, java_pos, java_locals, offset):
    handle_comparison(code, java_pos + offset, asm.Const(0), '!=')


def convert_ifle(code, java_pos, java_locals, offset):
    handle_comparison(code, java_pos + offset, asm.Const(0), '<=')


def convert_iflt(code, java_pos, java_locals, offset):
    handle_comparison(code, java_pos + offset, asm.Const(0), '<')


def convert_ifge(code, java_pos, java_locals, offset):
    handle_comparison(code, java_pos + offset, asm.Const(0), '>=')


def convert_ifgt(code, java_pos, java_locals, offset):
    handle_comparison(code, java_pos + offset, asm.Const(0), '>')

##############

def convert_if_acmpeq(code, java_pos, java_locals, offset):
    handle_comparison(code, java_pos + offset, None, '==')


def convert_if_acmpne(code, java_pos, java_locals, offset):
    handle_comparison(code, java_pos + offset, None, '!=')


def convert_if_acmple(code, java_pos, java_locals, offset):
    handle_comparison(code, java_pos + offset, None, '<=')


def convert_if_acmplt(code, java_pos, java_locals, offset):
    handle_comparison(code, java_pos + offset, None, '<')


def convert_if_acmpge(code, java_pos, java_locals, offset):
    handle_comparison(code, java_pos + offset, None, '>=')


def convert_if_acmpgt(code, java_pos, java_locals, offset):
    handle_comparison(code, java_pos + offset, None, '>')

##############

def convert_if_icmpeq(code, java_pos, java_locals, offset):
    handle_comparison(code, java_pos + offset, None, '==')


def convert_if_icmpne(code, java_pos, java_locals, offset):
    handle_comparison(code, java_pos + offset, None, '!=')


def convert_if_icmple(code, java_pos, java_locals, offset):
    handle_comparison(code, java_pos + offset, None, '<=')


def convert_if_icmplt(code, java_pos, java_locals, offset):
    handle_comparison(code, java_pos + offset, None, '<')


def convert_if_icmpge(code, java_pos, java_locals, offset):
    handle_comparison(code, java_pos + offset, None, '>=')


def convert_if_icmpgt(code, java_pos, java_locals, offset):
    handle_comparison(code, java_pos + offset, None, '>')

##############

def handle_comparison(code, java_target, constant_to_compare_with, comparison_operator):
    if constant_to_compare_with is not None:
        code(constant_to_compare_with)
    code.COMPARE_OP(comparison_operator)
    current = len(code.co_code)
    code.POP_JUMP_IF_TRUE(current + 3)
    code.jumps.append(JumpTarget(current, java_target, code.get_stack_size()))


def convert_lcmp(code, java_pos, java_locals):
    code(asm.If('>', 1, [asm.If('<', -1, 0)]))


def convert_fcmpg(code, java_pos, java_locals):
    code(asm.If('>', 1, [asm.If('<', -1, 0)]))


def convert_fcmpl(code, java_pos, java_locals):
    code(asm.If('<', 1, [asm.If('>', -1, 0)]))


def convert_dcmpg(code, java_pos, java_locals):
    code(asm.If('>', 1, [asm.If('<', -1, 0)]))


def convert_dcmpl(code, java_pos, java_locals):
    code(asm.If('<', 1, [asm.If('>', -1, 0)]))


def convert_monitorenter(code, java_pos, java_locals):
    # TODO: implement monitors
    code.POP_TOP()


def convert_monitorexit(code, java_pos, java_locals):
    # TODO: implement monitors
    code.POP_TOP()


def resolve_operands(constants, operands):
    if DEBUG:
        print operands,
    if not operands:
        return tuple()

    result = []
    for operand in operands:
        if isinstance(operand, dict):
            result.append(operand)
        elif operand.op_type == jawa.util.bytecode.OperandTypes.BRANCH:
            result.extend(resolve_operand_branch(operand))
        elif operand.op_type == jawa.util.bytecode.OperandTypes.CONSTANT_INDEX:
            result.extend(resolve_operand_constant(operand, constants))
        elif operand.op_type == jawa.util.bytecode.OperandTypes.LOCAL_INDEX:
            result.extend(resolve_operand_local(operand))
        elif operand.op_type == jawa.util.bytecode.OperandTypes.LITERAL:
            result.append(operand.value)
        elif operand.op_type == jawa.util.bytecode.OperandTypes.PADDING:
            pass
        else:
            raise NotImplementedError('Java operand not yet implemented: %s' % operand.op_type)

    return result

def resolve_operand_branch(operand):
    return operand.value,


def resolve_operand_local(operand):
    return operand.value,


def resolve_operand_constant(operand, constants):
    if operand.value not in constants:
        for k,v in enumerate(constants):
            print 'CONST ', k, v
        raise ValueError('Bad constant: %d' % operand.value)
    ref = constants[operand.value]
    if isinstance(ref, jawa.ConstantString):
        return ref.string.value,
    if isinstance(ref, jawa.ConstantInteger):
        return ref.value,
    if isinstance(ref, jawa.ConstantFloat):
        return ref.value,
    if isinstance(ref, jawa.ConstantDouble):
        return ref.value,
    if isinstance(ref, jawa.ConstantLong):
        return ref.value,
    if isinstance(ref, jawa.ConstantUTF8):
        return ref.value,
    if isinstance(ref, jawa.ConstantFieldRef):
        return (
            fix_dollar_sign(str(ref.class_.name.value)),
            str(ref.name_and_type.descriptor.value),
            str(ref.name_and_type.name.value)
        )
    if isinstance(ref, jawa.ConstantNameAndType):
        return str(ref.name.value), str(ref.descriptor.value)
    if isinstance(ref, jawa.ConstantMethodRef) or isinstance(ref, jawa.ConstantInterfaceMethodRef):
        descriptor = jawa.util.descriptor.method_descriptor( ref.name_and_type.descriptor.value)
        return (
            fix_dollar_sign(str(ref.class_.name.value)),
            str(ref.name_and_type.name.value),
            str(ref.name_and_type.descriptor.value),
            len(descriptor.args)
        )
    if isinstance(ref, jawa.ConstantClass):
        return ref.name.value,

    raise NotImplementedError('Java constant reference not yet implemented: %s' % ref)


def fix_dollar_sign(class_name):
    return class_name.replace('$', '__')


class OpcodeMap(dict):
    def __missing__(self, key):
        raise NotImplementedError('Java bytecode not yet implemented: %s' % key)


module = sys.modules[__name__]
opcode_map = OpcodeMap((k[8:],getattr(module, k)) for k in dir(module) if k.startswith('convert_'))


def convert(java_opcode, code, java_pos, java_locals, *operands):
    if DEBUG:
        print '    ### %-15s %s'  % (java_opcode, operands)
    code.java_bytecodes.append((len(code.co_code), (java_opcode, java_pos, operands)))
    handle_jumps(code, java_pos)
    opcode_map[java_opcode](code, java_pos, java_locals, *operands)
    code.stack_depth.append((len(code.co_code), code.get_stack_size()))



