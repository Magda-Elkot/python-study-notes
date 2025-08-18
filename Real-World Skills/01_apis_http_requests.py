# Topic: APIs & HTTP Requests
# Demonstrates basic GET, POST, PUT, PATCH, DELETE requests using a public test API

import requests

# -------- GET request --------
# Fetches data from an endpoint
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("GET request result:", response.json())  # prints the JSON data

# -------- POST request --------
# Sends new data to the server
data = {"title": "Hello World", "body": "This is a test post", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print("POST request result:", response.json())

# -------- PUT request --------
# Updates a full resource
update_data = {"id": 1, "title": "Updated Title", "body": "Updated body", "userId": 1}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=update_data)
print("PUT request result:", response.json())

# -------- PATCH request --------
# Updates part of a resource
patch_data = {"title": "Patched Title"}
response = requests.patch("https://jsonplaceholder.typicode.com/posts/1", json=patch_data)
print("PATCH request result:", response.json())

# -------- DELETE request --------
# Deletes a resource
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print("DELETE request status code:", response.status_code)  # 200 means success
