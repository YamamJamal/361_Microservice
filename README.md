This is a guide to begin the microservice in order to request and receive data.

Step 1: First start the microservice by executing the file gpu_api.py you can do this by typing 'python gpu_api.py' in the terminal.

Step 2: Send an HTTP GET request by clicking the link that is provided in the terminal after running.

Step 3: To Receive data and store it in a variable for you to use, you can run the following python call.

Make sure you have imported the request library for you to use in the call.
#start
import requests
def fetch_gpu_data():
    response = requests.get('http://127.0.0.1:5000/api/gpu')
    if response.status_code == 200:
        gpu_data = response.json()
        return gpu_data
print(fetch_gpu_data())
#end

Here I added the print(fetch_gpu_data for you to see the json data printed for you in the terminal).

![image](https://user-images.githubusercontent.com/102646172/236986601-b42dbecb-f7fe-4027-9b96-0ee4e95be70e.png)
