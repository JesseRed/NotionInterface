import requests
#import pydicom
import os
import time



#port = int(os.getenv('MyPACS_PORT'))
NOTION_KEY="secret_Bg2w5W0fRJyYgAHl8huffd4ERlgs3VJ1OohTFG8I4mt"
NOTION_DATABASE_ID="385fcd6024784d89965537c8d60ef1cd"
#r = requests.get('https://api.github.com/events')
#r = requests.get('https://api.notion.com/v1/pages')


# url = "http://127.0.0.1:5000/flask/patients"
# url = "http://localhost/flask/DB/series/1.2.840.113619.2.5.191818202100.1388589027.605.5"
headers = {
    'Content-type':'application/json',
    'Authorization': 'TOK:secret_Bg2w5W0fRJyYgAHl8huffd4ERlgs3VJ1OohTFG8I4mt',
    'Notion-Version': '2021-05-13'
    }
headers = {
    'Content-type':'application/json',
    'Authorization': 'Bearer secret_Bg2w5W0fRJyYgAHl8huffd4ERlgs3VJ1OohTFG8I4mt',
    'Notion-Version': '2021-05-13'
    }


mydata =  {"parent": { "database_id": "385fcd6024784d89965537c8d60ef1cd" },
         "properties": {"Name": {"title": [{"text": {"content": "Yurts uhigin Big Sur, California"}}]}}
        }

# #response = requests.request("GET", url, headers=headers)
# #response = requests.request("GET", url)
# #status = "success"
# r = requests.get(url, stream=True)
# print(r.raw)
# print("response = ")
# print(r.content)
# j= r.json()
# print(j['response'])

#r = requests.post('https://api.notion.com/v1/pages', headers=headers, json = mydata)


#import requests

url = "https://api.notion.com/v1/databases/385fcd6024784d89965537c8d60ef1cd/query"
url = "https://api.notion.com/v1/databases/385fcd6024784d89965537c8d60ef1cd/query"

payload="{\"filter\": {\"property\": \"ID\",\"number\": {\"greater_than_or_equal_to\": 2}}}"
payload="{\"page_size\": 1}"
headers = {
  'Authorization': 'Bearer secret_Bg2w5W0fRJyYgAHl8huffd4ERlgs3VJ1OohTFG8I4mt',
  'Content-Type': 'application/json',
  'Notion-Version': '2021-05-13'
}

#response = requests.request("POST", url, headers=headers, data=payload)

#print(response.text)


#print(dir(response))
#j = response.json()
#results = j["results"]
#for i in results:
#    print(f"--- {i}")
#print(j["has_more"])


# reads one entry after the other
response = requests.request("POST", url, headers=headers, data=payload)
j = response.json()
print("first line --------------")
print(j["results"])
while j["has_more"]:
    print("has_more ...........")
    x = j["next_cursor"]
    print(f"next_cursor = {x}")
    
    payload="{\"page_size\": 1, \"start_cursor\": " + x + "}"
    payload="{\"page_size\": 1, \"start_cursor\": \"" + x + "\"}"
    print(f"payload = {payload}")
    response = requests.request("POST", url, headers=headers, data=payload)
    j = response.json()
    print(j)
    #print(j["results"])

#print(j["next_cursor"])
#print(response.status_code)
#myit = response.iter_lines()
#print(next(myit))
#print(next(myit))

##print(response.iter_lines)
#print(response.iter_content())
# headers = {
#   'Authorization': 'Bearer secret_Bg2w5W0fRJyYgAHl8huffd4ERlgs3VJ1OohTFG8I4mt',
#   'Content-Type': 'application/json',
#   'Notion-Version': '2021-05-13'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

#r = requests.post('https://api.notion.com/v1/pages', headers=headers)

#print(f"r={r}")
# secret_Bg2w5W0fRJyYgAHl8huffd4ERlgs3VJ1OohTFG8I4mt

# https://www.notion.so/b18b1fc03f2544e68cc83ae317530e90?v=3820dad39d8744eea153b6688c5e20c6
# https://www.notion.so/b18b1fc03f2544e68cc83ae317530e90?v=3820dad39d8744eea153b6688c5e20c6

# https://www.notion.so/385fcd6024784d89965537c8d60ef1cd?v=0b096b1550924b9d87ab374be67f8767



# curl -X POST https://api.notion.com/v1/pages \
#   -H "Authorization: Bearer secret_Bg2w5W0fRJyYgAHl8huffd4ERlgs3VJ1OohTFG8I4mt" \
#   -H "Content-Type: application/json" \
#   -H "Notion-Version: 2021-05-13" \
#   --data '{
#     "parent": { "database_id": "385fcd6024784d89965537c8d60ef1cd" },
#     "properties": {
#       "Name": {
#         "title": [
#           {
#             "text": {
#               "content": "Yurts in Big Sur, California"
#             }
#           }
#         ]
#       }
#     }
#   }'

# curl -X POST https://api.notion.com/v1/pages \
#   -H "Authorization: Bearer secret_Bg2w5W0fRJyYgAHl8huffd4ERlgs3VJ1OohTFG8I4mt" \
#   -H "Content-Type: application/json" \
#   -H "Notion-Version: 2021-05-13" \
#   --data '{
#     "parent": { "database_id": "385fcd6024784d89965537c8d60ef1cd" },
#     "properties": {
#       "Name": {
#         "title": [
#           {
#             "text": {
#               "content": "Yurts in Big Sur, California"
#             }
#           }
#         ]
#       }
#     }
#   }'



# url = "http://127.0.0.1:5000/flask/patients"
# url = "http://localhost/flask/DB/series/1.2.840.113619.2.5.191818202100.1388589027.605.5"
# headers = {
#     'User-Agent': "PostmanRuntime/7.20.1",
#     'Accept': "*/*",
#     'Cache-Control': "no-cache",
#     'Postman-Token': "b1be09a6-211c-4d2d-ac21-933e515f7203,64cfffda-75e3-4f32-a09a-b2e09b760ff1",
#     'Host': "127.0.0.1:5000",
#     'Accept-Encoding': "gzip, deflate",
#     'Connection': "keep-alive",
#     'cache-control': "no-cache"
#     }

# #response = requests.request("GET", url, headers=headers)
# #response = requests.request("GET", url)
# #status = "success"
# r = requests.get(url, stream=True)
# print(r.raw)
# print("response = ")
# print(r.content)
# j= r.json()
# print(j['response'])
