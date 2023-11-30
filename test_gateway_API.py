"""
Tests to verify the Kinesis API Gateway is properly configured
"""
import json
import requests

HEADERS = {'Content-Type': 'application/json'}


def test_stream_get_post():
    """Test streams/stream-name GET gateway API"""
    invoke_url = "https://jydbc247f4.execute-api.us-east-1.amazonaws.com/Prod/streams/1/"
    payload = json.dumps({"StreamName": "1"})

    response = requests.request("GET", invoke_url, headers=HEADERS, data=payload)
    assert response.status_code == 200


def test_stream_post():
    """Test streams/stream-name POST gateway API"""
    invoke_url = "https://jydbc247f4.execute-api.us-east-1.amazonaws.com/Prod/streams/test-stream/"
    payload = json.dumps({"StreamName": "test-stream", "ShardCount": 2})

    response = requests.request("POST", invoke_url, headers=HEADERS, data=payload)
    assert response.status_code == 200


def test_stream_delete():
    """Test streams/stream-name DELETE gateway API"""
    invoke_url = "https://jydbc247f4.execute-api.us-east-1.amazonaws.com/Prod/streams/test-stream/"
    payload = json.dumps({"StreamName": "test-stream"})

    response = requests.request("DELETE", invoke_url, headers=HEADERS, data=payload)
    assert response.status_code == 200


def test_record_api():
    """Test streams/stream-name/record gateway API"""
    example_df = {"index": 1, "name": "Maya", "age": 25, "role": "engineer"}
    invoke_url = "https://jydbc247f4.execute-api.us-east-1.amazonaws.com/Prod/streams/test-stream/record"

    payload = json.dumps({"StreamName": "test-stream",
                          "Data": example_df,
                          "PartitionKey": "desired-name"
                          })

    response = requests.request("PUT", invoke_url, headers=HEADERS, data=payload)
    assert response.status_code == 200


def test_records_api():
    """Test streams/stream-name/records gateway API"""
    example_df = {"index": 1, "name": "Maya", "age": 25, "role": "engineer"}
    invoke_url = "https://jydbc247f4.execute-api.us-east-1.amazonaws.com/Prod/streams/test-stream/records"

    payload = json.dumps({"StreamName": "test-stream",
                          "Records": [
                              {"Data": example_df,
                               "PartitionKey": "P1"},
                              {"Data": example_df,
                               "PartitionKey": "P1"},
                          ]})

    response = requests.request("PUT", invoke_url, headers=HEADERS, data=payload)
    assert response.status_code == 200
