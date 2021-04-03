
import requests

# payload = {
# "post": "Today is a great day!",
# "platforms": ["twitter", "facebook"],
# # "media_urls": ["work.jpg"] #Required for Instagram
# }

payload = {
    "lastDays" : 5
# "post": "Today is a great day!",
# "platforms": ["twitter", "facebook"],
# "media_urls": ["work.jpg"] #Required for Instagram
}

# Live API Key
# 'Content-Type': 'application/json', 
headers = {
        'Authorization': 'Bearer token'}

r = requests.get('url', 
    json=payload, 
    headers=headers)
print(r.__dict__)
print(r.json)
print(r.text)
print(r.content)
print(r.encoding)