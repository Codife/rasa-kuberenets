import concurrent.futures

import requests
import random


urls = []

for i in range(1, 801):
    urls.append("http://localhost:80/webhooks/rest/webhook")


# Function to make a GET request to a URL

def make_request(url):
    sentence = {
        "sender": random.random(),
        "message": "show me boots under 900"
    }
    rasa_output = requests.post(url=url, json=sentence)
    return rasa_output.json()


# Create a ThreadPoolExecutor with max_workers as the number of requests to make

with concurrent.futures.ThreadPoolExecutor(max_workers=len(urls)) as executor:

    # Submit the requests and get the futures

    futures = [executor.submit(make_request, url) for url in urls]




    # Wait for all futures to complete

    results = concurrent.futures.wait(futures)




# Get the results from completed futures

for future in results.done:

    response = future.result()

    print('Response:', response)
    
    
print(len(results.done))