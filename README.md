# TheLogger

Easy to use logger object for creating code logs. Just import it and it's set up and ready to go.

### Installation

```
$ pip install icecream
```

### Usage

```python
from thelogger import lg

# log messages
lg.info('Hello World')
lg.warning('warning message')
lg.error('error message')

# start logging messages to a file
lg.reset(file = './demo_log.log')

# shorthand convience methods for logging messages
lg.d('this is a debug message')
lg.i('this is an info message')

# remove log handlers
lg.close()

# add default log handlers
lg.reset()
```

Output to console:

```
console output
```

Output to file:

```
file output
```
