from mastodon import Mastodon
import os
import csv

# Mastodon.create_app(
#     'mastofriends',
#     api_base_url = 'https://infosec.space',
#     to_file = 'pytooter_clientcred.secret'
# )

#mastodon = Mastodon(client_id = 'pytooter_clientcred.secret',)
#print(mastodon.auth_request_url())

# open the URL in the browser and paste the code you get
#mastodon.log_in(
#    code=input("Enter the OAuth authorization code: "),
#    to_file="pytooter_usercred.secret"
#)

#mastodon = Mastodon(access_token = 'pytooter_usercred.secret')

mastodon = Mastodon(api_base_url="https://infosec.space",access_token=os.environ["access_token"])
a = mastodon.me()["id"]
m = Mastodon.account_following(id=a,self=mastodon,limit=80)
with open('following_list.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    for i in m:
        data = [i.username, i.id, i.avatar_static]
        writer.writerow(data)
