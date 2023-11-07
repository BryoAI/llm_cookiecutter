import requests
import json
from flask import Flask, redirect, url_for, request, render_template
from llm import llama


app = Flask(__name__)
llm = llama()

@app.route('/')
def hello_world():
    return 'Welcome to Bryo hosted LLM!'

@app.route('/askai', methods=['POST'])
def webhook():
    if request.method == 'POST':
        payload = request.data.decode("utf-8")
        payload = json.loads(payload)
        security_token = payload.get('security_token')
        if security_token in ['bryo_access_control_1']:
            question_string = "Q: {} A: ".format(payload.get('question'))
            return llm.llm(question_string)
        else:
            return "please verify security token"
