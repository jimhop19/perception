import requests
import json
response_API = requests.get('http://localhost:9080/crawl.json?spider_name=spider_pts&start_requests=true&crawl_args={%22keyword%22:"黑熊"}')
#print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
print(parse_json["items"][0])