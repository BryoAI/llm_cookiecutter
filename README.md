# llm_cookiecutter
## Maintained by Bryo (www.bryo.io)
contact: info@bryo.io
<br>
linkedin: https://www.linkedin.com/company/bryo-ai

This repository provides a step-by-step guide for setting up and deploying open source language models, such as Llama, or proprietary language models like Vertex AI by Google. The code includes instructions for downloading and installing the Llama language model, Python functions for inference, and Flask APIs for exposing these language models through endpoints.

This cookiecutter is what bryo used to host its own language models for our Agents. You can checkout them here:
1. Bryo Customer Emails Agent: https://apps.odoo.com/apps/modules/16.0/client_communication_copilot/
2. Bryo Vendor Emails Agent: https://apps.odoo.com/apps/modules/16.0/lead_time_copilot/

## Pre-requisites
- Python 3.7 or higher
- Pip package installer
- Access to a cloud platform or server for deployment
- Gunicorn for serving the APIs. Install it using: https://docs.gunicorn.org/en/latest/install.html


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

[comment]: <> (## Language Model Deployment)
4. Download the Llama 2 language model, CPP version <br>
```
wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q6_K.gguf
```
Above LLM requires 9GB RAM atleast. For more models and their memory requirement check [TheBloke's](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF#provided-files) HuggingFace repo
### The CPU vs GPU debate
Running language models requires a lot of processing power, making GPUs ideal for running them. But we understand that our users won't always have access to these super expensive and rare GPUs. 

So the code in this repository makes it possible to run these language models in your laptops and servers without needed expensive GPUs.

These Language models require around 9GB of RAM(memory) to run and would consume around 6GB of your storage

Bryo recommends these configurations for running these models:
1. Running them Locally
```
Memory: 16GB, Storage for LLMs: 10GB
```

2. Running them on AWS
```
m4.2xlarge instance with 32GB RAM
```

### Language Model Inference (running locally)
1. Run the inference script
If you want to play with the language model in your personal system or get quick answers to some questions (works without internet access as well)
```
python inference.py
```

### Language Model API (serving)
The repository also gives you the code to serve the language model through an API endpoint. This is useful when you want to integrate the language model with your own applications or use it in production.
1. Spin up the GUnicorn server
```
gunicorn --bind 0.0.0.0:8000 wsgi:app --timeout 120
```
make sure 0.0.0.0 & port 8000 are free.

2. Send a POST request to the API endpoint
```
curl -X POST http://YOUR_IP_ADDRESS:8000/llama -H "Content-Type: application/json" -d '{"question": "What is the capital of France?"}'
```

or use the `test_api.py` script
```
python test_api.py
```
The test_api.py uses requests to send a POST request to the API endpoint. The response is then printed to the console.

## Use bryo hosted models
We have also hosted our own language models for our Agents. We use GPUs and a much more powerful version of the Llama model, that's mentioned above.
<br>
Bryo will be happy to help you setup your own language models. Or give to access to our hosted models.
You can reach out to us at: info@bryo.io






