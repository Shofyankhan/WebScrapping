from pip._vendor.requests import get
import json

url = 'https://www.instagram.com/graphql/query/'

short_code = input('Enter a shortcode :')

varibles = {"shortcode":short_code,"first":50}

params = {
    'query_hash': 'd5d763b1e2acf209d62d22d184488e57',
    'variables': json.dumps(varibles)
}

r = get(url, params=params).json()

users = r['data']['shortcode_media']['edge_liked_by']['edges']

count = 0
for user in users:
    username = user['node']['username']
    fullname = user['node']['full_name']
    profile_pic = user['node']['profile_pic_url']
    #print(username)
    count +=1
    print(count)
    print(f'{username} || {fullname} || {profile_pic}')
