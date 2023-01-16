import requests
from datetime import datetime

USERNAME = "YOUR-USERNAME"
TOKEN = "YOUT-TOKEN"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling chart",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
today = datetime.now()

pixela_endpoint2 = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometres did you cycle today?:"),
}

response = requests.post(url=pixela_endpoint2, headers=headers, json=pixel_data)
print(response.text)

#Changing a pixel

pixel_update_endpoint = f"{pixela_endpoint2}/20221102"

update_pixel_data = {
    "quantity": "14.9",
}

# response = requests.put(url=pixel_update_endpoint, headers=headers, json=update_pixel_data)
# print(response.text)

# Deleting a pixel

deletion_endpoint = f"{pixela_endpoint2}/20221102"
response = requests.delete(url=deletion_endpoint, headers=headers)
print(response)
