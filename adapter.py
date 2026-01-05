class ExternalLogger:
    def log_message(self, msg):
        print(f"External log: {msg}")

class Logger:
    def log(self, message):
        pass

class LoggerAdapter(Logger):
    def __init__(self, external_logger):
        self.external_logger = external_logger

    def log(self, message):
        self.external_logger.log_message(message)

if __name__ == "__main__":
    external_logger = ExternalLogger()
    logger = LoggerAdapter(external_logger)
    logger.log("This is a test message.")
