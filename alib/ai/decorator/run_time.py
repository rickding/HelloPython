import logging
import time

log = logging.getLogger(__name__)


# https://www.cnblogs.com/paranoia/p/6196859.html
def run_time(func):
    def run(*argv):
        start_time = time.clock()
        if argv:
            ret = func(*argv)
        else:
            ret = func()

        log.warning('%s used: %.1f seconds\n' % (func.__name__, time.clock() - start_time))
        return ret

    return run
