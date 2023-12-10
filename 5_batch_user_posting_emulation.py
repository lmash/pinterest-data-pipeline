from config import batch_data_point_types, topics_endpoint_url, batch_headers
from extract import BatchExtractor


def run_infinite_post_data_loop():
    """This function runs until it's manually stopped."""
    extractor = BatchExtractor(
        endpoint_url=topics_endpoint_url,
        headers=batch_headers,
        data_point_types=batch_data_point_types,
    )

    while True:
        extractor.create_engine()
        extractor.run()


if __name__ == "__main__":
    run_infinite_post_data_loop()
