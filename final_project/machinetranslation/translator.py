"""
Transate text between english and french using
IBM Watson Transaltion Cloud service
"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version=f'{VERSION}',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')

def englishToFrench(english_text):
    if english_text == '':
        return ''
    else:
        french_text = language_translator.translate(
            text=f'{english_text}', model_id='en-fr'
            ).get_result()
        return french_text['translations'][0]['translation']

def frenchToEnglish(french_text):
    if french_text == '':
        return ''
    else:
        english_text = language_translator.translate(
            text=f'{french_text}', model_id='fr-en'
            ).get_result()
        return english_text['translations'][0]['translation']
