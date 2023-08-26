import requests
from datetime import datetime


USERNAME = "leusha4ever"
TOKEN ="leusha4ever"
GRAPH_ID ="graph1"


pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor": "yes",
    
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    
    "id":GRAPH_ID,
    "name":"Coding",
    "unit":"hours",
    "type":"float",
    "color":"shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN,
}


response = requests.post(url=graph_endpoint, json=graph_config,headers=headers)
print(response.text)





post_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
graph_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you code today?",),
}
response = requests.post(url=post_graph_endpoint, json=graph_params,headers=headers)
print(response.text)



# updating the graph-------------------->

update_graph_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_params = {
    "quantity":"1.6"
}
response = requests.put(url=update_graph_endpoint,json=update_params,headers=headers)
print(response.text)


# deleting a pixel-------------------->

delete_pixel_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_pixel_endpoint,headers=headers)
print(response.text)