import vk
access_token = "85f3dcef213096485f634ff73b99609a26205fc3f172eeb81a853ec6270a185e0a39c68b9db42eaa82d04"
session = vk.Session(access_token=access_token)
vk_api = vk.API(session)
count=10
vk_api.friends.get(users_id=478809761, v="5.130")
