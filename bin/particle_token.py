#!/usr/bin/env python
import requests
import argparse
import json

parser = argparse.ArgumentParser(
    description="Manage Your Particle Access Tokens."
)

# particle_token list|generate|delete|delete_all -u USERNAME -p PASSWD
# 
# * list
#     - username
#     - password
# * generate
#     - username
#     - password
#     - expires_in
# * delete
#     - username
#     - password
#     - token
# * delete_all (Delete all __PASSWORD_ONLY__ tokens)
#     - username
#     - password


parser.add_argument("command", help="Command to execute: list|generate|delete|delete_all")

parser.add_argument("-u", "--username", default=None, help="Particle Username")
parser.add_argument("-p", "--password", default=None, help="Particle Password")

parser.add_argument("-e", "--expires_in", default=0, help="How many seconds a generated tokes is valid for.")

parser.add_argument("-t", "--token", default=None, help="An Access Token to operate on.")

args = parser.parse_args()


def generate_token(args):
    '''POST https://api.particle.io/oauth/token -u particle:particle -d grant_type=password -d username=USER -d password=PASS -d expires_in=EXP'''
    
    token_info = {
        "grant_type": "password",
        "username": args.username,
        "password": args.password,
        "expires_in": args.expires_in
    }
    resp = requests.post("https://api.particle.io/oauth/token", auth=('particle','particle'), data=token_info)    
    resp.raise_for_status()
    
    return resp.text
    
    
def list_tokens(args):
    '''GET https://api.particle.io/v1/access_tokens -uUSER:PASS'''

    resp = requests.get("https://api.particle.io/v1/access_tokens", auth=(args.username, args.password))
    resp.raise_for_status()
        
    return resp.text

def delete_token(args):
    '''DEL https://api.particle.io/v1/access_tokens/TOKEN -uUSER:PASS'''
    
    if args.token == None:
        raise ValueError("Must specify a token to delete with -t|--token")
    
    resp = requests.delete("https://api.particle.io/v1/access_tokens/"+args.token, auth=(args.username, args.password))
    resp.raise_for_status()
    
    return resp.text
    
def delete_all_tokens(args):
    token_json = list_tokens(args)
    
    data = json.loads(token_json)

    for token in data:
        if token['client'] == '__PASSWORD_ONLY__':
            args.token = token['token']
            r_json = delete_token(args)
            result = json.loads(r_json)
            if result['ok'] != True:
                raise ValueError("Delete failed for '%s'." % (args.token))

    return "{ 'ok': true }"

# Main
actions = {
    "list": list_tokens,
    "generate": generate_token,
    "delete": delete_token,
    "delete_all": delete_all_tokens
}

if args.username == None or args.password == None:
    raise ValueError("Must specify 'username' and 'password'")
        
print(actions[args.command](args))
