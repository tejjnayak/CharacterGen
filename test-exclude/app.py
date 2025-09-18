import requests

# Make a GET request
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Check the status code
if response.status_code == 200:
    # Print the JSON response
    print(response.json())
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
