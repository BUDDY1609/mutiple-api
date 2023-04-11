import re
import os
import random
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

api_key = os.environ.get('API_KEY_1', 'jbafu/gnbjsbjdbg/febfsb').split('/')
API = (random.choice(api_key))
print(API)
