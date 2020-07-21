from pip._vendor.requests import get
import json
import time

url = 'https://www.instagram.com/graphql/query/'

short_code = input('Enter a shortcode :')

end_cursor = None

count = 0
while 1:
    varibles = {
        "shortcode":short_code,
        "first":50,
        "after": end_cursor
    }

    params = {
        'query_hash': 'd5d763b1e2acf209d62d22d184488e57',
        'variables': json.dumps(varibles)
    }

    r = get(url, params=params).json()

    try: users = r['data']['shortcode_media']['edge_liked_by']['edges']
    except:
        print('Wait for 20 sec !')
        time.sleep(20)
        continue

    for user in users:
        username = user['node']['username']
        fullname = user['node']['full_name']
        profile_pic = user['node']['profile_pic_url']
        count +=1
        print(f'{count} || {username} || {fullname} || {profile_pic}')

    end_cursor = r['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor']
    has_next_page = r['data']['shortcode_media']['edge_liked_by']['page_info']['has_next_page']
    if has_next_page == False: break
    time.sleep(2)