import requests

def emotion_detector(text_to_analyze):
    # Define the URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Define the input JSON payload
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send the POST request
    response = requests.post(url, json=payload, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Assuming the response is in JSON format and has a 'text' attribute
        result_text = response.json().get('text')
        return result_text
    else:
        # If the request was not successful, print an error message
        print(f"Error: {response.status_code}")
        return None

# Example usage
text_to_analyze = "Your input text here."
result = emotion_detector(text_to_analyze)
print("Result:", result)
