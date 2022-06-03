# My favorite references bookmarks
https://realpython.com/ <br/>
https://github.com/wilfredinni/python-cheatsheet <br/>

# Context Manager 
https://rednafi.github.io/digressions/python/2020/03/26/python-contextmanager.html <br/>

Code snippet: <> <br/>

# Switch case in python - equivalent

```
>>> def south(): return "South"
... 
>>> def west(): return "west"
... 
>>> switch_case = { 1:south, 2:west}
>>> switch_case[1]
<function south at 0x7eff8812dee0>
>>> switch_case[1]()
'South'
>>> switch_case[2]()
```

# get UTC time
```
now = datetime.datetime.now(timezone.utc)
timestamp = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
```
ref: https://www.geeksforgeeks.org/get-utc-timestamp-in-python/ <br>

# Logging
```
import logging

logger = logging.getLogger(__name__)
c_handler = logging.StreamHandler()
c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
logger.addHandler(c_handler)

logger.setLevel(logging.DEBUG)
```
ref: https://realpython.com/python-logging/ <br>


# args and kwargs
```
https://www.geeksforgeeks.org/args-kwargs-python/

def myFun(*args,**kwargs):
	print("args: ", args)
	print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")

```

# decorators

ref: https://realpython.com/primer-on-python-decorators/ <br>
```
#!/usr/bin/env python3
import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    print(f'n: {num_times}')
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(10)
```
