import requests

url = "https://flashchainsign.com/bes/contract/home"
headers = {
    'Authorization': 'Bearer ebd92ae8-bab7-470b-b3e5-3d0f2f350d4b',
    'Content-Type': 'application/json'
}

payload = {
    # "queryType": 8,
    # "pageNum": 1,
    # "pageSize": 10,
    # "contractName": "",
    "orgId": 0
}
print(payload)

response = requests.request('post', url, headers=headers, json=payload)
print(response.text)
