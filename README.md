# llm_cookiecutter
This repository provides a step-by-step guide for setting up and deploying open source language models, such as Llama, or proprietary language models like Vertex AI by Google. The code includes instructions for downloading and installing the Llama language model, Python functions for inference, and Flask APIs for exposing these language models through endpoints.

## Pre-requisites
- Python 3.7 or higher
- Pip package installer
- Access to a cloud platform or server for deployment

## Installation
1. Clone this repository
```
git clone git@github.com:BryoAI/llm_cookiecutter.git
```

2. Navigate to the repository
```
cd llm_cookiecutter
```

3. Install the required packages
```
pip install -r requirements.txt
```

## Language Model Deployment
1. Download the Llama language model
```
python download_llama.py
```

### Language Model Inference
1. Add your question to the `question.txt` file for batch inference
2. Run the inference script
```
python inference.py
```

### Language Model API
1. Run the Flask API
```
python3 api.py
```

2. Send a POST request to the API endpoint
```
curl -X POST http://YOUR_IP_ADDRESS:8000/llama -H "Content-Type: application/json" -d '{"question": "What is the capital of France?"}'
```

or use the `test_api.py` script
```
python test_api.py
```
The test_api.py uses requests to send a POST request to the API endpoint. The response is then printed to the console.








