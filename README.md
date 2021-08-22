# NicehashRigstarter
I'm trying to code a python script that allows me to start my Nicehash mining rig

Hello there, I was trying to code a python script that allows me to start my mining Rig for automation purposes. The overall process seemed easy, just send a POST request and sign it with the headers. Then I realized that the XAuth header needed the API key and an encrypted HASH that confirmes the authenticity of the request. Doing so and getting help from the official GitHub code from Nicehash I was able to code the following script. I am still unsure whether the query field in the message has to be empty or not since POST requests don't have a query, do they?
