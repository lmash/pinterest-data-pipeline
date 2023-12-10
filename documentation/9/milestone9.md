### Task 1: Create data streams using Kinesis Data Streams (AWS GUI)

![9.1.1.Pin_data_stream.jpg](9.1.1.Pin_data_stream.jpg)
![9.1.1.Geo_data_stream.jpg](9.1.1.Geo_data_stream.jpg)
![9.1.1.User_data_stream.jpg](9.1.1.User_data_stream.jpg)

### Task 2: Configure an API with Kinesis proxy integration (AWS GUI)
#### Create Resource to List Streams in Kinesis
**Create resource with GET method**
![9.2.1.Add_Streams_method_get.jpg](9.2.1.Add_Streams_method_get.jpg)

**Edit integration request add HTTP header**
![9.2.2.Add_HTTP_to_integration_request.jpg](9.2.2.Add_HTTP_to_integration_request.jpg)

**Add Mapping Template**
![9.2.3.Add_Mapping_template_to_integration_request.jpg](9.2.3.Add_Mapping_template_to_integration_request.jpg)

#### Create new child resource with methods to Create, Describe and Delete a Stream in Kinesis
**New child resource under streams with the Resource Path {stream-name}**
![9.2.4.Child_resource.jpg](9.2.4.Child_resource.jpg)

Create methods for each of the below using the same steps as the above with the following variations

| Method | Action         | 
|--------|----------------|
| GET    | DescribeStream |
| POST   | CreateStream   |
| DELETE | DeleteStream   |


**GET method Template contents**
```
{
    "StreamName": "$input.params('stream-name')"
}
```
**POST method Template contents**
```
{
    "ShardCount": #if($input.path('$.ShardCount') == '') 5 #else $input.path('$.ShardCount') #end,
    "StreamName": "$input.params('stream-name')"
}
```
**DELETE method Template contents**
```
{
    "StreamName": "$input.params('stream-name')"
}
```

#### Create new child resources for record and records
![9.2.5.Child_resource_record.jpg](9.2.5.Child_resource_record.jpg)
![9.2.6.Child_resource_records.jpg](9.2.6.Child_resource_records.jpg)

Create methods for each of the below using the same steps as the above with the following variations

| Resource | Method | Action      | 
|----------|--------|-------------|
| record   | PUT    | PutRecord   |
| records  | PUT    | PutRecords  |

**Resource record PUT method Template contents**
```
{
    "StreamName": "$input.params('stream-name')",
    "Data": "$util.base64Encode($input.json('$.Data'))",
    "PartitionKey": "$input.path('$.PartitionKey')"
}
```

**Resource records PUT method Template contents**
```
{
    "StreamName": "$input.params('stream-name')",
    "Records": [
       #foreach($elem in $input.path('$.records'))
          {
            "Data": "$util.base64Encode($elem.data)",
            "PartitionKey": "$elem.partition-key"
          }#if($foreach.hasNext),#end
        #end
    ] 
}
```
### Task 3: Send data to the Kinesis streams
[9_stream_user_posting_emulation.py](..%2F..%2F9_stream_user_posting_emulation.py)

### Task 4: Read data from Kinesis streams in databricks
![9.4.1.GeoData.jpg](9.4.1.GeoData.jpg)
![9.4.2.PinData.jpg](9.4.2.PinData.jpg)
![9.4.3.UserData.jpg](9.4.3.UserData.jpg)

### Task 5: Transform Kinesis streams in databricks
As we are streaming the same data we processed in batch if the data is in a matching dataframe it can be processed with the same cleaning queries
**Create a scheme for each dataframe**
![9.5.1.CreateStructures.jpg](9.5.1.CreateStructures.jpg)
**Convert string data to multiple fields**
![9.5.2.ConvertData.jpg](9.5.2.ConvertData.jpg)

**Clean data**
Use the same queries as Milestone 7

### Task 6: Write the streaming data to Delta Tables
**Write streaming pin data**
![9.6.1.Write_pin.jpg](9.6.1.Write_pin.jpg)
![9.6.2.Pin_data_written.jpg](9.6.2.Pin_data_written.jpg)

**Write streaming geo data**
![9.6.3.Write_geo.jpg](9.6.3.Write_geo.jpg)
![9.6.4.Geo_data_written.jpg](9.6.4.Geo_data_written.jpg)

**Write streaming user data**
![9.6.5.Write_user.jpg](9.6.5.Write_user.jpg)
![9.6.6.User_data_written.jpg](9.6.6.User_data_written.jpg)