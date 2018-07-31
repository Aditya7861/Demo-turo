import requests
from subprocess import Popen , PIPE
from bs4 import BeautifulSoup

url = "http://m.cricbuzz.com/"

data = requests.get(url);

soup = BeautifulSoup(data.content,'html.parser')

mydivs = soup.findAll('span', {"class": "cbz-ui-home-scores cbz-common-match"})

score = mydivs[0].get_text()

# print(score)

process = Popen(['notify-send', score ], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()

