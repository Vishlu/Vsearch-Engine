# times of india
# international business
# latest stories
from bs4 import BeautifulSoup
import requests

bus_url = "https://timesofindia.indiatimes.com/business/international-business"

response = requests.get(bus_url)

all_post_data = []

if response.status_code == 200:

	soup = BeautifulSoup(response.text, "html.parser")
	all_common_span = soup.find_all("span", attrs={"class": "w_tle"})

	for each_post in all_common_span:
		url = each_post.find('a').get('href')
		text = each_post.find('a').text
		
		all_post_data.append((url, text))

		context = {
			"link": url,
			"desc": text 
		}

		for u, t in context.items():
			print(u + " : " + t)
		print(len(all_post_data))
	
else:
	print("Website is no available")