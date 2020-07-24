import requests
import json, time, csv
from os.path import dirname, join

url = 'https://www.instagram.com/graphql/query/'

short_code = 'CCi_6vhsY45'

end_cursor = None

count = 0

counterfile = 1

jumlah_per_file = 1000

current_dir = dirname(__file__)
file_path = join(current_dir, "./hasil_like/")

writer = csv.writer(open('{}{} {}.csv'.format(file_path, short_code, counterfile), 'w', newline=''))
headers = ['User Name', 'Full Name', 'Profile Pic']
writer.writerow(headers)
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

    r = requests.get(url, params=params).json()

    try: users = r['data']['shortcode_media']['edge_liked_by']['edges']
    except:
        print('Wait for 20 sec !')
        time.sleep(20)
        continue

    for user in users:
        if count % jumlah_per_file == 0 and count!=0:
            counterfile +=1
            writer = csv.writer(open('{}{} {}.csv'.format(file_path, short_code, counterfile), 'w', newline=''))
            headers = ['User Name', 'Full Name', 'Profile Pic']
            writer.writerow(headers)
        username = user['node']['username']
        fullname = user['node']['full_name']
        profile_pic = user['node']['profile_pic_url']
        count +=1
        print(f'{count} || {username} || {fullname} || {profile_pic}')
        writer = csv.writer(open('{}{} {}.csv'.format(file_path, short_code, counterfile), 'a', newline='', encoding="utf-8"))
        data = [username, fullname, profile_pic]
        writer.writerow(data)

    end_cursor = r['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor']
    has_next_page = r['data']['shortcode_media']['edge_liked_by']['page_info']['has_next_page']
    if has_next_page == False: break
    time.sleep(2)