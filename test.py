import boto3

s3 = boto3.resource("s3")


def test():
    for bucket in s3.buckets.all():
        bucket_name: str = bucket.name

        print(bucket_name)

        bucket = s3.Bucket(bucket_name)

        print(bucket)
