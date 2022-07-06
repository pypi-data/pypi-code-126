from creativiousUtilities.logging import Logger

logger = Logger(name="testLogger", subname="core", logfile="MainLogger.log", logAllFile="loggingAll.log").getLogger()

logger.error("AHH AN ERROR")
logger.info("this is info")