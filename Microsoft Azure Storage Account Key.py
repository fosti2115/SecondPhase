from azure.storage.blob import BlobServiceClient

# Example Azure Storage Account Key
AZURE_STORAGE_ACCOUNT_NAME = 'myaccountname'
AZURE_STORAGE_ACCOUNT_KEY = 'oOrbZg9EDosW4nZvGoxrmSt14P49fS7zPd81h5ZBlmrUq7O3IYr7j90Zye6amnnW9M7dPvqUxKZg0s0oJm1j/DR8HnfM3gmQF4uTpPHFJgB7xvhhblB7gD1Xy+4Z2B8jm9b0n/W5jJ2NWGmWgHRYVJg=='
ENDPOINT_SUFFIX= 'core.windows.net'

def list_containers():
    try:
        blob_service_client = BlobServiceClient(account_url=f"https://{AZURE_STORAGE_ACCOUNT_NAME}.blob.core.windows.net", credential=AZURE_STORAGE_ACCOUNT_KEY)
        containers = blob_service_client.list_containers()
        for container in containers:
            print(f"Container: {container.name}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_containers()
