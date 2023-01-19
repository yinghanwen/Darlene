import sys
from pathlib import Path
from datetime import datetime, timedelta
from loguru import logger
from nonebot.log import logger_id   

logger.remove(logger_id)

LOG_PATH = Path(".") / "cache" / "logs"
LOG_PATH.mkdir(exist_ok=True, parents=True)


log_format: str = (
    "<g>{time:MM-DD HH:mm:ss}</g> "
    "[<lvl>{level}</lvl>] "
    "<c><u>{name}</u></c> | "
    "{message}"
)






class LoguruNameDealer:
    def __call__(self, record):
        log_handle = record["name"]
        
        if "nonebot_plugin_gocqhttp" in log_handle:
            plugin_name = log_handle.split("_")[-1]
            record["name"] = "gocqhttp"
        else:
            record["name"] = record["name"].split(".")[0]

        return record


logger.add(
    LOG_PATH / f'{datetime.now().date()}.log',
    level='INFO',
    rotation='00:00',
    format=log_format,
    retention=timedelta(days=30)
)

logger.add(
    LOG_PATH / f'debug_{datetime.now().date()}.log',
    level='DEBUG',
    rotation='00:00',
    format=log_format,
    retention=timedelta(days=30)
)

logger.add(
    LOG_PATH / f'warning_{datetime.now().date()}.log',
    level='WARNING',
    rotation='00:00',
    format=log_format,
    retention=timedelta(days=30)
)

logger.add(
    LOG_PATH / f'error_{datetime.now().date()}.log',
    level='ERROR',
    rotation='00:00',
    format=log_format,
    retention=timedelta(days=30)
)

