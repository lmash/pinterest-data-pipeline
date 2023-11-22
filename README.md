# AiCore Project pinterest-data-pipeline


## Table of Contents
* [Project description](#project-description)
* [Tech Stack](#tech-stack)
* [Project aim](#project-aim)
* [What I've learned](#what-ive-learned)
* [Breakdown of steps](#breakdown-of-steps)
* [Setup](#setup)
* [Usage](#usage)
* [File structure](#file-structure)
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
Consolidate data engineering concepts covered. 

#### What I've learned
  - t.b.c.

#### File structure
t.b.c.

#### Setup Noted
| AWS Setting                             | Value                                                                                                                                                                                                             |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Zookeeper connection string (PLAINTEXT) | z-2.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:2181,z-1.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:2181,z-3.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:2181 |
| Bootstrap brokers                       | b-1.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-3.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-2.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098 |
| 0e36c8cd403d-ec2-access-role ARN        | arn:aws:iam::584739742957:role/0e36c8cd403d-ec2-access-role                                                                                                                                                       |
| S3 bucket name                          | user-0e36c8cd403d-bucket                                                                                                                                                                                          |
| EC2 public DNS                          | ec2-107-22-147-56.compute-1.amazonaws.com                                                                                                                                                                         |
| Invoke URL (API Gateway)                | https://jydbc247f4.execute-api.us-east-1.amazonaws.com/Prod                                                                                                                                                       |


#### Setup
##### Pre-requisites
  - AWS cloud account
  - MSK Cluster Setup with **zookeeper connection string** and **bootstrap brokers** noted
  - EC2 Instance setup  
  - User setup with region us-east-1 logged into AWS console and AWS GUI
  - API REST Gateway

##### Milestone 3 
[Batch Processing: Configure the EC2 Kafka client](setup%2Fmilestone3.md)

##### Milestone 4
[Batch Processing: Connect a MSK cluster to a S3 bucket](setup%2Fmilestone4.md)

##### Milestone 5
[Batch Processing: Configuring an API in API Gateway](setup%2Fmilestone5.md)

##### Milestone 6
[Batch Processing: Databricks](setup%2Fmilestone6.md)

#### License

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
