import requests
import json
import time

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(url, headers, params):
    response = requests.request("GET",
                                search_url,
                                headers=headers,
                                params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def func_call(id):
        headers = create_headers(bearer_token)
        json_response = connect_to_endpoint(search_url, headers, query_params)
        # print(json.dumps(json_response, indent=4, sort_keys=True))
        return json_response

data_list = []

for id in convo_id_dict:
  bearer_token = "BEARER TOKEN"
  search_url = "https://api.twitter.com/2/tweets/search/all"
  # conversation_id = str(id)
  conversation_id = convo_id_dict[id]
  if conversation_id!= "NA":
    query_params = {
        'query': 'conversation_id:{}'.format(conversation_id),
        'tweet.fields': 'conversation_id',
        'start_time': '2021-01-25T00:00:00Z',
        'max_results': 50}

    # Replace with conversation ID below (Tweet ID of the root Tweet)
    # conversation_id = str(id)
    data_list.append(func_call(conversation_id))
  else:
    data_list.append("NA")
  time.sleep(1)