# gcp-python-logging
## A python module for the handy printing of logs to StackDriver based on severity from within a Google Cloud Function

After running into an issue with Python logging not logging to the correct StackDriver severity filter, I created this helper module in order to facilitate that function. It replicates much of the logging functionality, but translated into StackDriver levels.

---

## Severity Levels
| Severity | Int Level |
| -------- | --------- |
| ALL | 0 |
| DEBUG | 100 |
| INFO | 200 |
| WARNING | 400 |
| ERROR | 500 |
| CRITICAL | 600 |
for all severity levels except `ALL`, only logs of that log level or higher will be printed out (ex: Log Level of `WARNING` only prints out `WARNING`, `ERROR`, and `CRITICAL`). If the `ALL` log level is written, it will appear in all cases.

---
## Setup the Module
This module can be used simply by doing: `pip install gcp-python-logging`

This module can then be imported and initialized as such:
```
from gcp_python_logging import LoggingClient

logger = LoggingClient()
```
Passing no arguments will use the environment variables available to grab the project, function name, and function region. However you can also pass those variables into the client in order to change where these logs will be sent.

---
## Creating a Log
In order to create a new log, simply use a similar syntax to Python logger.
```
logger.debug('This is a debug statement')
logger.error('Something went wrong!')
```

---
## Changing Log Level
By default, this module sets the LogLevel to `DEBUG`, but this can be changed by running the command:
```
logger.setLogLevel('ERROR')
```
Then only logs at level `ERROR` or higher will be reported.

---

### Author's Note:
This currently prints out all logs in a JsonPayload in order to meet the needs of my project. If users would prefer the ability to choose the printout type please feel free to reach out to me.