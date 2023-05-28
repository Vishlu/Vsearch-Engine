# economictimes 
# agriculture
from bs4 import BeautifulSoup
import requests

agi_url = "https://economictimes.indiatimes.com/news/economy/agriculture"
response = requests.get(agi_url)

all_agi_data = []

if response.status_code == 200:
	soup = BeautifulSoup(response.content, "html.parser")
	common_agi_posts = soup.find_all('div', attrs={"class": "eachStory"}) 

	for each_agi in common_agi_posts:
		img = each_agi.find('img', class_="lazy").get('data-original')
		link = each_agi.find('a').get('href')
		title = each_agi.find('h3').text
		time = each_agi.find('time', class_="date-format").text
		para = each_agi.find('p').text

		all_agi_data.append((img, link, title, time, para))

		context = {
			'img' : img,
			'link' : link,
			'title' : title,
			'time' : time,
			'para' : para
		}

		for k, v in context.items():
			print(k + " : " + v)
		print(len(all_agi_data))