# https://www.machinelearningplus.com/python/python-logging-guide/

import logging

# Basic configuration
logging.basicConfig(level=logging.INFO)

def hypotenuse(a, b):
    """Compute the hypotenuse"""
    return (a**2 + b**2)**0.5
a = 1
b = 2
logging.info("Hypotenuse of {a}, {b} is {c}".format(a=3, b=4, c=hypotenuse(a,b)))
# logging.{level}(message)

# The printed log message has the following default format: {LEVEL}:{LOGGER}:{MESSAGE}.

# The logger is called root, because that is the default logger.
# A logger is like an entity you can create and configure to log different type and format of messages.

# You can configure a logger that prints to the console and another logger that sends the logs to a file,
# has a different logging level and is specific to a given module.




# The 5 levels of logging
# Logging has 5 different hierarchical levels of logs that a given logger may be configured to.
# Let’s see what the python docs has to say about each level:
# - DEBUG: Detailed information, for diagnosing problems. Value=10.
# - INFO: Confirm things are working as expected. Value=20.
# - WARNING: Something unexpected happened, or indicative of some problem. But the software is still working as expected. Value=30.
# - ERROR: More serious problem, the software is not able to perform some function. Value=40
# - CRITICAL: A serious error, the program itself may be unable to continue running. Value=50




# How to log to a file instead of the console

# To send the log messages to a file from the root logger, you need to set the file argument in logging.basicConfig()
import logging
logging.basicConfig(level=logging.INFO, file='sample.log')




# How to change the logging format

# https://www.machinelearningplus.com/python/python-logging-guide/
logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')




# Why working with the root logger for all modules isn’t the best idea

# Because they all will share the same ‘root’ logger.
# But why is that bad?
# Let’s look at the below code:

# 1. code inside myprojectmodule.py
import logging
logging.basicConfig(file='module.log')
#-----------------------------
# 2. code inside main.py (imports the code from myprojectmodule.py)
import logging
import myprojectmodule  # This runs the code in myprojectmodule.py
logging.basicConfig(file='main.log')  # No effect, because!

# Imagine you have one or more modules in your project. And these modules use the basic root module. Then, when importing
# the module (‘myprojectmodule.py‘), all of that module’s code will run and logger gets configured.
# Once configured, the root logger in the main file (that imported the ‘myprojectmodule‘ module) will no longer be able
# to change the root logger settings. Because, the logging.basicConfig() once set cannot be changed.
# That means, if you want to log the messages from myprojectmodule to one file and the logs from the main module in another file, root logger can’t that.
# To do that you need to create a new logger.




# How to create a new logger?

# You can create a new logger using the ‘logger.getLogger(name)‘ method. If a logger with the same name exists, then that logger will be used.
# While you can give pretty much any name to the logger, the convention is to use the __name__ variable like this:
logger = logging.getLogger(__name__)
logger.info('my logging message')
# But, why use __name__ as the name of the logger, instead of hardcoding a name?
# Because the __name__ variable will hold the name of the module (python file) that called the code.
# So, when used inside a module, it will create a logger bearing the value provided by the module’s __name__ attribute.
# Now, once you’ve created a new logger, you should remember to log all your messages using the new logger.info()
# instead of the root’s logging.info() method.

# Another aspect to note is, all the loggers have a built-in hierarchy to it.
# What do I mean by that?
# For example, if you have configured the root logger to log messages to a particular file.
# You also have a custom logger for which you have not configured the file handler to send messages to console or another log file.
# In this case, the custom logger will fallback and write to the file set by the root logger itself.
# Until and unless you configure the log file of your custom logger.
# So what is a file handler and how to set one up?




# What is and How to set up a File Handler and Formatter?

# The FileHandler() and Formatter() classes are used to setup the output file and the format of messages for loggers other than the root logger.

# In the root logger we setup the filename and the format of the message just by specifying the filename and format parameters
# in logging.basicConfig() and all subsequent logs went to that file.

# However, when you create a separate logger, you need to set them up individually using the logging.FileHandler() and logging.Formatter() objects.
# A FileHandler is used to make your custom logger to log in to a different file.
# Likewise, a Formatter is used to change the format of your logged messages.

import logging
# Gets or creates a logger
logger = logging.getLogger(__name__)
# set log level
logger.setLevel(logging.WARNING)
# define file handler and set formatter
file_handler = logging.FileHandler('logfile.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
# add file handler to logger
logger.addHandler(file_handler)
# Logs
logger.debug('A debug message')
logger.info('An info message')
logger.warning('Something is not right.')
logger.error('A Major error has happened.')
logger.critical('Fatal error. Cannot continue')




# How to include traceback information in logged messages

# Besides ‘debug‘, ‘info‘, ‘warning‘, ‘error‘, and ‘critical‘ messages, you can log exceptions that will include any associated traceback information.
# logger.exception will log the message provided in its arguments as well as the error message traceback info.
# Below is a nice example.

import logging
# Create or get the logger
logger = logging.getLogger(__name__)
# set log level
logger.setLevel(logging.INFO)
def divide(x, y):
    try:
        out = x / y
    except ZeroDivisionError:
        logger.exception("Division by zero problem")
    else:
        return out
# Logs
logger.error("Divide {x} / {y} = {c}".format(x=10, y=0, c=divide(10,0)))
#> ERROR:__main__:Division by zero problem
#> Traceback (most recent call last):
#>   File "<ipython-input-16-a010a44fdc0a>", line 12, in divide
#>     out = x / y
#> ZeroDivisionError: division by zero
#> ERROR:__main__:None











# https://realpython.com/python-logging/


# The corresponding methods for each level can be called as shown in the following example:
import logging
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
# logging.critical('This is a critical message')
# WARNING:root:This is a warning message
# ERROR:root:This is an error message
# CRITICAL:root:This is a critical message

# The output shows the severity level before each message along with root,
# which is the name the logging module gives to its default logger.
# Notice that the debug() and info() messages didn’t get logged. This is because, by default,
# the logging module logs the messages with a severity level of WARNING or above.




# Basic Configurations

# Some of the commonly used parameters for basicConfig() are the following:
# level: The root logger will be set to the specified severity level.
# filename: This specifies the file.
# filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
# format: This is the format of the log message.


logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# More parameters for basicConfig() -> https://docs.python.org/3/library/logging.html#logging.basicConfig

# Note that basicConfig() can only be called once.
# debug(), info(), warning(), error(), and critical() also call basicConfig() without arguments automatically
# if it has not been called before. This means that after the first time one of the above functions is called,
# you can no longer configure the root logger because they would have called the basicConfig() function internally.




# Formatting the Output

# Examples:
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


# The entire list of available attributes to format the output can be found here -> https://docs.python.org/3/library/logging.html#logrecord-attributes


# Capturing Stack Traces

# logging.exception()
# Note that logging.exception() should only be called from an exception handler (except ...)
import logging
a = 5
b = 0
try:
  c = a / b
except Exception as e:
  logging.error("Exception occurred", exc_info=True)
# ERROR:root:Exception occurred
# Traceback (most recent call last):
#   File "exceptions.py", line 6, in <module>
#     c = a / b
# ZeroDivisionError: division by zero
# [Finished in 0.2s]




# Classes and Functions
# The most commonly used classes defined in the logging module are the following:
# - Logger: This is the class whose objects will be used in the application code directly to call the functions.
# - LogRecord: Loggers automatically create LogRecord objects that have all the information related to the event
#   being logged, like the name of the logger, the function, the line number, the message, and more.
# - Handler: Handlers send the LogRecord to the required output destination, like the console or a file.
#   Handler is a base for subclasses like StreamHandler, FileHandler, SMTPHandler, HTTPHandler, and more. These subclasses send the logging outputs to corresponding destinations, like sys.stdout or a disk file.
# - Formatter: This is where you specify the format of the output by specifying a string format that lists out
#   the attributes that the output should contain.

# Unlike the root logger, a custom logger can’t be configured using basicConfig(). You have to configure it using
# if Handlers and Formatters.
# A logger that you create can have more than one handler, which means you can set it up to be saved to
# a log file and also send it over email.
# Like loggers, you can also set the severity level in handlers. This is useful if you want to set multiple handlers
# for the same logger but want different severity levels for each of them. For example, you may want logs with level
# WARNING and above to be logged to the console, but everything with level ERROR and above should also be saved to a file.

# Example:
# logging_example.py
import logging
# Create a custom logger
logger = logging.getLogger(__name__)
# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)
# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)
# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)
logger.warning('This is a warning')
logger.error('This is an error')

# c_handler is a StreamHandler with level WARNING and takes the info from the LogRecord to generate an output
# in the format specified and prints it to the console. f_handler is a FileHandler with level ERROR, and it
# ignores this LogRecord as its level is WARNING.




# Other Configuration Methods -> https://realpython.com/python-logging/






# Dodatkowe podsumowanie:

# Możemy stworzyć root logger bądź inne loggery.
# Stworzenie root loggera:
# a)
logger = logging.getLogger()
# b)
logging.basicConfig() # stworzenie root loggera i dodanie do niego StreamHandler (printuje logi na konsolę)
# Stworzenie innego loggera
# a)
logger = logging.getLogger(__name__) # rekomendowany sposob, ale uwaga na name hierarchy
# b)
logger = logging.getLogger('my_new_logger')