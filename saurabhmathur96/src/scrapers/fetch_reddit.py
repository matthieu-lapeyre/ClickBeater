import requests
import tqdm
import time


def replace_first_line( src_filename, target_filename, replacement_line):
    f = open(src_filename)
    first_line, remainder = f.readline(), f.read()
    t = open(target_filename,"w")
    t.write(replacement_line + "\n")
    t.write(remainder)
    t.close()


BASE_URL = "https://www.reddit.com/r/savedyouaclick/hot.json"
DATA_FILE = "data/clickbait-top-reddit.txt"

params = {
    "sort": "hot",
    "after": ""
}
headers = {
    "User-agent": "clickbait-detector scraper"
}
titles = list()


with open(DATA_FILE, "r") as f:
    last_scrapping = float(f.readline().strip())

response = requests.get(BASE_URL, params=params, headers=headers)
response = response.json()
new_last_scrapping = response["data"]['children'][0]['data']['created_utc']

for i in tqdm.tqdm(range(20)):
    response = requests.get(BASE_URL, params=params, headers=headers)
    time.sleep(1)

    if response.status_code == 200:
        response = response.json()
        params["after"] = response["data"]["after"]
        
        for post in response["data"]["children"]:
            if float(post['data']['created_utc']) > last_scrapping:
                titles += [post["data"]["title"].split("|")[0].encode("ascii", "ignore")]
            else:
                break

print(len(titles), 'new clickbait titles added')

with open(DATA_FILE, "a") as outfile:
    outfile.write(b'\n'.join(titles).decode())

time.sleep(2)

replace_first_line(DATA_FILE, DATA_FILE, str(new_last_scrapping))
time.sleep(2)