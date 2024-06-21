import requests
import json

# Przykładowy token Slack Webhook URL do wstawienia (który zostanie znaleziony)
slack_webhook_url = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"

def send_message_to_slack(message: str):
    payload = {
        "text": message
    }
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(slack_webhook_url, data=json.dumps(payload), headers=headers)
    if response.status_code != 200:
        raise ValueError(f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}")

# Przykładowe wysłanie wiadomości do Slacka
send_message_to_slack("Hello, this is a test message from your Python script!")
