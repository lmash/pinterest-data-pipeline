from dataclasses import dataclass


@dataclass
class BatchDataPointType:
    invoke_url: str
    table_name: str


topics_endpoint_url = "https://jydbc247f4.execute-api.us-east-1.amazonaws.com/Prod/topics/0e36c8cd403d"
batch_headers = {"Content-Type": "application/vnd.kafka.json.v2+json"}

batch_data_point_types = [
    BatchDataPointType(
        invoke_url=f"{topics_endpoint_url}.pin", table_name="pinterest_data"
    ),
    BatchDataPointType(
        invoke_url=f"{topics_endpoint_url}.geo", table_name="geolocation_data"
    ),
    BatchDataPointType(
        invoke_url=f"{topics_endpoint_url}.user", table_name="user_data"
    ),
]


@dataclass
class StreamDataPointType:
    table_name: str
    stream_name: str
    partition_key: str


streams_endpoint_url = f"https://jydbc247f4.execute-api.us-east-1.amazonaws.com/Prod/streams/"
streams_header = {'Content-Type': 'application/json'}

streams_data_point_types = [
    StreamDataPointType(table_name='geolocation_data',
                        stream_name='streaming-0e36c8cd403d-geo',
                        partition_key='ind'),
    StreamDataPointType(table_name='pinterest_data',
                        stream_name='streaming-0e36c8cd403d-pin',
                        partition_key='index'),
    StreamDataPointType(table_name='user_data',
                        stream_name='streaming-0e36c8cd403d-user',
                        partition_key='ind')
]
