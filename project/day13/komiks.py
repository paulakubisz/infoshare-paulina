import requests
import json
import os
from project.tools.pobieracz import pobierz

current = 'http://xkcd.com/info.0.json'
pattern = 'http://xkcd.com/{num}/info.0.json'
json_data = None

folder = os.path.join(os.getcwd(), 'comics')

def get_current_comic():
    global json_data
    response = requests.get(current)
    requests.raise_for_status()

    json_data = json.loads(response.text, encoding='utf-8')

    with open('currently.json', 'w') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)


def comic_link(url):
    response = requests.get(url)
    return json.loads(response.text)["img"]


def main():
    get_current_comic()
    pic_url = json_data["img"]
    pobierz(pic_url, 'komiks.png')

    last_comic_num = json_data["num"]

    if not os.path.exists(folder):
        os.mkdir(folder)


    for x in range(1,11):
        pic_link = comic_link(pattern.format(num=last_comic_num-x))
        pic_name = os.path.basename(pic_link)
        pic_path = os.path.join(folder, pic_name)

        pobierz(pic_link, pic_path)
        print("Zapisałam komiks r: ", x)
        print('Ścieżka zapisu: ', pic_path)

if __name__ == '__main__':

    main()