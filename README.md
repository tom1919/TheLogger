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

# quick test to see if your able to receive emails
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
