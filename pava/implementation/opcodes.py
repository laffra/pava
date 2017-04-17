from collections import namedtuple
import pava
import sys

DEBUG = False


def convert_ldc(python_method, java_index, value):
    python_method.push(java_index, repr(value))


def convert_ldc_w(python_method, java_index, value):
    python_method.push(java_index, repr(value))


def convert_ldc2_w(python_method, java_index, value):
    python_method.push(java_index, repr(value))


def convert_instanceof(python_method, java_index, class_name):
    python_method.add_class_reference(class_name)
    python_method.push(java_index, 'isinstance(%s, %s)' % (python_method.pop(), class_name))


def convert_arraylength(python_method, java_index):
    python_method.push(java_index, 'len(%s)' % python_method.pop())


def convert_getstatic(python_method, java_index, field):
    python_method.add_class_reference(replace_reserved_names(field.class_name))
    python_method.push(java_index, '%s.%s' % (replace_reserved_names(field.class_name),
                                              replace_reserved_names(field.field_name)))


def convert_putstatic(python_method, java_index, field):
    python_method.add_class_reference(replace_reserved_names(field.class_name))
    python_method.push(java_index, '%s.%s = %s' % (replace_reserved_names(field.class_name),
                                                   replace_reserved_names(field.field_name),
                                                   python_method.pop()), is_statement=True)


def convert_new(python_method, java_index, class_name):
    python_method.add_class_reference(replace_reserved_names(class_name))
    python_method.push(java_index, '%s()' % replace_reserved_names(class_name))


def convert_anewarray(python_method, java_index, class_):
    python_method.push(java_index, '[]')


def convert_checkcast(python_method, java_index, class_name):
    python_method.add_class_reference(class_name)
    python_method.push(java_index, 'pava.checkcast(%s, %s)' % (python_method.pop(), class_name))


def convert_invokevirtual(python_method, java_index, method):
    invoke_instance_method(python_method, java_index, method)


def convert_invokeinterface(python_method, java_index, method):
    invoke_instance_method(python_method, java_index, method)


def is_self_opcode(code, index):
    return code.co_code[index] == 124 and code.co_code[index + 1] == 0 and code.co_code[index + 2] == 0


def convert_invokespecial(python_method, java_index, java_method):
    python_method.add_class_reference(java_method.class_name)
    args = map(str, python_method.pop_args(len(java_method.args) + 1))
    if args[0] == 'self':
        expression = '%s.%s(%s)' % (java_method.class_name, java_method.method_name, ', '.join(args))
    else:
        expression = '%s.%s(%s)' % (args[0], java_method.method_name, ', '.join(args[1:]))
    python_method.push(java_index, expression, java_method.return_type == 'void')

def convert_invokestatic(python_method, java_index, java_method):
    python_method.add_class_reference(java_method.class_name)
    args = map(str, python_method.pop_args(len(java_method.args)))
    expression = '%s.%s(%s)' % (java_method.class_name, java_method.method_name, ', '.join(args))
    python_method.push(java_index, expression, java_method.return_type == 'void')


def convert_invokedynamic(python_method, java_index, java_method):
    python_method.add_class_reference(java_method.class_name)
    args = map(str, python_method.pop_args(len(java_method.args)))
    expression = '%s.%s(%s)' % (java_method.class_name, java_method.method_name, ', '.join(args))
    python_method.push(java_index, expression, java_method.return_type == 'void')


def invoke_instance_method(python_method, java_index, java_method):
    if java_method.method_name == 'toString____' and len(java_method.args) == 0:
        return python_method.push(java_index, 'str(%s)' % python_method.pop())

    args = map(str, python_method.pop_args(len(java_method.args) + 1))
    expression = '%s.%s(%s)' % (args[0], java_method.method_name, ', '.join(args[1:]))
    python_method.push(java_index, expression, java_method.return_type == 'void')


def convert_pop(python_method, java_index):
    python_method.push(java_index, '_ = %s' % python_method.pop(), is_statement=True)


def convert_pop2(python_method, java_index):
    python_method.push(java_index, '_ = %s' % python_method.pop(), is_statement=True)


def convert_areturn(python_method, java_index):
    python_method.push(java_index, 'return %s' % python_method.pop())


def convert_dup(python_method, java_index):
    # before: word1, ...
    word1 = python_method.pop()
    tmp = python_method.next_temp()
    # after: tmp1, tmp1, tmp1=word1, ...
    python_method.push(java_index, '%s = %s' % (tmp, word1), is_statement=True)
    python_method.push(java_index, '%s' % tmp)
    python_method.push(java_index, '%s' % tmp)


def convert_dup_x1(python_method, java_index):
    # before: word1, word2, ...
    word1 = python_method.pop()
    word2 = python_method.pop()
    tmp = python_method.next_temp()
    # after: tmp1, word2, tmp1, tmp1=word1, ...
    python_method.push(java_index, '%s = %s' % (tmp, word1))
    python_method.push(java_index, '%s' % tmp)
    python_method.push(java_index, '%s' % word2)
    python_method.push(java_index, '%s' % tmp)


def convert_dup_x2(python_method, java_index):
    # before: word1, word2, ...
    word1 = python_method.pop()
    word2 = python_method.pop()
    tmp = python_method.next_temp()
    # after: tmp1, word2, tmp1, tmp1=word1, ...
    python_method.push(java_index, '%s = %s' % (tmp, word1))
    python_method.push(java_index, '%s' % tmp)
    python_method.push(java_index, '%s' % word2)
    python_method.push(java_index, '%s' % tmp)

def convert_dup2_x2(python_method, java_index):
    convert_dup_x2(python_method, java_index)

def convert_dup2(python_method, java_index):
    convert_dup(python_method, java_index)

def convert_dup2_x1(python_method, java_index):
    convert_dup_x1(python_method, java_index)


def convert_ireturn(python_method, java_index):
    python_method.push(java_index, 'return %s' % python_method.pop())


def convert_dreturn(python_method, java_index):
    python_method.push(java_index, 'return %s' % python_method.pop())


def convert_freturn(python_method, java_index):
    python_method.push(java_index, 'return %s' % python_method.pop())


def convert_lreturn(python_method, java_index):
    python_method.push(java_index, 'return %s' % python_method.pop())


def convert_return(python_method, java_index):
    if '__java_init__' in python_method.name:
        python_method.push(java_index, 'return self')
    else:
        python_method.push(java_index, 'return None')


def convert_aastore(python_method, java_index):
    array, index, value =  python_method.pop(3)
    python_method.push(java_index, '%s[%s] = %s' % (array, index, value), is_statement=True)


def convert_aaload(python_method, java_index):
    array, index =  python_method.pop(2)
    python_method.push(java_index, '%s[%s]' % (array, index))


def convert_iastore(python_method, java_index):
    array, index, value =  python_method.pop(3)
    python_method.push(java_index, '%s[%s] = %s' % (array, index, value), is_statement=True)


def convert_fastore(python_method, java_index):
    array, index, value =  python_method.pop(3)
    python_method.push(java_index, '%s[%s] = %s' % (array, index, value), is_statement=True)


def convert_dastore(python_method, java_index):
    array, index, value =  python_method.pop(3)
    python_method.push(java_index, '%s[%s] = %s' % (array, index, value), is_statement=True)


def convert_lastore(python_method, java_index):
    array, index, value =  python_method.pop(3)
    python_method.push(java_index, '%s[%s] = %s' % (array, index, value), is_statement=True)


def convert_sastore(python_method, java_index):
    array, index, value =  python_method.pop(3)
    python_method.push(java_index, '%s[%s] = %s' % (array, index, value), is_statement=True)


def convert_bastore(python_method, java_index):
    array, index, value =  python_method.pop(3)
    python_method.push(java_index, '%s[%s] = %s' % (array, index, value), is_statement=True)


def convert_iaload(python_method, java_index):
    array, index =  python_method.pop(2)
    python_method.push(java_index, '%s[%s]' % (array, index))


def convert_saload(python_method, java_index):
    array, index =  python_method.pop(2)
    python_method.push(java_index, '%s[%s]' % (array, index))


def convert_baload(python_method, java_index):
    array, index =  python_method.pop(2)
    python_method.push(java_index, '%s[%s]' % (array, index))


def convert_laload(python_method, java_index):
    array, index =  python_method.pop(2)
    python_method.push(java_index, '%s[%s]' % (array, index))


def convert_daload(python_method, java_index):
    array, index =  python_method.pop(2)
    python_method.push(java_index, '%s[%s]' % (array, index))


def convert_faload(python_method, java_index):
    array, index =  python_method.pop(2)
    python_method.push(java_index, '%s[%s]' % (array, index))


def convert_castore(python_method, java_index):
    array, index, value =  python_method.pop(3)
    python_method.push(java_index, '%s[%s] = %s' % (array, index, value), is_statement=True)


def convert_caload(python_method, java_index):
    array, index =  python_method.pop(2)
    python_method.push(java_index, '%s[%s]' % (array, index))


def convert_athrow(python_method, java_index):
    python_method.push(java_index, 'raise %s' % python_method.pop(), is_statement=True)


##########


def convert_iinc(python_method, java_index, operands):
    index, value = operands
    python_method.push(java_index, 'a%d += %s' % (index, value), is_statement=True)

def convert_iinc_w(python_method, java_index, operands):
    index, value = operands
    python_method.push(java_index, 'a%d += %s' % (index, value), is_statement=True)


##########


def convert_aload(python_method, java_index, index):
    python_method.push(java_index, 'a%d' % index)


def convert_astore(python_method, java_index, index):
    python_method.push(java_index, 'a%d = %s' % (index, python_method.pop()), is_statement=True)


##########


def convert_iload(python_method, java_index, index):
    python_method.push(java_index, 'a%d' % index)


def convert_istore(python_method, java_index, index):
    python_method.push(java_index, 'a%d = %s' % (index, python_method.pop()), is_statement=True)


##########


def convert_fload(python_method, java_index, index):
    python_method.push(java_index, 'a%d' % index)


def convert_fstore(python_method, java_index, index):
    python_method.push(java_index, 'a%d = %s' % (index, python_method.pop()), is_statement=True)


##########


def convert_dload(python_method, java_index, index):
    python_method.push(java_index, 'a%d' % index)


def convert_dstore(python_method, java_index, index):
    python_method.push(java_index, 'a%d = %s' % (index, python_method.pop()), is_statement=True)


##########


def convert_lload(python_method, java_index, index):
    python_method.push(java_index, 'a%d' % index)


def convert_lstore(python_method, java_index, index):
    python_method.push(java_index, 'a%d = %s' % (index, python_method.pop()), is_statement=True)


##########


def convert_aload_0(python_method, java_index):
    python_method.push(java_index, 'cls' if python_method.is_static else 'self')


def convert_astore_0(python_method, java_index):
    target = 'cls' if python_method.is_static else 'self'
    python_method.push(java_index, '%s = %s' % (target, python_method.pop()), is_statement=True)


def convert_aload_1(python_method, java_index):
    python_method.push(java_index, 'a1')


def convert_astore_1(python_method, java_index):
    python_method.push(java_index, 'a1 = %s' % python_method.pop(), is_statement=True)


def convert_aload_2(python_method, java_index):
    python_method.push(java_index, 'a2')


def convert_astore_2(python_method, java_index):
    python_method.push(java_index, 'a2 = %s' % python_method.pop(), is_statement=True)


def convert_aload_3(python_method, java_index):
    python_method.push(java_index, 'a3')


def convert_astore_3(python_method, java_index):
    python_method.push(java_index, 'a3 = %s' % python_method.pop(), is_statement=True)


##########


def convert_iload_0(python_method, java_index):
    python_method.push(java_index, 'a0')


def convert_istore_0(python_method, java_index):
    python_method.push(java_index, 'a0 = %s' % python_method.pop(), is_statement=True)


def convert_iload_1(python_method, java_index):
    python_method.push(java_index, 'a1')


def convert_istore_1(python_method, java_index):
    python_method.push(java_index, 'a1 = %s' % python_method.pop(), is_statement=True)


def convert_iload_2(python_method, java_index):
    python_method.push(java_index, 'a2')


def convert_istore_2(python_method, java_index):
    python_method.push(java_index, 'a2 = %s' % python_method.pop(), is_statement=True)


def convert_iload_3(python_method, java_index):
    python_method.push(java_index, 'a3')


def convert_istore_3(python_method, java_index):
    python_method.push(java_index, 'a3 = %s' % python_method.pop(), is_statement=True)


##########


def convert_lload_0(python_method, java_index):
    python_method.push(java_index, 'a0')


def convert_lstore_0(python_method, java_index):
    python_method.push(java_index, 'a0 = %s' % python_method.pop(), is_statement=True)


def convert_lload_1(python_method, java_index):
    python_method.push(java_index, 'a1')


def convert_lstore_1(python_method, java_index):
    python_method.push(java_index, 'a1 = %s' % python_method.pop(), is_statement=True)


def convert_lload_2(python_method, java_index):
    python_method.push(java_index, 'a2')


def convert_lstore_2(python_method, java_index):
    python_method.push(java_index, 'a2 = %s' % python_method.pop(), is_statement=True)


def convert_lload_3(python_method, java_index):
    python_method.push(java_index, 'a3')


def convert_lstore_3(python_method, java_index):
    python_method.push(java_index, 'a3 = %s' % python_method.pop(), is_statement=True)


##########


def convert_dload_0(python_method, java_index):
    python_method.push(java_index, 'a0')


def convert_dstore_0(python_method, java_index):
    python_method.push(java_index, 'a0 = %s' % python_method.pop(), is_statement=True)


def convert_dload_1(python_method, java_index):
    python_method.push(java_index, 'a1')


def convert_dstore_1(python_method, java_index):
    python_method.push(java_index, 'a1 = %s' % python_method.pop(), is_statement=True)


def convert_dload_2(python_method, java_index):
    python_method.push(java_index, 'a2')


def convert_dstore_2(python_method, java_index):
    python_method.push(java_index, 'a2 = %s' % python_method.pop(), is_statement=True)


def convert_dload_3(python_method, java_index):
    python_method.push(java_index, 'a3')


def convert_dstore_3(python_method, java_index):
    python_method.push(java_index, 'a3 = %s' % python_method.pop(), is_statement=True)


##########


def convert_fload_0(python_method, java_index):
    python_method.push(java_index, 'a0')


def convert_fstore_0(python_method, java_index):
    python_method.push(java_index, 'a0 = %s' % python_method.pop(), is_statement=True)


def convert_fload_1(python_method, java_index):
    python_method.push(java_index, 'a1')


def convert_fstore_1(python_method, java_index):
    python_method.push(java_index, 'a1 = %s' % python_method.pop(), is_statement=True)


def convert_fload_2(python_method, java_index):
    python_method.push(java_index, 'a2')


def convert_fstore_2(python_method, java_index):
    python_method.push(java_index, 'a2 = %s' % python_method.pop(), is_statement=True)


def convert_fload_3(python_method, java_index):
    python_method.push(java_index, 'a3')


def convert_fstore_3(python_method, java_index):
    python_method.push(java_index, 'a3 = %s' % python_method.pop(), is_statement=True)


##########


def convert_aconst_null(python_method, java_index):
    python_method.push(java_index, 'None')


def convert_dconst_0(python_method, java_index):
    python_method.push(java_index, 0.0)


def convert_dconst_1(python_method, java_index):
    python_method.push(java_index, 1.0)


def convert_fconst_0(python_method, java_index):
    python_method.push(java_index, 0.0)


def convert_fconst_1(python_method, java_index):
    python_method.push(java_index, 1.0)


def convert_fconst_2(python_method, java_index):
    python_method.push(java_index, 2.0)


def convert_lconst_0(python_method, java_index):
    python_method.push(java_index, 0)


def convert_lconst_1(python_method, java_index):
    python_method.push(java_index, 1)


def convert_iconst_m1(python_method, java_index):
    python_method.push(java_index, '-1')


def convert_iconst_0(python_method, java_index):
    python_method.push(java_index, '0')


def convert_iconst_1(python_method, java_index):
    python_method.push(java_index, '1')


def convert_iconst_2(python_method, java_index):
    python_method.push(java_index, '2')


def convert_iconst_3(python_method, java_index):
    python_method.push(java_index, '3')


def convert_iconst_4(python_method, java_index):
    python_method.push(java_index, '4')


def convert_iconst_5(python_method, java_index):
    python_method.push(java_index, '5')


def convert_getfield(python_method, java_index, field):
    python_method.push(java_index, '%s.%s' % (
        python_method.pop(),
        replace_reserved_names(field.field_name))
    )


def convert_putfield(python_method, java_index, field):
    value, obj = python_method.pop(), python_method.pop()
    python_method.push(java_index, '%s.%s = %s' % (
        obj,
        replace_reserved_names(field.field_name),
        value,
    ), is_statement=True)


def convert_bipush(python_method, java_index, value):
    python_method.push(java_index, value)


def convert_sipush(python_method, java_index, value):
    python_method.push(java_index, value)


def convert_i2d(python_method, java_index):
    pass # TODO: fix magnitude/sign during conversion


def convert_i2l(python_method, java_index):
    pass # TODO: fix magnitude/sign during conversion


def convert_f2i(python_method, java_index):
    python_method.push(java_index, 'int(%s)' % python_method.pop())


def convert_f2l(python_method, java_index):
    pass # TODO: fix magnitude/sign during conversion


def convert_l2i(python_method, java_index):
    pass # TODO: fix magnitude/sign during conversion


def convert_l2d(python_method, java_index):
    pass # TODO: fix magnitude/sign during conversion


def convert_d2l(python_method, java_index):
    pass # TODO: fix magnitude/sign during conversion


def convert_i2c(python_method, java_index):
    pass # TODO: fix magnitude/sign during conversion


def convert_c2i(python_method, java_index):
    pass # TODO: fix magnitude/sign during conversion


def convert_s2i(python_method, java_index):
    pass # TODO: fix magnitude/sign during conversion


def convert_i2s(python_method, java_index):
    pass # TODO: fix magnitude/sign during conversion


def convert_d2f(python_method, java_index):
    pass # TODO: fix magnitude/sign during conversion


def convert_l2f(python_method, java_index):
    python_method.push(java_index, 'float(%s)' % python_method.pop())


def convert_d2i(python_method, java_index):
    python_method.push(java_index, 'int(%s)' % python_method.pop())


def convert_f2d(python_method, java_index):
    pass # TODO: fix magnitude/sign during conversion


def convert_i2f(python_method, java_index):
    pass # TODO: fix magnitude/sign during conversion


def convert_i2b(python_method, java_index):
    pass # TODO: fix magnitude/sign during conversion


def binary_operator(python_method, operator, java_index):
    operand2 = python_method.pop()
    operand1 = python_method.pop()
    python_method.push(java_index, '%s %s %s' % (operand1, operator, operand2))


def unary_operator(python_method, operator, java_index):
    python_method.push(java_index, '%s%s' % (operator, python_method.pop()))


def convert_imul(python_method, java_index):
    binary_operator(python_method, '*', java_index)


def convert_dmul(python_method, java_index):
    binary_operator(python_method, '*', java_index)


def convert_fmul(python_method, java_index):
    binary_operator(python_method, '*', java_index)


def convert_fsub(python_method, java_index):
    binary_operator(python_method, '-', java_index)


def convert_iadd(python_method, java_index):
    binary_operator(python_method, '+', java_index)


def convert_fadd(python_method, java_index):
    binary_operator(python_method, '+', java_index)


def convert_ladd(python_method, java_index):
    binary_operator(python_method, '+', java_index)


def convert_lmul(python_method, java_index):
    binary_operator(python_method, '*', java_index)


def convert_dadd(python_method, java_index):
    binary_operator(python_method, '+', java_index)


def convert_idiv(python_method, java_index):
    binary_operator(python_method, '/', java_index)


def convert_fdiv(python_method, java_index):
    binary_operator(python_method, '/', java_index)


def convert_ineg(python_method, java_index):
    unary_operator(python_method, '-', java_index)


def convert_fneg(python_method, java_index):
    unary_operator(python_method, '-', java_index)


def convert_dneg(python_method, java_index):
    unary_operator(python_method, '-', java_index)


def convert_lneg(python_method, java_index):
    unary_operator(python_method, '-', java_index)


def convert_isub(python_method, java_index):
    binary_operator(python_method, '/', java_index)


def convert_dsub(python_method, java_index):
    binary_operator(python_method, '-', java_index)


def convert_lsub(python_method, java_index):
    binary_operator(python_method, '-', java_index)


def convert_ldiv(python_method, java_index):
    binary_operator(python_method, '/', java_index)


def convert_ddiv(python_method, java_index):
    binary_operator(python_method, '/', java_index)


def convert_ixor(python_method, java_index):
    binary_operator(python_method, '^', java_index)


def convert_lxor(python_method, java_index):
    binary_operator(python_method, '^', java_index)


def convert_iand(python_method, java_index):
    binary_operator(python_method, '&', java_index)


def convert_ior(python_method, java_index):
    binary_operator(python_method, '&', java_index)


def convert_irem(python_method, java_index):
    binary_operator(python_method, '%', java_index)


def convert_lrem(python_method, java_index):
    binary_operator(python_method, '%', java_index)


def convert_drem(python_method, java_index):
    binary_operator(python_method, '%', java_index)


def convert_lor(python_method, java_index):
    binary_operator(python_method, '|', java_index)


def convert_land(python_method, java_index):
    binary_operator(python_method, '&', java_index)


def convert_ishl(python_method, java_index):
    python_method.push(java_index, '(%s & 31) << %s' % (python_method.pop(), python_method.pop()))


def convert_ishr(python_method, java_index):
    python_method.push(java_index, '(%s & 31) >> %s' % (python_method.pop(), python_method.pop()))


def convert_iushl(python_method, java_index):
    python_method.push(java_index, '(%s & 31) << %s' % (python_method.pop(), python_method.pop()))


def convert_iushr(python_method, java_index):
    python_method.push(java_index, '(%s & 31) >> %s' % (python_method.pop(), python_method.pop()))


def convert_lshl(python_method, java_index):
    python_method.push(java_index, '(%s & 63) << %s' % (python_method.pop(), python_method.pop()))


def convert_lshr(python_method, java_index):
    python_method.push(java_index, '(%s & 63) >> %s' % (python_method.pop(), python_method.pop()))


def convert_lushl(python_method, java_index):
    python_method.push(java_index, '(%s & 63) << %s' % (python_method.pop(), python_method.pop()))


def convert_lushr(python_method, java_index):
    python_method.push(java_index, '(%s & 63) >> %s' % (python_method.pop(), python_method.pop()))


JumpTarget = namedtuple('JumpTarget', ['python_offset', 'java_index', 'python_stack_size'])
Injection = namedtuple('Injection', ['index', 'count', 'target'])


def convert_goto(python_method, java_index, java_target_index):
    if java_target_index > java_index:
        expression = python_method.add_else(java_index, java_target_index)
    else:
        expression = python_method.add_loop(java_index, java_target_index)
    python_method.push(java_index, expression, is_statement=True)


def convert_jsr(python_method, java_index, java_target_index):
    python_method.push(java_index, '"jsr not implemented"')


def convert_ret(python_method, java_index, value):
    python_method.push(java_index, '"ret not implemented"')


def convert_lookupswitch(python_method, java_index, lookup_dict):
    python_method.add_lookup_switch(java_index, lookup_dict)


def convert_case(python_method, java_index, operands):
    python_method.push(java_index, '# CASE=%s=%s=%s' % operands)


def convert_default(python_method, java_index, operands):
    if python_method.previous_ins.opcode != 'switchend':
        python_method.push(java_index, '# DEFAULT=%s=%s=%s' % operands)


def convert_switchend(python_method, java_index, operands):
    python_method.push(java_index, '# ENDSWITCH=%s=%s=%s' % operands)


def convert_tableswitch(python_method, java_index, table_dict):
    convert_lookupswitch(python_method, java_index, table_dict)
    # TODO: optimize low/high, do binary search


DEFAULT_VALUES = {
    'char': "' '",
    'byte': 0,
    'short': 0,
    'int': 0,
    'long': 0,
    'double': 0.0,
    'float': 0.0,
    'boolean': False,
}

def convert_newarray(python_method, java_index, element_type):
    python_method.push(java_index, '[%s] * %s' % (DEFAULT_VALUES.get(element_type, None), python_method.pop()))


def convert_multianewarray(python_method, java_index, signature):
    count = len(signature) - len(signature.replace('[', '')) - 1
    args = map(str, python_method.pop_args(count))
    python_method.push(java_index, 'pava.multianewarray(%s)' % ','.join(args))


def convert_ifnull(python_method, java_index, java_target_index):
    if_label = python_method.add_if(java_index, java_target_index)
    python_method.push(java_index, 'if %s is not None: %s' % (python_method.pop(), if_label))


def convert_ifnonnull(python_method, java_index, java_target_index):
    if_label = python_method.add_if(java_index, java_target_index)
    python_method.push(java_index, 'if %s is None: %s' % (python_method.pop(), if_label))

##############


def convert_ifeq(python_method, java_index, java_target_index):
    handle_comparison(python_method, java_index, java_target_index, python_method.pop(), 0, '!=')


def convert_ifne(python_method, java_index, java_target_index):
    handle_comparison(python_method, java_index, java_target_index, python_method.pop(), 0, '==')


def convert_ifle(python_method, java_index, java_target_index):
    handle_comparison(python_method, java_index, java_target_index, python_method.pop(), 0, '>')


def convert_iflt(python_method, java_index, java_target_index):
    handle_comparison(python_method, java_index, java_target_index, python_method.pop(), 0, '>=')


def convert_ifge(python_method, java_index, java_target_index):
    handle_comparison(python_method, java_index, java_target_index, python_method.pop(), 0, '<')


def convert_ifgt(python_method, java_index, java_target_index):
    handle_comparison(python_method, java_index, java_target_index, python_method.pop(), 0, '<=')

##############

def convert_if_acmpeq(python_method, java_index, java_target_index):
    handle_comparison(python_method, java_index, java_target_index, python_method.pop(), python_method.pop(), '!=')


def convert_if_acmpne(python_method, java_index, java_target_index):
    handle_comparison(python_method, java_index, java_target_index, python_method.pop(), python_method.pop(), '==')


def convert_if_acmple(python_method, java_index, java_target_index):
    handle_comparison(python_method, java_index, java_target_index, python_method.pop(), python_method.pop(), '>')


def convert_if_acmplt(python_method, java_index, java_target_index):
    handle_comparison(python_method, java_index, java_target_index, python_method.pop(), python_method.pop(), '>=')


def convert_if_acmpge(python_method, java_index, java_target_index):
    handle_comparison(python_method, java_index, java_target_index, python_method.pop(), python_method.pop(), '<')


def convert_if_acmpgt(python_method, java_index, java_target_index):
    handle_comparison(python_method, java_index, java_target_index, python_method.pop(), python_method.pop(), '<=')

##############

def convert_if_icmpeq(python_method, java_index, java_target_index):
    handle_comparison(python_method, java_index, java_target_index, python_method.pop(), python_method.pop(), '!=')


def convert_if_icmpne(python_method, java_index, java_target_index):
    handle_comparison(python_method, java_index, java_target_index, python_method.pop(), python_method.pop(), '==')


def convert_if_icmple(python_method, java_index, java_target_index):
    handle_comparison(python_method, java_index, java_target_index, python_method.pop(), python_method.pop(), '>')


def convert_if_icmplt(python_method, java_index, java_target_index):
    handle_comparison(python_method, java_index, java_target_index, python_method.pop(), python_method.pop(), '>=')


def convert_if_icmpge(python_method, java_index, java_target_index):
    handle_comparison(python_method, java_index, java_target_index, python_method.pop(), python_method.pop(), '<')


def convert_if_icmpgt(python_method, java_index, java_target_index):
    handle_comparison(python_method, java_index, java_target_index, python_method.pop(), python_method.pop(), '<=')


##############

def handle_comparison(python_method, java_index, java_target_index, operand1, operand2, comparison_operator):
    if_label = python_method.add_if(java_index, java_target_index)
    python_method.push(java_index, 'if %s %s %s: %s' % (
        operand1, comparison_operator, operand2, if_label
    ), True)


def convert_lcmp(python_method, java_index):
    python_method.push(java_index, 'cmp(%s, %s)' % (python_method.pop(), python_method.pop()))


def convert_fcmpg(python_method, java_index):
    python_method.push(java_index, 'cmp(%s, %s)' % (python_method.pop(), python_method.pop()))


def convert_dcmpg(python_method, java_index):
    python_method.push(java_index, 'cmp(%s, %s)' % (python_method.pop(), python_method.pop()))


def convert_fcmpl(python_method, java_index):
    python_method.push(java_index, '-cmp(%s, %s)' % (python_method.pop(), python_method.pop()))


def convert_dcmpl(python_method, java_index):
    python_method.push(java_index, '-cmp(%s, %s)' % (python_method.pop(), python_method.pop()))


def convert_monitorenter(python_method, java_index):
    python_method.push(java_index, 'pava.monitorenter(%s)' % (python_method.pop()))


def convert_monitorexit(python_method, java_index):
    python_method.push(java_index, 'pava.monitorexit(%s)' % (python_method.pop()))


def java_local(code, index):
    if code.is_static:
        return 'a%d' % (index + 1)
    else:
        return 'self' if index == 0 else 'a%d' % index


class OpcodeMap(dict):
    def __missing__(self, key):
        raise NotImplementedError('Java bytecode not yet implemented: %s' % key)


module = sys.modules[__name__]
opcode_map = OpcodeMap((k[8:],getattr(module, k)) for k in dir(module) if k.startswith('convert_'))


def last_opcode(code):
    return code.co_code[-1]


def remove_last_opcode(code):
    code.co_code.pop()


RESERVED_WORDS = {
    'and', 'assert', 'break', 'class', 'continue',
    'def', 'del', 'elif', 'else', 'except',
    'exec', 'finally', 'for', 'from', 'global',
    'if', 'import', 'in', 'is', 'lambda',
    'not', 'or', 'pass', 'print', 'raise',
    'return', 'try', 'while',
    # some specific ones for pava
    'set', 'dict', 'with', 'yield'
}


def replace_reserved_names(name):
    if name in RESERVED_WORDS:
        return '__%s__' % name
    if name == '<init>': return '__init__'
    if name == '<clinit>': return '__clinit__'
    name = name.replace('$', '_')
    name = name.replace('-', '_')
    return name


def format_operands(operands):
    from javaruntime import MethodReference
    from javaruntime import FieldReference
    result = []
    for op in operands:
        if isinstance(op, MethodReference):
            result.append('%s.%s(%s)' % (op.class_name, op.method_name, ', '.join(op.args)))
        elif isinstance(op, FieldReference):
            result.append('%s.%s' % (op.class_name, op.field_name))
        else:
            result.append(str(op))
    return ' '.join(result)

def convert(java_opcode, python_method, java_index, *operands):
    python_method.java_bytecodes[java_index] = '%s %s' % (java_opcode, format_operands(operands))
    # handle_jumps(python_method, java_index)
    # code.pava_file.set_lineno(code)
    python_method.check_if(java_index)
    if DEBUG:
        print('        %s %s %s' % (str(java_index).rjust(4), opcode_map[java_opcode].__name__[8:], format_operands(operands)))
    opcode_map[java_opcode](python_method, java_index, *operands)
    # code.last_code_length = len(code.co_code)
    # code.stack_depth.append((len(code.co_code), code.get_stack_size()))




