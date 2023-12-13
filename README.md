# AiCore Project pinterest-data-pipeline

#### Project description
Build Pinterest's experimental data pipeline. Pinterest have billions of user interactions such as image uploads or image clicks 
which they need to process every day to inform the decisions to make. The project builds a system hosted in the cloud 
that ingests both batch and streaming events, and runs them through separate pipelines. The streaming pipeline will be 
used to compute real-time metrics (to recommend a profile in real-time), and the batch pipeline is used for computing 
metrics that depend on historical data.

#### Batch Data Pipeline Flow
Batch data (JSON payload) is sent via HTTP POST requests to an AWS API Gateway. The gateway routes the requests to a Kafka REST proxy, which
publishes them to the MSK Cluster. The MSK cluster writes the data to topics previously configured which are in a S3 bucket.
Databricks is configured to mount the S3 bucket. A databricks notebook runs daily as scheduled in MWAA Scheduler. The notebook 
reads the latest data and runs various queries against it.

![batch_flow](documentation%2Fprocess_flow%2Fbatch_flow.jpeg)

#### Streaming Data Pipeline Flow
Streaming data (JSON payload) is sent via HTTP PUT requests to an AWS API Gateway. The gateway routes the requests to Amazon Kinesis Data Streams.
A Databricks Notebook connects to the Kinesis Data Streams, reads, cleans and writes the streaming data to delta tables.

![streaming_flow](documentation%2Fprocess_flow%2Fstreaming_flow.jpeg)

#### Project aim
Put into practice concepts learnt about AWS, Kafka, Spark, Airflow and Databricks. Use python as the central
language across all applications.

For AWS, I configured: IAM roles, EC2 instances, S3 buckets, an MSK Cluster, API Gateways, a MWAA Scheduler and Kinesis Data Streams.
In Kafka, I created topics, used producers and consumers and configured a REST proxy.
Spark was hosted in Databricks. I used pyspark to extract, transform and load data.
For Airflow, I created a DAG to schedule a Databricks Notebook, ran and monitored the job.
I used Databricks to create Notebooks with python & pyspark commands.

#### Tech Stack
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-000?style=for-the-badge&logo=apachekafka)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-FDEE21?style=flat-square&logo=apachespark&logoColor=black)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

#### What I've learned
  - A pipeline consists of many independent parts, each which has to be configured, tested and implemented correctly.
  - Always check both the response code and the response text when sending requests.
  - The power of chaining in pyspark
  - Define your table schema, do not infer! 
  - If something seems difficult at first read the instructions a few times, try practicing the concept several times, find different sources to explain.
  - AWS is well named and documented.
  - This project is only the tip of the iceberg, lots left to still learn.

#### Description of files
| filename                           | description                                                                                                                 |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| 5_batch_user_posting_emulation.py  | Python file which runs the process to extract data from an AWS database and create HTTP POST messages for batch processing. |
| 6_batch_mount_S3_bucket.ipynb      | Databricks notebook for mounting an S3 bucket.                                                                              |
| 7_batch_read_clean_query.ipynb     | Databricks notebook with code to read, clean and query Pinterest batch data.                                                |
| 8_batch_0e36c8cd403d_dag.py        | Python file. Contains code for MWAA (AWS managed Airflow) to schedule a Databricks notebook run                             |
| 9_stream_read_clean_write.ipynb    | Databricks notebook with code to read and clean Pinterest stream data, and then write it to Delta Tables.                   |
| 9_stream_user_posting_emulation.py | Python file which runs the process to extract data from an AWS database and create HTTP PUT messages for stream processing. |
| README.md                          | Text file (markdown format) description of the project.                                                                     |
| config.py                          | Dataclasses and configuration for data extraction.                                                                          |
| extract.py                         | Classes used for data extraction.                                                                                           |
| utils/authenticate.ipynb           | Authentication.                                                                                                             |
| clean.py                           | Clean pin, user and geo data.                                                                                               |
| create_schema.py                   | Create schema for pin, user and geo before loading data.                                                                    |

#### Setup and Usage
The project was split into milestones. Work done for each of the milestones has been documented in the links below

[Milestone 3 Batch Processing: Configure the EC2 Kafka client](documentation%2F3%2Fmilestone3.md)

[Milestone 4 Batch Processing: Connect an MSK cluster to a S3 bucket](documentation%2F4%2Fmilestone4.md)

[Milestone 5 Batch Processing: Configuring an API in API Gateway](documentation%2F5%2Fmilestone5.md)

[Milestone 6 Batch Processing: Databricks](documentation%2F6%2Fmilestone6.md)

[Milestone 7 Batch Processing: Spark on Databricks](documentation%2F7%2Fmilestone7.md)

[Milestone 8 Batch Processing: AWS MWAA](documentation%2F8%2Fmilestone8.md)

[Milestone 9 Stream Processing: AWS Kinesis](documentation%2F9%2Fmilestone9.md)

#### Improvements I would make to the Pipelines
  - Automating AWS configuration using the boto library so all setup could be automated and tested
  - Splitting the streaming into 3 notebooks (one for Pin, User and Geo) and scheduling these to run in parallel would ensure consistent streaming data writes

#### License

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
