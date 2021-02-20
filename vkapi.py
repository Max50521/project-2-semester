import vk
import json
import requests
# my id 218576668  478809761
user_id = 478809761
a = "845407d3de9e28a28f7ba3e21689f40b92305eb6ebe297b6dd76839bcf38ff872ab78cc27f4a575da6210"
r=requests.get("https://api.vk.com/method/friends.get", params={  #r=requests.get("https://api.vk.com/method/friends.get"
    "user_id" : user_id,
    "order": "name",
    "count": 100,
    "offset": 0,
    "fields": "nickname, domain, sex, bdate, city, education, online, relation, last_seen",
    "access_token" :a,
    "v":5.122 #5.130
}).json["response"]["items"]

with open("friends.json",'w') as f:
    f.write(json.dumps(r))
f.close()
