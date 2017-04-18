# alexa_iapyx
An Alexa Skill to control Iapyx on an Internet Button

## Setup
1. Create a Python 2.7.x virtual environment
    - `virtualenv -p /path/to/python venv`
2. Activate the Virtual Environment
    - `. venv/bin/active`
3. Install "requests"
    - `pip install requests`
4. Create a file named `secrets.py` with these contents (See `secrets.py.dist`):

        # Particle Device ID
        DEVICE_ID = "YOUR_PARTICLE_DEVICE_ID"

        # A Particle Cloud Access Token
        # See `bin/particle_token.py`
        ACCESS_TOKEN = "VALID_PARTICLE_ACCESS_TOKEN"

        # Amazon Skill Application ID
        APPLICATION_ID = "YOUR_ASK_APPLICATION_ID"
5. Test
    - `make test`

## Packaging for AWS Lambda
1. Build the package (zip file)
    - `make package`
2. Upload to Lambda via AWS Console
