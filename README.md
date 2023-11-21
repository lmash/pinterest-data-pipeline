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

#### Setup Note
| AWS Setting                   | Value  |
|-------------------------------|--------|
| Zookeeper connection string   |        |
| Bootstrap brokers             |        |
| 0e36c8cd403d-ec2-access-role  |        |


#### Setup
##### Pre-requisites
  - AWS cloud account
  - MSK Cluster Setup with **zookeeper connection string** and **bootstrap brokers** noted
  - EC2 Instance exists with 
  - User setup with region us-east-1 logged into AWS console

##### Milestone 3 
[Configure the EC2 Kafka client](setup%2Fmilestone3.md)

##### Milestone 4
1. Create a custom plugin with MSK Connect
   - Download Confluent.io Amazon S3 Connector onto the EC2 instance
   - Copy Confluent.io Amazon S3 Connector to S3 bucket
   - Create the MSK Connect connector referencing the Confluent.io Amazon S3 Connector.zip in S3 bucket
2. Create a connector with MSK Connect
   - 

#### License
Licensed under the [MIT](https://github.com/lmash/pinterest-data-pipeline924/blob/main/LICENSE) license.