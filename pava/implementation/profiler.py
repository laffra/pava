import cProfile
import os
import pstats

PROFILE = False

def profile(cmd, global_context, local_context, top_line_count=30):
    if PROFILE:
        name = 'pava_stats'
        cProfile.runctx(cmd, global_context, local_context, name)
        pstats.Stats(name).sort_stats('cumulative').print_stats(top_line_count)
        os.remove(name)
    else:
        exec(cmd, global_context, local_context)
