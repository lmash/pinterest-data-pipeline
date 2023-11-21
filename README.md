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
This project t.b.c.
All configuration is done using AWS. The MSK cluster is already setup along with 2 roles.

### Tech Stack
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-000?style=for-the-badge&logo=apachekafka)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-FDEE21?style=flat-square&logo=apachespark&logoColor=black)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


#### Project aim
t.b.c.
Provide scripted setup so that AWS configuration is automated 

#### What I've learned
  - t.b.c.

#### Setup Noted
| AWS Setting                             | Value                                                                                                                                                                                                             |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Zookeeper connection string (PLAINTEXT) | z-2.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:2181,z-1.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:2181,z-3.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:2181 |
| Bootstrap brokers                       | b-1.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-3.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-2.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098 |
| 0e36c8cd403d-ec2-access-role ARN        | arn:aws:iam::584739742957:role/0e36c8cd403d-ec2-access-role                                                                                                                                                       |
| S3 bucket name                          | user-0e36c8cd403d-bucket                                                                                                                                                                                          |


#### Setup
##### Pre-requisites
  - AWS cloud account
  - MSK Cluster Setup with **zookeeper connection string** and **bootstrap brokers** noted
  - EC2 Instance exists  
  - User setup with region us-east-1 logged into AWS console and AWS GUI

##### Milestone 3 
[Batch Processing: Configure the EC2 Kafka client](setup%2Fmilestone3.md)

##### Milestone 4
[Batch Processing: Connect a MSK cluster to a S3 bucket](setup%2Fmilestone4.md)

#### License
Licensed under the [MIT](https://github.com/lmash/pinterest-data-pipeline924/blob/main/LICENSE) license.