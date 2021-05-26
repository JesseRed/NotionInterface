import requests
#import pydicom
import os
import time
import json


#port = int(os.getenv('MyPACS_PORT'))
NOTION_KEY="secret_Bg2w5W0fRJyYgAHl8huffd4ERlgs3VJ1OohTFG8I4mt"
NOTION_KEY="secret_Aj82oDGkp6lUL7tPpGru22izDDFiNkquMRK1Cw5DNwv"


NOTION_DATABASE_ID="385fcd6024784d89965537c8d60ef1cd"
NOTION_DATABASE_ID="fc5f22706f6d4f5b88aa8aebbc0f90f6"
#https://www.notion.so/For-Franzi-fc5f22706f6d4f5b88aa8aebbc0f90f6



mydata =  {"parent": { "database_id": "fc5f22706f6d4f5b88aa8aebbc0f90f6" },
         "properties": {"Name": {"title": [{"text": {"content": "Yurts uhigin Big Sur, California"}}]}}
        }

url = "https://api.notion.com/v1/databases/385fcd6024784d89965537c8d60ef1cd/query"
url = "https://api.notion.com/v1/databases/fc5f22706f6d4f5b88aa8aebbc0f90f6/query"
url = "https://api.notion.com/v1/databases/fc5f22706f6d4f5b88aa8aebbc0f90f6/query"
url = "https://api.notion.com/v1/databases/ba1205b5c86048a2a1d2e0490b5c38ec/query"

payload="{\"filter\": {\"property\": \"ID\",\"number\": {\"greater_than_or_equal_to\": 2}}}"
payload="{\"page_size\": 1}"
#payload="{ }"
headers = {
  'Authorization': 'Bearer secret_Aj82oDGkp6lUL7tPpGru22izDDFiNkquMRK1Cw5DNwv',
  'Content-Type': 'application/json',
  'Notion-Version': '2021-05-13'
}


# reads one entry after the other
response = requests.request("POST", url, headers=headers, data=payload)
j1 = response.json()
print("first line --------------")
print(j1["results"])
j = j1
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


print("printing results")
r = j1["results"][0]
print(r)

print("--------------")
print(f"filename 1= {r['properties']['File_1']['rich_text'][0]['plain_text']}")
#/BIOMAG_DATA/STORAGE/184987d2-0222-4194-95c6-bd25a0bce348/20200115_09h10_0010995889_info.txt
#rsync -av -e 'ssh -p 2222' ck@dresden.biomag.uni-jena.de:/BIOMAG_DATA/STORAGE/184987d2-0222-4194-95c6-bd25a0bce348/20200115_09h10_0010995889_info.txt .
