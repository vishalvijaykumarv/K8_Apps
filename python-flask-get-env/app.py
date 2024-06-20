import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    HOSTNAME = os.getenv("HOSTNAME", "Unknown")
    POD_NAME = os.getenv("POD_NAME", "Unknown")
    return f'responce from flask app :- HOSTNAME={HOSTNAME} & POD_NAME={POD_NAME}'

@app.route('/env-list')
def all_env():
    # Get all environment variables
    all_env_vars = os.environ
    env_vars_str = "<br>".join([f"{key}: {value}" for key, value in all_env_vars.items()])
    return f'All Environment Variables:<br>{env_vars_str}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
