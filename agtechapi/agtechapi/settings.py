import os.path
import sys

# secrets file exists in production, this is how we detect
if(os.path.isfile('/etc/config/secrets.json')):
    from agtechapi.production import *
else:
    from agtechapi.development import *