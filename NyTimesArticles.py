"""from bs4 import BeautifulSoup
import requests
#url = raw_input("put in url please (https://www.nytimes.com/)")
url ='https://www.nytimes.com/'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)
for link in soup.find_all('a'):
	print(link.get('href'))"""


import requests
from bs4 import BeautifulSoup
base_url ="https://www.nytimes.com/"
#base_url = input("what website do you wish to acquire links from")  
r = requests.get(base_url)
soup = BeautifulSoup(r.text , "lxml")
articles = ""
for story_heading in soup.find_all(class_= 'story-heading'):
	print(story_heading.a)
	articles += " \n" + str(story_heading.a)
	
	
open_file = open("article_list.txt",'w')
open_file.write(articles)
open_file.close()
	
print("\nthere is also a copy of this in a file named \"article list\" beware however that running this program will rewrite that file every time this program is run")
