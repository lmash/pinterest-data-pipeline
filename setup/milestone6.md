### Mount a S3 bucket to Databricks
Pre-requisite: Databricks account has full access to S3 bucket with Access Key & Secret Access Key in authentication_credentials.csv
All steps performed in Databricks

**Check for authentication_credentials.csv**
```
dbutils.fs.ls("/FileStore/tables")
```
![6.2.Credentials.jpg](6.2.1.Credentials.jpg)

**Read the csv with AWS keys into a spark dataframe**
![6.2.2.Read csv with aws keys.jpg](6.2.2.Read_csv_with_aws_keys.jpg)

**Extract AWS access key and secret key from spark dataframe**
![6.2.3.Extract_keys.jpg](6.2.3.Extract_keys.jpg)

**Mount the S3 bucket**
![6.2.3.Mount_S3_bucket.jpg](6.2.3.Mount_S3_bucket.jpg)

**Create the 3 dataframes**
![6.2.4.Create_3_dataframes.jpg](6.2.4.Create_3_dataframes.jpg)
