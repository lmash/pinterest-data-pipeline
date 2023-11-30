import json
import requests
import random
from sqlalchemy import text
from time import sleep

from extract import AWSDBConnector, BatchDataPointType, DateTimeEncoder

random.seed(100)
new_connector = AWSDBConnector()


def run_infinite_post_data_loop():
    topics_endpoint_url = 'https://jydbc247f4.execute-api.us-east-1.amazonaws.com/Prod/topics/0e36c8cd403d'

    data_point_types = [
        BatchDataPointType(invoke_url=f'{topics_endpoint_url}.pin', table_name='pinterest_data'),
        BatchDataPointType(invoke_url=f'{topics_endpoint_url}.geo', table_name='geolocation_data'),
        BatchDataPointType(invoke_url=f'{topics_endpoint_url}.user', table_name='user_data')
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

                payload = json.dumps({
                    "records": [{"value": result}]
                }, cls=DateTimeEncoder)

                headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
                response = requests.request("POST", data_point.invoke_url, headers=headers, data=payload)

                print(f"Status code: {response.status_code} Response text: {response.text}\n"
                      f"for payload: {payload}")


if __name__ == "__main__":
    run_infinite_post_data_loop()
