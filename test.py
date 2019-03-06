import farmOS

hostname = ''
username = ''
password = ''

farm = farmOS.farmOS(hostname, username, password)
success = farm.authenticate()

if success:
    print('Authentication successful.')
    r = farm.httpRequest('farm.json')
    print(r.text)
else:
    print('Authentication failed.')
