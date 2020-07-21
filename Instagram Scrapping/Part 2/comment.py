from pip._vendor.requests import get
import json, time

url = 'https://www.instagram.com/graphql/query/'

short_code = 'CCg2Nb3DK7P'

end_cursor = None

count = 0

counterfile = 1
while 1:
    varibles = {
        "shortcode": short_code,
        "first": 50,
        "after": end_cursor
    }

    params = {
        'query_hash': 'bc3296d1ce80a24b1b6e40b1e72903f5',
        'variables': json.dumps(varibles)
    }

    r = get(url, params=params).json()

    try:
        users = r['data']['shortcode_media']['edge_media_to_parent_comment']['edges']
    except:
        print('Wait for 20 sec !')
        time.sleep(20)
        continue

    for user in users:
        username = user['node']['owner']['username']
        text = user['node']['text']
        count +=1
        print(f'{count} || {username} || {text}')
    end_cursor = r['data']['shortcode_media']['edge_media_to_parent_comment']['page_info']['end_cursor']
    has_next_page = r['data']['shortcode_media']['edge_media_to_parent_comment']['page_info']['has_next_page']
    if has_next_page == False: break
    time.sleep(2)