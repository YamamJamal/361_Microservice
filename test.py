import requests


def fetch_gpu_data():
    # Make an HTTP GET request to the /api/gpu endpoint
    response = requests.get('http://127.0.0.1:5000/api/gpu')

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        gpu_data = response.json()
        return gpu_data
    else:
        print('Error fetching GPU data:', response.status_code)
        return None


gpu_data = fetch_gpu_data()

if gpu_data is not None:
    print(gpu_data)


# Do something with the GPU data
# else:
#     # Handle the case when GPU data retrieval failed
#     pass
