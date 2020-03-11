class LoggingClient():
    import os
    import google.cloud.logging
    from google.cloud.logging.resource import Resource
    from enum import IntEnum

    logging_client = google.cloud.logging.Client()
    resource = None
    logger = None
    log_level = 'DEBUG'

    def __init__(self, project=None, function_name=None, region=None):
        if project is None:
            project = self.os.environ.get('GCP_PROJECT')
        if function_name is None:
            function_name = self.os.environ.get('FUNCTION_NAME')
        if region is None:
            region = self.os.environ.get('FUNCTION_REGION')

        log_name = 'cloudfunctions.googleapis.com%2Fcloud-functions'
        self.logger = self.logging_client.logger(log_name.format(project))
        self.resource = self.Resource(type="cloud_function", labels={"function_name": function_name, "region": region})
        self.setLogLevel('DEBUG')

    def all(self, message):
        self.createLog(message)

    def debug(self, message):
        self.createLog(message, 'DEBUG')
    
    def info(self, message):
        self.createLog(message, 'INFO')

    def warning(self, message):
        self.createLog(message, 'WARNING')

    def error(self, message):
        self.createLog(message, 'ERROR')

    def critical(self, message):
        self.createLog(message, 'CRITICAL')

    def createLog(self, message, severity=None):
        if self.checkLevel(severity):
            if isinstance(message, dict):
                self.logger.log_struct(message, resource=self.resource, severity=severity)
            else:
                self.logger.log_struct({'message': message}, resource=self.resource, severity=severity)

    def setLogLevel(self, level):
        if level in self.Severity.__members__:
            self.log_level = self.Severity[level]
        else:
            raise self.LogLevelError('The Log Level of \'{}\' does not exist.'.format(level))

    def checkLevel(self, severity):
        return self.Severity[severity] >= self.log_level or self.Severity[severity] == 0

    class Severity(IntEnum):
        ALL = 0
        DEBUG = 100
        INFO = 200
        WARNING = 400
        ERROR = 500
        CRITICAL = 600

    class LogLevelError(Exception):
        pass