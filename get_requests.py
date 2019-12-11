import requests

# build url
path_url =  'http://api.postcodes.io/postcodes/'
arguements = 'e146gt'

posts_codes = requests.get(path_url+arguements)

# print(type(posts_codes))

# turn this into a dictionary
dict_responce = posts_codes.json()
# print(dict_responce)

# getting out data
print(dict_responce.keys())

print(dict_responce['status']) # this will print the keys value.

print(dict_responce['result'])
print((dict_responce['result']).keys())
print(dict_responce['result']['admin_district']) # admin district is a key within the key result

for key in dict_responce['result']:
    print('key:', key)
    print(key, '-->', dict_responce['result'][key])