import requests
import json

get_poll_by_id = {"filter": {"id": "2"}}
get_passed_polls = {"filter": {"user_id": 2940243}}
get_all_active_polls = {"filter": {"status": "active"}}
json_to_post = {"poll_id": "2", "user_id": "100453", "answers": "1;4"}


resp = requests.get("http://127.0.0.1:5000/api/get_poll", json=get_poll_by_id)
resp = requests.get("http://127.0.0.1:5000/api/active_polls", json=get_all_active_polls)
resp = requests.get("http://127.0.0.1:5000/api/get_passed_polls", json=get_passed_polls)
resp = requests.post("http://127.0.0.1:5000/api/send_poll_answer", data=json_to_post)
print(json.dumps(resp.json(), indent=4))
