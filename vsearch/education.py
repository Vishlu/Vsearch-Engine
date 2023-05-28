# indian express
# education news post
from bs4 import BeautifulSoup
import requests

edu_url = "https://indianexpress.com/section/education/"

response = requests.get(edu_url)

all_post = []

if response.status_code == 200:
	soup = BeautifulSoup(response.content, "html.parser")

	all_container = soup.find_all("div", attrs={"class": "articles"})

	for each_edu in all_container:
		img = each_edu.find('img', class_="attachment-thumbnail size-thumbnail wp-post-image").get('data-lazy-srcset')
		title = each_edu.find("h2", attrs={"class" : "title"}).text
		desc = each_edu.find('p').text
		url = each_edu.find('a').get('href')
		date = each_edu.find('div', attrs={"class" : "date"}).text
		print("____________________________________________________________________________")

		all_post.append((img, title, desc, url, date))

		context = {
			'img': img,
			'title': title,
			'desc': desc,
			'url': url,
			'date': date
		}

		for i, j in context.items():
			print(i, " : " , j)
		print(len(all_container))
