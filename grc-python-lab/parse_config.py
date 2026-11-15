import json

# Open and load the JSON file into a Python dictionary
with open("s3_config.json", "r") as file:
    bucket_data = json.load(file)

# Drill down into the dictionary keys (just like a cloud API response)
bucket_name = bucket_data["BucketName"]
is_encrypted = bucket_data["Encryption"]["Enabled"]
block_policy = bucket_data["PublicAccessBlock"]["BlockPublicPolicy"]

print(f"Auditing Bucket: {bucket_name}")
print(f"Encryption Enabled: {is_encrypted}")
print(f"Public Policy Blocked: {block_policy}")