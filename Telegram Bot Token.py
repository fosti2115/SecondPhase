# Example Telegram Bot Token
TELEGRAM_BOT_TOKEN = '123456789:ABCDEF1234-Example_Token'

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=data)
    return response.json()

if __name__ == "__main__":
    chat_id = '123456789'
    text = 'Hello, this is a test message.'
    print(send_message(chat_id, text))
