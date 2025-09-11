import requests
import logging

# Configure logging to write errors to a file named 'http_errors.log'
logging.basicConfig(filename='http_errors.log', level=logging.ERROR, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def send_get_request(url):
    """Sends a GET request to the specified URL and displays the response."""
    print("\n--- Sending GET Request ---")
    try:
        # Send the GET request
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        print(f"Request to: {url}")
        print(f"Status Code: {response.status_code} {response.reason}")
        
        print("\n[Response Headers]")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
            
        print("\n[Response Body]")
        # Assuming the response body is JSON, print it nicely
        print(response.json())

    except requests.exceptions.RequestException as e:
        print(f"Error: The request to {url} failed.")
        logging.error(f"GET request to {url} failed: {e}")

def send_post_request(url, data):
    """Sends a POST request with data to the specified URL and displays the response."""
    print("\n--- Sending POST Request ---")
    try:
        # Send the POST request with a JSON payload
        response = requests.post(url, json=data, timeout=5)
        response.raise_for_status()

        print(f"Request to: {url}")
        print(f"Status Code: {response.status_code} {response.reason}")
        
        print("\n[Response Headers]")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
            
        print("\n[Response Body]")
        print(response.json())

    except requests.exceptions.RequestException as e:
        print(f"Error: The request to {url} failed.")
        logging.error(f"POST request to {url} failed with data {data}: {e}")

if __name__ == "__main__":
    # A public API for testing requests
    test_api_url = "https://jsonplaceholder.typicode.com/posts"

    # 1. Send GET request to retrieve posts
    send_get_request(test_api_url + '/1')

    # 2. Send POST request to create a new post
    new_post_data = {
        'title': 'Computer Networks',
        'body': 'This is a test post for the HTTP assignment.',
        'userId': 1
    }
    send_post_request(test_api_url, new_post_data)

    # 3. Example of a failed request for error logging
    send_get_request("https://thissitedoesnotexist.xyz")
