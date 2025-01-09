import boto3

def list_s3_buckets():
    # Create an S3 client
    s3_client = boto3.client('s3')
    
    try:
        # List buckets
        response = s3_client.list_buckets()
        
        print("S3 Buckets in your account:")
        for bucket in response['Buckets']:
            print(f"- {bucket['Name']}")
            
    except Exception as e:
        print(f"Error fetching bucket list: {e}")

# Run the function
if __name__ == "__main__":
    list_s3_buckets()
