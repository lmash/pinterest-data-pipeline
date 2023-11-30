import json
import requests
import random
from sqlalchemy import text
from time import sleep

from extract import AWSDBConnector, StreamDataPointType, DateTimeEncoder

random.seed(100)
new_connector = AWSDBConnector()
HEADERS = {'Content-Type': 'application/json'}


def run_infinite_post_data_loop():
    data_point_types = [
        StreamDataPointType(
            table_name='geolocation_data',
            stream_name='streaming-0e36c8cd403d-geo',
            partition_key='ind'
        ),
        StreamDataPointType(
            table_name='pinterest_data',
            stream_name='streaming-0e36c8cd403d-pin',
            partition_key='index'
        ),
        StreamDataPointType(
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
                invoke_url = f"https://jydbc247f4.execute-api.us-east-1.amazonaws.com/Prod/streams/" \
                             f"{data_point.stream_name}/record"

                select_statement = text(f"SELECT * FROM {data_point.table_name} LIMIT {random_row}, 1")
                selected_row = connection.execute(select_statement)

                for row in selected_row:
                    result = dict(row._mapping)

                payload = json.dumps({"StreamName": data_point.stream_name,
                                      "Data": result,
                                      "PartitionKey": data_point.partition_key,
                                      }, cls=DateTimeEncoder)

                response = requests.request("PUT", invoke_url, headers=HEADERS, data=payload)
                print(f"Status code: {response.status_code} Response text: {response.text}\n"
                      f"for payload: {payload}")


if __name__ == "__main__":
    run_infinite_post_data_loop()
