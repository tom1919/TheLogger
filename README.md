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

Output to console:
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

my_script.py:
```python class:"lineNo"
from thelogger import lg, notify

# decorate your func with @notify to receive an email when it's done executing
@notify(email = 'py.notify1@gmail.com')
def concat_str(arg1, arg2=''):
    return f'{arg1} {arg2}'
# the execution details of concat_str will be in the email
my_str = concat_str('hello', 'world')

# pass a logger object to log the function execution details
@notify(email = 'py.notify1@gmail.com', logger = lg)
def concat_str(arg1, arg2=''):
    return f'{arg1} {arg2}'
my_str = concat_str('hello', 'world')

# include a remote host address if your organization has gmail blocked
@notify(email = 'py.notify1@gmail.com', logger = lg, host = 'mail.abc.com')
def concat_str(arg1, arg2=''):
    return f'{arg1} {arg2}'
my_str = concat_str('hello', 'world')

# quick test to see if your able to receive emails
notify('py.notify1@gmail.com', test = True)

# set the default arguments for the notify decorator
notify = notify(email = 'py.notify1@gmail.com', logger = lg, setdefault = True)
# now you can decorate functions w/o passing the args to @notify each time
@notify
def concat_str(arg1, arg2=''):
    return f'{arg1} {arg2}'
my_str = concat_str('hello', 'world')
```

### Example Email
