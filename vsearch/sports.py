# indianexpress
# sports
from bs4 import BeautifulSoup
import requests

news_url = "https://indianexpress.com/section/sports/"
response = requests.get(news_url)

all_data = []

if response.status_code == 200:
	soup = BeautifulSoup(response.content, "html.parser")
	common_division = soup.find_all('div', attrs={"class": "articles"})
	for each_contain in common_division:
		img = each_contain.find('img', class_="attachment-thumbnail size-thumbnail wp-post-image").get('data-lazy-srcset')
		url = each_contain.find('a').get('href')
		title = each_contain.find('h2', attrs={"class": "title"}).text
		date = each_contain.find('div', attrs={"class": "date"}).text
		desc = each_contain.find('p').text
		print("___________________________________________________")

		all_data.append((img, title, url, date, desc))
		
		context = {
			"img": img,
			"title": title,
			"url": url,
			"date": date,
			"desc": desc
		}

		for key, dic in context.items():
			print(key, " : ", dic) 
			print()
		num_item = len(all_data)
		print(num_item)
else:
	print("Not Found Out")

