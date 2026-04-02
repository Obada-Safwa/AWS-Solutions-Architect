import boto3

s3 = boto3.client('s3')

bucket_name = "my-bucket-name325145"
region = "eu-central-1"

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={'LocationConstraint': region}
)

print(f"Bucket {bucket_name} created successfully")
# Create a file and write to it
with open("/tmp/hello.txt", "w") as f:
    f.write("Hello World\n")
    f.write("This is line 2\n")
    f.write("This is line 3\n")

print("File created successfully")

with open("/tmp/hello.txt", "rb") as data:
    print("data", data)
    s3.put_object(Bucket=bucket_name, Key="hello.txt", Body=data)

print("File added to Bucket successfully")