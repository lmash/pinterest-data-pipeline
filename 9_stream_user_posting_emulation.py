from config import streams_data_point_types, streams_endpoint_url, streams_header
from extract import StreamExtractor


def run_infinite_post_data_loop():
    """This function runs until it's manually stopped."""
    extractor = StreamExtractor(
        endpoint_url=streams_endpoint_url,
        headers=streams_header,
        data_point_types=streams_data_point_types,
    )

    while True:
        extractor.create_engine()
        extractor.run()


if __name__ == "__main__":
    run_infinite_post_data_loop()
