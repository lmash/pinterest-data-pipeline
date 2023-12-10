from abc import ABC, abstractmethod
import datetime
import json
import random
import requests
from time import sleep
from typing import List, Dict

import sqlalchemy

random.seed(100)


class Extractor(ABC):
    """
    This class enables Batch or Streaming data extraction
    Example usage:

    extractor = BatchExtractor(
        endpoint_url=<batch_endpoint_url>,
        headers=<batch_headers>,
        data_point_types=<batch_data_point_types>,
    )

    while True:
        extractor.create_engine()
        extractor.run()

    """

    def __init__(
        self,
        endpoint_url: str,
        headers: Dict,
        data_point_types: List,
    ):
        self.endpoint_url = endpoint_url
        self.headers = headers
        self.data_point_types = (
            data_point_types  # BatchDataPointType or StreamDataPointType
        )
        self.connector = AWSDBConnector()
        self.engine = None
        self.random_row = None

    def create_engine(self):
        """
        Create a database connection to an AWS database. Includes a variable sleep and the selection of a
        random row to be requested.
        """
        sleep(random.randrange(0, 2))
        self.random_row = random.randint(0, 11000)
        self.engine = self.connector.create_db_connector()

    @abstractmethod
    def _get_payload(self, result, data_point) -> str:
        """
        To override
        Create a JSON payload
        """
        pass

    @abstractmethod
    def _get_response(self, data_point, payload) -> requests.Response:
        """
        To override
        Send a payload an AWS API Gateway
        """
        pass

    def run(self):
        """Connect to the database, run the SELECT statement, send the payload and print the response"""
        with self.engine.connect() as connection:
            for data_point in self.data_point_types:
                select_statement = sqlalchemy.text(
                    f"SELECT * FROM {data_point.table_name} LIMIT {self.random_row}, 1"
                )
                selected_row = connection.execute(select_statement)

                for row in selected_row:
                    result = dict(row._mapping)

                payload = self._get_payload(result=result, data_point=data_point)
                response = self._get_response(data_point=data_point, payload=payload)

                print(
                    f"Status code: {response.status_code} Response text: {response.text}\n"
                    f"for payload: {payload}"
                )


class BatchExtractor(Extractor):
    """Subclass for batch data extraction"""

    def _get_payload(self, result, data_point) -> str:
        return json.dumps({"records": [{"value": result}]}, cls=DateTimeEncoder)

    def _get_response(self, data_point, payload) -> requests.Response:
        return requests.request(
            "POST", data_point.invoke_url, headers=self.headers, data=payload
        )


class StreamExtractor(Extractor):
    """Subclass for streaming data extraction"""

    def _get_payload(self, result, data_point) -> str:
        return json.dumps(
            {
                "StreamName": data_point.stream_name,
                "Data": result,
                "PartitionKey": data_point.partition_key,
            },
            cls=DateTimeEncoder,
        )

    def _get_response(self, data_point, payload) -> requests.Response:
        invoke_url = f"{self.endpoint_url}{data_point.stream_name}/record"
        return requests.request("PUT", invoke_url, headers=self.headers, data=payload)


class AWSDBConnector:
    """A class to connect to an AWS hosted database"""

    def __init__(self):
        self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
        self.USER = "project_user"
        self.PASSWORD = ":t%;yCY3Yjg"
        self.DATABASE = "pinterest_data"
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
