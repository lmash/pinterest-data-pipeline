# AiCore Project pinterest-data-pipeline

#### Project description
Replicate Pinterest's experimental data pipeline. Pinterest have billions of user interactions such as image uploads or image clicks 
which they need to process every day to inform the decisions to make. The project builds a system hosted in the cloud 
that ingests both batch and streaming events, and runs them through separate pipelines. The streaming pipeline will be 
used to compute real-time metrics (to recommend a profile in real-time), and the batch pipeline is used for computing 
metrics that depend on historical data.

#### Tech Stack
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-000?style=for-the-badge&logo=apachekafka)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-FDEE21?style=flat-square&logo=apachespark&logoColor=black)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

#### Pipeline Flows
![batch_arch.jpeg](documentation%2Fprocess_flow%2Fbatch_arch.jpeg)
![streaming_arch.jpeg](documentation%2Fprocess_flow%2Fstreaming_arch.jpeg)

#### Project aim
Put into practice concepts learnt about AWS, Kafka, Spark, Airflow and Databricks. Use python as the central
language across all applications.

For AWS we configured: IAM roles, EC2 instances, S3 buckets, a MSK Cluster, API Gateways and a MWAA Scheduler.
In Kafka we created topics, used producers and consumers and configured a REST proxy.
Spark was hosted in Databricks. We used pyspark to extract, clean and load data.
For Airflow we created a DAG to schedule a Databricks Notebook, we ran and monitored the job.
We used Databricks to create Notebooks with python & pyspark commands.

#### What I've learned
  - A pipeline consists of many independent parts, each which has to be configured, tested and implemented correctly.
  - Always check both the response code and the response text when sending requests.
  - The power of chaining in pyspark
  - If something seems difficult at first read the instructions a few times, try practicing the concept several times, find different sources to explain.

#### Description of files
| filename                              | description                                                                                               |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------|
| 5_user_posting_emulation.py           | Python file which extracts data from an AWS database and creates HTTP POST messages for batch processing. |
| 6_mount_S3_bucket.ipynb               | Databricks notebook for mounting an S3 bucket.                                                            |
| 7_batch_read_clean_query.ipynb        | Databricks notebook with code to read, clean and query Pinterest batch data.                              |
| 8_0e36c8cd403d_dag.py                 | Python file. Contains code for MSWAA (AWS managed Airflow) to schedule a Databricks notebook run          |
| 9_stream_read_clean_write.ipynb       | Databricks notebook with code to read and clean Pinterest stream data, and then write it to Delta Tables. |
| 9_user_posting_emulation_streaming.py | Python file which extracts data from an AWS database and creates HTTP PUT messages for stream processing. |
| README.md                             | Text file (markdown format) description of the project.                                                   |
| extract.py                            | Classes used for data extraction.                                                                         |

#### Setup and Usage
The project was split into milestones. Work done for each of the milestones has been documented in the links below

[Milestone 3 Batch Processing: Configure the EC2 Kafka client](documentation%2F3%2Fmilestone3.md)

[Milestone 4 Batch Processing: Connect a MSK cluster to a S3 bucket](documentation%2F4%2Fmilestone4.md)

[Milestone 5 Batch Processing: Configuring an API in API Gateway](documentation%2F5%2Fmilestone5.md)

[Milestone 6 Batch Processing: Databricks](documentation%2F6%2Fmilestone6.md)

[Milestone 7 Batch Processing: Spark on Databricks](documentation%2F7%2Fmilestone7.md)

[Milestone 8 Batch Processing: AWS MWAA](documentation%2F8%2Fmilestone8.md)

[Milestone 9 Stream Processing: AWS Kinesis](documentation%2F9%2Fmilestone9.md)

#### License

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
