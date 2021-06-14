''' Import Libraries '''

from flask import Flask, request, jsonify, render_template
import os
import json
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import requests
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_watson import TextToSpeechV1
import logging as logger

''' Initialize Flask Variables '''
logger.basicConfig(level="DEBUG")

app = Flask(__name__)
account_sid = ""
auth_token = ""
filePath = './static/audios/'
apikey = ''
url = ''
assistantid = ''
sessionid = ''

#########################
# Watson Assistant Sessions
#########################

def createSession():
    global sessionid
    session = assistant.create_session(assistantid).get_result()
    sessionid = session.get('session_id')
    print('New Session created ID: ', sessionid)

def destroySession():
    try:
        response = assistant.delete_session(
        assistant_id=assistantid, session_id=sessionid).get_result()
        print(response)
    except Exception as e:
        pass

def session():
    global sessionid
    if sessionid == '':
        createSession()
    else:
        destroySession()
        createSession()

def watsonAssistant(msg):

        message = assistant.message(
            assistantid,
            sessionid,
            input={'text': msg}
        ).get_result()
        
        try:
            payload = {
                "message": message['output']['generic'][0]['text']
            }
        except:
            payload = {
                "message": "Eu não entendi. Você pode tentar reformular a frase."
            }

        return payload['message']

class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        print(json.dumps(data, indent=2))

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))

myRecognizeCallback = MyRecognizeCallback()

def speechtoText():
    with open('speechtotext.json', 'r') as credentialsFile:
            credentials = json.loads(credentialsFile.read())

    stt_apikey = credentials.get('apikey')
    stt_url = credentials.get('url')

    authenticator = IAMAuthenticator(stt_apikey)
    speech_to_text = SpeechToTextV1(
        authenticator=authenticator
    )

    speech_to_text.set_service_url(stt_url)

    with open(filePath+"input.ogg",'rb') as audio_file:
        speech_recognition_results = speech_to_text.recognize(
            audio=audio_file,
            content_type='audio/ogg',
            recognize_callback=myRecognizeCallback,
            model='pt-BR_BroadbandModel',
        ).get_result()
        text_translation = speech_recognition_results["results"][0]["alternatives"][0]["transcript"]
    return text_translation.strip()

@app.route('/', methods=['GET', 'POST'])
def index():

    try:
        with open('watsonassistant.json', 'r') as credentialsFile:
            credentials = json.loads(credentialsFile.read())
            global apikey, url, assistantid, authenticator, assistant
            apikey = credentials.get('apikey')
            url = credentials.get('url')
            assistantid = credentials.get('assistant-id')

            authenticator = IAMAuthenticator(apikey)
            assistant = AssistantV2(
                version='2020-04-01',
                authenticator=authenticator
            )

            assistant.set_service_url(url)

    except:
        logger.debug('Watson Assistant Credentials not found!')

    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        
        getTwilioCredentials()
        
        ResponseMsg = json.dumps(request.form.to_dict(), indent=2)
        respo = json.loads(ResponseMsg)
        print(respo)
        
        receivedMsg = respo.get('Body')
        
        if receivedMsg == 'Ola' or receivedMsg == 'ola' or receivedMsg == 'Hi' or receivedMsg == 'hi':
            session()
            message = watsonAssistant('')
            resp = MessagingResponse()
            resp.message(message)
            return str(resp)

        if respo.get('MediaContentType0') == 'audio/ogg':
            audio_url = respo.get('MediaUrl0')
            
            res = requests.get(audio_url)
            with open(filePath+"input.ogg", "wb") as o:
                o.write(res.content)
            
            transcript = speechtoText()
            message = watsonAssistant(transcript)
            resp = MessagingResponse()
            resp.message(message)
            return str(resp)

        if respo.get('Body') == 'Test':
            message = "If you are able to get this message then the application works"
            resp = MessagingResponse()
            resp.message(message)
            return str(resp)

        message = watsonAssistant(receivedMsg)
        resp = MessagingResponse()
        resp.message(message)
        return str(resp)

@app.route('/storeTwilioCredentials', methods=['POST'])
def storeTwilioCredentials():
    receivedPayload = json.loads(request.get_data())

    data = {
        "account_sid": receivedPayload.get('account_sid'),
        "auth_token": receivedPayload.get('auth_token')
    }
    
    with open('twiliocredentials.json', 'w') as fs:
        json.dump(data, fs, indent=2)

    return jsonify({"status": "Configured"})

@app.route('/getTwilioCredentials', methods=['GET'])
def getTwilioCredentials():
    try:
        with open('twiliocredentials.json') as creds:
            twiliocreds = json.loads(creds.read())
        twiliocreds.get('auth_token')
        return jsonify({"status": "Configured"})
    except:
        return jsonify({"status": "Not Configured"})

@app.route('/storeWaCredentials', methods=['POST'])
def storeWaCredentials():
    receivedPayload = json.loads(request.get_data())

    data = {
        "apikey": receivedPayload.get('wa_apikey'),
        "assistant-id": receivedPayload.get('wa_assistant_id'),
        "url": receivedPayload.get('wa_url')
    }
    
    with open('watsonassistant.json', 'w') as fs:
        json.dump(data, fs, indent=2)

    return jsonify({"status": "Configured"})

@app.route('/getWaCredentials', methods=['GET'])
def getWaCredentials():
    try:
        with open('watsonassistant.json') as creds:
            wacreds = json.loads(creds.read())
        wacreds.get('apikey')
        return jsonify({"status": "Configured"})
    except:
        return jsonify({"status": "Not Configured"})

@app.route('/storeSttCredentials', methods=['POST'])
def storeSttCredentials():
    receivedPayload = json.loads(request.get_data())

    data = {
        "apikey": receivedPayload.get('stt_apikey'),
        "url": receivedPayload.get('stt_url')
    }
    
    with open('speechtotext.json', 'w') as fs:
        json.dump(data, fs, indent=2)

    return jsonify({"status": "Configured"})

@app.route('/getSttCredentials', methods=['GET'])
def getSttCredentials():
    try:
        with open('speechtotext.json') as creds:
            sttcreds = json.loads(creds.read())
        sttcreds.get('apikey')
        return jsonify({"status": "Configured"})
    except:
        return jsonify({"status": "Not Configured"})


''' Start the Server '''

port = os.getenv('VCAP_APP_PORT', '8080')
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=port)