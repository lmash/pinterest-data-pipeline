# AiCore Project pinterest-data-pipeline


## Table of Contents
* [Project description](#project-description)
* [Tech Stack](#tech-stack)
* [Project aim](#project-aim)
* [What I've learned](#what-ive-learned)
* [Breakdown of steps](#breakdown-of-steps)
* [Setup](#setup)
* [Usage](#usage)
* [Description of files](#description-of-files)
* [Licence](#license)

#### Project description
This project replicates Pinterest's experimental data pipeline. We build a pipeline which contains both batch and streaming processing.
All configuration is done using AWS. The MSK cluster is already setup along with 2 roles.

### Tech Stack
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-000?style=for-the-badge&logo=apachekafka)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-FDEE21?style=flat-square&logo=apachespark&logoColor=black)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


#### Project aim
Put into practice concepts learnt about AWS, Apache Kafka, Apache Spark, Apache Airflow and Databricks.  

#### What I've learned
  - A pipeline consists of many independent parts, each which has to be configured, tested and implemented correctly
  - Working 

#### Description of files
| filename                              | description                                                                                                                                                               |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 5_user_posting_emulation.py           | Python file (markdown format) description of the project.                                                                                                                 |
| 6_mount_S3_bucket.ipynb               | Text file of packages to be installed by pip.                                                                                                                             |
| 7_batch_read_clean_query.ipynb        | Text file for API keys to be populated and renamed.                                                                                                                       |
| 8_0e36c8cd403d_dag.py                 | Javascript file. Contains most of the review and edit logic. Updates stars and ratings and re displays them after saving. <br/>Displays changed description after saving. |
| 9_stream_read_clean_write.ipynb       | Javascript file. Enables bootstrap tooltips.                                                                                                                              |
| 9_user_posting_emulation_streaming.py | Css file with shared styling for the project.                                                                                                                             |
| README.md                             | Text file (markdown format) description of the project.                                                                                                                   |

#### Setup
##### Pre-requisites
  - AWS cloud account
  - MSK Cluster Setup with **zookeeper connection string** and **bootstrap brokers** noted
  - EC2 Instance setup  
  - User setup with region us-east-1 logged into AWS console and AWS GUI
  - API REST Gateway

##### Milestones 
[Milestone 3 Batch Processing: Configure the EC2 Kafka client](documentation%2F3%2Fmilestone3.md)

[Milestone 4 Batch Processing: Connect a MSK cluster to a S3 bucket](documentation%2F4%2Fmilestone4.md)

[Milestone 5 Batch Processing: Configuring an API in API Gateway](documentation%2F5%2Fmilestone5.md)

[Milestone 6 Batch Processing: Databricks](documentation%2F6%2Fmilestone6.md)

[Milestone 7 Batch Processing: Spark on Databricks](documentation%2F7%2Fmilestone7.md)

[Milestone 8 Batch Processing: AWS MWAA](documentation%2F8%2Fmilestone8.md)

[Milestone 9 Stream Processing: AWS Kinesis](documentation%2F9%2Fmilestone9.md)

#### License

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
