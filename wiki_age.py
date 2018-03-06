#This is my first Web Scraping Script to find 
#age of a person using wikipedia

import requests
from bs4 import BeautifulSoup

name=raw_input('Enter his name:-')
get_space_indices=name.find(" ")
new_name=name[:get_space_indices]+'_'+name[get_space_indices+1:]
#print(new_name)
url='https://en.wikipedia.org/wiki/{}'.format(new_name)

def parser():
	print(url)
	data=requests.get(url)
	#print(data)
	if data.status_code == 200:
		soup=BeautifulSoup(data.content,'lxml')
		first_para=soup.p.get_text()
		born_id=first_para.find('born')
		print(first_para[born_id:born_id+21])
		print(" ")
	else:
		print "No Name Found Please Try again"


parser()
