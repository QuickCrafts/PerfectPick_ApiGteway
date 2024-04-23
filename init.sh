## Python required

## Create Virtual Env
python3 -m venv venv
source venv/bin/activate # On Windows it should be .\venv\Scripts\activate

## Install required packages
pip install fastapi 'strawberry-graphql[debug-server]' "uvicorn[standard]" httpx pika