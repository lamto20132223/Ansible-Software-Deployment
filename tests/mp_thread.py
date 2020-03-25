
from multiprocessing.pool import ThreadPool

import time

def foo(bar, baz):
    print 'hello {0}'.format(bar)
    time.sleep(10)
    return 'foo' + baz

pool = ThreadPool(processes=1)

async_result = pool.apply_async(foo, ('world', 'foo')) # tuple of args for foo

# do some other stuff in the main process

print("lamtv10")

return_val = async_result.get()  # get the return value from your function.
print(return_val)

lamtv10="lamtv10"
print(lamtv10)

print(lamtv10+ return_val)