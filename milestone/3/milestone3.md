### Task 3: Set up Kafka on the EC2 instance

**Install kafka software (AWS console)**
```commandline
sudo yum install java-1.8.0
wget https://archive.apache.org/dist/kafka/2.8.1/kafka_2.12-2.8.1.tgz
tar -xzf kafka_2.12-2.8.1.tgz
```

**Install IAM MSK authentication package (AWS console)**
```commandline
cd /home/ec2-user/kafka_2.12-2.8.1/libs
wget https://github.com/aws/aws-msk-iam-auth/releases/download/v1.1.5/aws-msk-iam-auth-1.1.5-all.jar
```

**Add principal to role's trust relationship (AWS GUI)**

https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1#/roles/details/0e36c8cd403d-ec2-access-role?section=permissions

Note role ARN

Edit trust relationship to be able to assume the 0e36c8cd403d-ec2-access-role, which contains the necessary permissions to authenticate to the MSK cluster.
![3.3.Edit_trust_relationship.jpg](%2F3.3.Edit_trust_relationship.jpg)

**Configure Kafka client to use AWS IAM authentication to the cluster (AWS console)**
```commandline
cd /home/ec2-user
touch kafka_2.12-2.8.1/bin/client.properties
vi kafka_2.12-2.8.1/bin/client.properties
```
Add the below and then save the file
```shell
# Sets up TLS for encryption and SASL for authN.
security.protocol = SASL_SSL

# Identifies the SASL mechanism to use.
sasl.mechanism = AWS_MSK_IAM

# Binds SASL client implementation.
sasl.jaas.config=software.amazon.msk.auth.iam.IAMLoginModule required awsRoleArn="arn:aws:iam::584739742957:role/0e36c8cd403d-ec2-access-role";

# Encapsulates constructing a SigV4 signature based on extracted credentials.
# The SASL client bound by "sasl.jaas.config" invokes this class.
sasl.client.callback.handler.class = software.amazon.msk.auth.iam.IAMClientCallbackHandler
```

### Task 4: Create Kafka topics
On the AWS console
```commandline
./kafka-topics.sh --bootstrap-server b-1.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-3.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-2.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098 --command-config client.properties --create --topic 0e36c8cd403d.pin

./kafka-topics.sh --bootstrap-server b-1.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-3.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-2.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098 --command-config client.properties --create --topic 0e36c8cd403d.geo

./kafka-topics.sh --bootstrap-server b-1.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-3.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-2.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098 --command-config client.properties --create --topic 0e36c8cd403d.user
```