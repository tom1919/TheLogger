# TheLogger

Easy logging, timing and email notifications of code execution.

### Installation

```
$ pip install thelogger
```

### Logging

my_script.py:
```python class:"lineNo"
from thelogger import lg

# log messages
lg.info('Hello World')
lg.warning('warning message')
lg.error('error message')

# start logging messages to a file
lg.reset(file = './demo_log.txt')

# shorthand convenience methods for logging messages
lg.i('this is an info message')
lg.w('this is a warning message')

# remove log handlers
lg.close()
lg.i('nothing is logged because there are no log handlers')

# add default log handlers
lg.reset()
```

Output to Console:
```
[I 2021-11-13 08:50:36] Hello World
[W 2021-11-13 08:50:36] warning message
[E 2021-11-13 08:50:36] error message
[I 2021-11-13 08:50:36] this is an info message
[W 2021-11-13 08:50:36] this is a warning message
```

Output to demo_log.txt:
```
[I 2021-11-13 08:50:36 my_script:12] this is an info message
[W 2021-11-13 08:50:36 my_script:13] this is a warning message
```

### Email Notifications
```python class:"lineNo"
from thelogger import lg, notify

# decorate your func with @notify and pass in your email address 
@notify(email = 'my_email@gmail.com')
def concat_str(arg1, arg2=''):
    return f'{arg1} {arg2}'
# when concat_str is finished executing you will receive an email with the details
my_str = concat_str('hello', 'world')

# pass a logger object to log the function execution details
@notify(email = 'my_email@gmail.com', logger = lg)
def concat_str(arg1, arg2=''):
    return f'{arg1} {arg2}'
my_str = concat_str('hello', 'world')

# include a remote host address if your organization has gmail blocked
@notify(email = 'my_email@gmail.com', logger = lg, host = 'mail.abc.com')
def concat_str(arg1, arg2=''):
    return f'{arg1} {arg2}'
my_str = concat_str('hello', 'world')

# quick test to see if you're able to receive emails
notify('my_email@gmail.com', test = True)

# set the default arguments for the notify decorator
notify = notify(email = 'my_email@gmail.com', logger = lg, setdefault = True)
# now you can decorate functions w/o passing the args to @notify each time
@notify
def concat_str(arg1, arg2=''):
    return f'{arg1} {arg2}'
my_str = concat_str('hello', 'world')
```

Example Email:

![alt text](https://github.com/tom1919/TheLogger/blob/main/example_email.PNG)

### "Free" Logging of Scripts
Leverage TheLogger to easily log a program's execution details without typing out any log messages. See below example script and log file.

my_program.py:
```python class:"lineNo"
import numpy as np
import pandas as pd
from thelogger import notify, lg

lg = lg.reset(file = 'my_program.log')
notify = notify(setdefault=True, logger=lg)

@notify
def get_data(arg1):
    data = pd.DataFrame(np.random.randint(0,100,size=(10**7, 50)))
    return data

@notify
def wrangle_data(data):
    data2 = data.iloc[0:5,0:5] + 1
    return data2

@notify
def distribute_data(data2):
    print(data2)

@notify
def execute_program(program_name):
    data = get_data('my_arg')
    data2 = wrangle_data(data)
    distribute_data(data2)
    return 'success'

execute_program('my_program')
```

Output to my_program.log:
```
[I 2022-04-19 20:43:56 my_program:36] Starting: execute_program('my_program')...
[I 2022-04-19 20:43:56 my_program:31] Starting: data = get_data('my_arg')...
[I 2022-04-19 20:43:59 my_program:31] Finished: data = get_data('my_arg')...
[I 2022-04-19 20:44:00 my_program:31] Inputs and Output of get_data:
| Variable   | Type                          | Length   | String                                                      |
|------------|-------------------------------|----------|-------------------------------------------------------------|
| arg1       | 'str'                         | 6        | my_arg                                                      |
| output     | 'pandas.core.frame.DataFrame' | 10000000 | cols: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, ... |
Elapsed Time: 0:00:03.479504
[I 2022-04-19 20:44:00 my_program:32] Starting: data2 = wrangle_data(data)...
[I 2022-04-19 20:44:00 my_program:32] Finished: data2 = wrangle_data(data)...
[I 2022-04-19 20:44:00 my_program:32] Inputs and Output of wrangle_data:
| Variable   | Type                          | Length   | String                                                      |
|------------|-------------------------------|----------|-------------------------------------------------------------|
| data       | 'pandas.core.frame.DataFrame' | 10000000 | cols: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, ... |
| output     | 'pandas.core.frame.DataFrame' | 5        | cols: 0, 1, 2, 3, 4...                                      |
Elapsed Time: 0:00:00.000718
[I 2022-04-19 20:44:00 my_program:33] Starting: distribute_data(data2)...
[I 2022-04-19 20:44:00 my_program:33] Finished: distribute_data(data2)...
[I 2022-04-19 20:44:00 my_program:33] Inputs and Output of distribute_data:
| Variable   | Type                          | Length   | String                 |
|------------|-------------------------------|----------|------------------------|
| data2      | 'pandas.core.frame.DataFrame' | 5        | cols: 0, 1, 2, 3, 4... |
| output     | 'NoneType'                    | nan      | None                   |
Elapsed Time: 0:00:00.004332
[I 2022-04-19 20:44:00 my_program:36] Finished: execute_program('my_program')...
[I 2022-04-19 20:44:00 my_program:36] Inputs and Output of execute_program:
| Variable     | Type   | Length   | String     |
|--------------|--------|----------|------------|
| program_name | 'str'  | 10       | my_program |
| output       | 'str'  | 7        | success    |
Elapsed Time: 0:00:03.69315
```
