from dataclasses import dataclass
import datetime
import json
import sqlalchemy


class AWSDBConnector:
    """A class to connect to an AWS hosted database"""

    def __init__(self):
        self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
        self.USER = 'project_user'
        self.PASSWORD = ':t%;yCY3Yjg'
        self.DATABASE = 'pinterest_data'
        self.PORT = 3306

    def create_db_connector(self):
        engine = sqlalchemy.create_engine(
            f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4"
        )
        return engine


class DateTimeEncoder(json.JSONEncoder):
    """
    A custom class to serialize datetime objects, overrides the default method
    https://pynative.com/python-serialize-datetime-into-json/
    """

    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


@dataclass
class BatchDataPointType:
    invoke_url: str
    table_name: str


@dataclass
class StreamDataPointType:
    table_name: str
    stream_name: str
    partition_key: str
