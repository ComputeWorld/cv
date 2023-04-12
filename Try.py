import requests
import json
from chatterbot import ChatBot

translator_api_key = 'YOUR_TRANSLATOR_API_KEY_HERE'
translator_api_url = 'https://translation.googleapis.com/language/translate/v2'

def translate(text, source_language, target_language):
    payload = {
        'key': translator_api_key,
        'q': text,
        'source': source_language,
        'target': target_language
    }
    response = requests.post(translator_api_url, data=payload)
    translation = json.loads(response.text)['data']['translations'][0]['translatedText']
    return translation

chatbot = ChatBot('Translator')

while True:
    user_input = input('You: ')
    translated_input = translate(user_input, 'en', 'hi') # translate from English to Hindi
    translated_response = chatbot.get_response(translated_input)
    response = translate(str(translated_response), 'hi', 'en') # translate back to English
    print('Chatbot:', response)
