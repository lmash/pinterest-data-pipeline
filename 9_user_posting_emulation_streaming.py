from dataclasses import dataclass
import datetime
import json
import requests
import random
import sqlalchemy
from sqlalchemy import text
from time import sleep


random.seed(100)
HEADERS = {'Content-Type': 'application/json'}


class AWSDBConnector:

    def __init__(self):

        self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
        self.USER = 'project_user'
        self.PASSWORD = ':t%;yCY3Yjg'
        self.DATABASE = 'pinterest_data'
        self.PORT = 3306
        
    def create_db_connector(self):
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
        return engine


new_connector = AWSDBConnector()


class DateTimeEncoder(json.JSONEncoder):
    """
    A custom class to serialize datetime objects, overrides the default method
    https://pynative.com/python-serialize-datetime-into-json/
    """
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


@dataclass
class DataPointType:
    table_name: str
    stream_name: str
    partition_key: str


def run_infinite_post_data_loop():
    invoke_url = "https://jydbc247f4.execute-api.us-east-1.amazonaws.com/Prod/streams/<stream_name>/record"

    data_point_types = [
        DataPointType(
            table_name='geolocation_data',
            stream_name='streaming-0e36c8cd403d-geo',
            partition_key='ind'
        ),
        DataPointType(
            table_name='pinterest_data',
            stream_name='streaming-0e36c8cd403d-pin',
            partition_key='index'
        ),
        DataPointType(
            table_name='user_data',
            stream_name='streaming-0e36c8cd403d-user',
            partition_key='ind'
        )
    ]

    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:

            for data_point in data_point_types:
                select_statement = text(f"SELECT * FROM {data_point.table_name} LIMIT {random_row}, 1")
                selected_row = connection.execute(select_statement)

                for row in selected_row:
                    result = dict(row._mapping)

                payload = json.dumps({"StreamName": data_point.stream_name,
                                      "Data": result,
                                      "PartitionKey": data_point.partition_key
                                      }, cls=DateTimeEncoder)

                requests.request("PUT", invoke_url, headers=HEADERS, data=payload)


if __name__ == "__main__":
    run_infinite_post_data_loop()
