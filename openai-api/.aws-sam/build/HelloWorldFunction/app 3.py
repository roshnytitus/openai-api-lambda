import json
import os
import openai

# import requests
openai.api_key = os.getenv("OPENAI_API_KEY")


def lambda_handler(event, context):
    
    # body = json.loads(event['body'])
    subjects = event['queryStringParameters']['subjects']

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create a detailed study schedule to help me prepare for my exams. The schedule should span the next seven days and include specific tasks to be completed each day. The exams will each cover one of the following subjects and will be held on their respective exam dates: {subjects}.",
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )   

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response['choices'][0]['text']),
    }
