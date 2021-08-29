import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('SJqbPI7mf0lhFLbOa04VIuqeWope93RJtUFEfMhpLYsP')
assistant = AssistantV2(
    version='2021-06-14',
    authenticator = authenticator
)

assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com')
response = assistant.create_session(
    assistant_id='9d449feb-47a6-498a-b6a0-83b541d384c9'
).get_result()
session_id = response
session_id = session_id["session_id"]
print(type(session_id))
print(session_id)

while True:
    input_text = input("enter the text")
    response = assistant.message(
    assistant_id='9d449feb-47a6-498a-b6a0-83b541d384c9',
    session_id = session_id,
    input={
        'message_type': 'text',
        'text': input_text
    }
).get_result()

    print(response)
    print(response["output"]["generic"][0]["text"])

