import json
import os
import requests

# load the config from the config.json file
with open('config.json', 'r') as f:
    config = json.load(f)

# build the URL using the config values
url = f"http://{config['ip']}:{config['port']}/api/ask"
headers = {'Authorization': str(config['api_key'])}

# define a default value for the data variable
data = {'content': 'Hello world'}

# check if response.json file exists
if os.path.exists('response.json'):
    # load the response from the file
    with open('response.json', 'r') as f:
        response_data = json.load(f)

    data_content = input("Enter the data content: ")

    # check if response_id and conversation_id have values in the response
    if response_data.get('response_id') and response_data.get('conversation_id'):
        # update the data dictionary with the response_id and conversation_id values
        data.update({
            'content': data_content,
            'conversation_id': response_data['conversation_id'],
            'parent_id': response_data['response_id']
        })

# send the request with the data dictionary
response = requests.post(url, headers=headers, json=data)

# save the response to the response.json file
with open('response.json', 'w') as f:
    json.dump(response.json(), f)

# print the content from the response
print(response.json()['content'])
