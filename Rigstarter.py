import requests
import hmac
from hashlib import sha256
import uuid
import json

# Enter you personal information here:
api_key = "*****"
api_secret = "*****"
org_id = "*****"
rig_id = "*****"

# Adding extra information for headers
time= requests.get("https://api2.nicehash.com/api/v2/time").json()
xtime = time["serverTime"]
xnonce = str(uuid.uuid4())

# Creating HMAC signature
message = bytearray(api_key, 'utf-8')
message += bytearray('\x00', 'utf-8')
message += bytearray(str(xtime), 'utf-8')
message += bytearray('\x00', 'utf-8')
message += bytearray(xnonce, 'utf-8')
message += bytearray('\x00', 'utf-8')
message += bytearray('\x00', 'utf-8')
message += bytearray(org_id, 'utf-8')
message += bytearray('\x00', 'utf-8')
message += bytearray('\x00', 'utf-8')
message += bytearray("POST", 'utf-8')
message += bytearray('\x00', 'utf-8')
message += bytearray("/main/api/v2/mining/rigs/status2", 'utf-8')
message += bytearray('\x00', 'utf-8')
message += bytearray('\x00', 'utf-8')
message += bytearray(str({"rigId": rig_id, "action": "START"}), 'utf-8')

HMAC_signature = hmac.new(bytearray(api_secret, 'utf-8'), message, sha256).hexdigest()

# Creating the headers
Headers = {
    'X-Time': str(xtime),
    'X-Nonce': xnonce,
    'X-Auth': api_key + ":" +  HMAC_signature,
    'X-Organization-Id': org_id,
    'X-Request-Id': str(uuid.uuid4())
    }

# Sending the finished request 
r = requests.post("https://api2.nicehash.com/main/api/v2/mining/rigs/status2", headers=Headers, json={"rigId": rig_id, "action": "START"})
print(r.text)
