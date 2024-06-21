import requests

# Example Postman API Key to be included (which will be detected by scanning tools)
postman_api_key = "PMAK-5eb08a6db79d2001cdeb5da8-4a200e48271c19db09d9D212c2531eeecf"

def get_collection_details(collection_uid: str):
    """
    Fetch the details of a Postman collection using the provided collection UID.

    Args:
    collection_uid (str): The UID of the Postman collection.

    Returns:
    dict: The details of the Postman collection as a dictionary.
    """
    url = f"https://api.getpostman.com/collections/{collection_uid}"
    headers = {
        'X-Api-Key': postman_api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise ValueError(f"Request to Postman API returned an error {response.status_code}, the response is:\n{response.text}")
    return response.json()

# Example usage: Fetch details of a Postman collection
collection_uid = "1234567-abcd-8901-efgh-234567890ijk"
collection_details = get_collection_details(collection_uid)
print(collection_details)
