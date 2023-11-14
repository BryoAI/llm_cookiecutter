import requests
import json

from flask import Flask, redirect, url_for, request, render_template

import llama


app = Flask(__name__)
llm = llama.Llama()

@app.route('/')
def hello_world():
    return 'Welcome to Bryo hosted LLM!'

@app.route('/askai', methods=['POST'])
def webhook():
    if request.method == 'POST':
        json_payload = request.data.decode("utf-8")
        payload = json.loads(json_payload)
        security_token = payload.get('security_token')
        if security_token not in ['bryo_access_control_1']:
            return "please verify security token"
        question_string = f"Q: {payload.get('question')} A: "
        return llm.query(question_string)

    else:
        return f"Method not allowed: {request.method}"
