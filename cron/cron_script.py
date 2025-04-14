import requests

API_URL = "http://hello-service.dev-playground.svc.cluster.local/hello"  # Update with your service's cluster URL

try:
    response = requests.get(API_URL)
    print(f"Response from API: {response.text}")
except Exception as e:
    print(f"Error calling API: {e}")