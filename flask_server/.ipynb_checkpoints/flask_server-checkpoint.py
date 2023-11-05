#import pandas
import requests
import json
from flask import Flask, redirect, url_for, request, render_template
from llm import llama


app = Flask(__name__)
llm = llama()

@app.route('/')
def hello_world():
    return render_template('chatbot.html')
    #return 'HELLO WORLD!'

@app.route('/askai', methods=['POST'])
def webhook():
    print("Data received from Webhook is: ", request.json)
    if request.method == 'POST':
        payload = request.data.decode("utf-8")
        payload = json.loads(payload)
        security_token = payload.get('security_token')
        if security_token in ['bryo_access_control_1']:
            question_string = payload.get('question')
            max_tokens = payload.get('max_tokens')
            stop = payload.get('stop')
            echo = payload.get('echo')
            output = llm.query_llm(question_string)
            return output
        else:
            print("wrong security token")
            return "incorrect security token"


#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8000, debug=True)
