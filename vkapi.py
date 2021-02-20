import vk
import json
import requests
# my id 218576668  478809761
user_id = 478809761
token = "845407d3de9e28a28f7ba3e21689f40b92305eb6ebe297b6dd76839bcf38ff872ab78cc27f4a575da6210"
version = 5.92
domain = "internetpasta"

response = requests.get('https://api.vk.com/method/wall.get',
             params = {    'domain':domain,
                           "access_token":token,
                           'v':version,
                      }
                        )
data = response.json()['response']['items']
filename='data'
myfile = open(filename, mode='w')
json.dump(data, myfile)
myfile.close()
#myfile=open(data,mode='r')
#vk_parsing=json.load(myfile)
