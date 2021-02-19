import requests
import datetime as dt
pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "removed"
TOKEN = "removed"
GRAPH_ID = "graph1"

headers = {
    "X-USER-TOKEN": TOKEN
}
#
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# $ curl -X POST https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret' -d '{"id":"test-graph",
# "name":"graph-name","unit":"commit","type":"int","color":"shibafu"}'

# note the url now has /v1/users/<username>/graphs
#
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "momiji",
# }
#
#
# # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#
# # pixela_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
#
# today = dt.datetime.now().strftime("%Y%m%d")
#
#
#
# pixel_data = {
#     "date": today,
#     "quantity": input("How many kilometers did you cycle today? "),
# }

#
# response = requests.post(url=pixela_endpoint, json=pixel_data, headers=headers)

# print(response.text)

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
#
# update_pixel = {
#     "quantity": "15",
# }
#
# response = requests.put(url=update_endpoint, json=update_pixel, headers=headers)
# print(response.text)

delete_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

response = requests.delete(url=delete_graph_endpoint, headers=headers)

print(response.text)