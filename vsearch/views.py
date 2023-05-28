from http.client import HTTPResponse
from telnetlib import STATUS
from django.shortcuts import redirect, render, HttpResponseRedirect
from bs4 import BeautifulSoup
import requests


def home_search(request):
    if request.method == "POST":
        user = request.POST.get("user-input")
        url = "https://www.ask.com/web?q=" + user
        try:
            response = requests.get(url)
        except:
           pass
        else:
            try:
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    container = soup.find_all('div', attrs={"class": "PartialSearchResults-item"})
                    data_container = []

                        
                    for each in container:
                        ''' '''
                        container_url = each.find('a').get('href')
                        container_title = each.find(attrs={'class' : 'PartialSearchResults-item-title'}).text
                        container_desc = each.find(attrs={'class': 'PartialSearchResults-item-abstract'}).text
                        data_container.append((container_url, container_title, container_desc))
                        # print(data_container)

                        context_json = {
                            'url' : container_url, 
                            'title' : container_title,
                            'desc' : container_desc
                        }

                        for i,j in context_json.items():
                            # print(i+ ":"+ j)
                           ''' '''
                        
                        
                    num = len(data_container)
                    return render(request, "vsearch/web_data.html", {'data_container': data_container, 'num': num})
                            
                elif user == None and user == " ":
                    HttpResponseRedirect('Please Enter Some Data')
                    
            except Exception as http_error:
                HttpResponseRedirect("Your Search Result Found an Error", http_error)
            
                
    return render(request, "vsearch/search_home.html")
    



def user_second_home_query(request):
    if request.method == "POST":
        user = request.POST.get("dynamic-input")
        url = "https://www.ask.com/web?q=" + user
        response = requests.get(url)
        try:
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                container = soup.find_all('div', attrs={"class": "PartialSearchResults-item"})
                data_container = []

                
                for each in container:
                    ''' '''
                    container_url = each.find('a').get('href')
                    container_title = each.find(attrs={'class' : 'PartialSearchResults-item-title'}).text
                    container_desc = each.find(attrs={'class': 'PartialSearchResults-item-abstract'}).text
                    data_container.append((container_url, container_title, container_desc))
                    # print(data_container)

                    context_json = {
                        'url' : container_url, 
                        'title' : container_title,
                        'desc' : container_desc
                    }

                    for i,j in context_json.items():
                        # print(i+ ":"+ j)
                        ''' '''

                num = len(data_container)
                return redirect(request, "vsearch/web_data.html", {'data_container': data_container, 'num': num})
                    
            # elif user == None and user == " ":
            #     print('Please Enter Some Data')
            
        except Exception as http_error:
            HttpResponseRedirect("Your Search Result Found an Error", http_error)

    return render(request, "vsearch/web_data.html")


def business_query(request):
    # times of india
    # international business
    # latest stories
    # from bs4 import BeautifulSoup
    # import requests

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
                '''' '''
                # print(u + " : " + t)
            stories_count = len(all_post_data)
        
    else:
        HttpResponseRedirect("Data is no available")
    return render(request, 'vsearch/business.html', {'business_stories': all_post_data, 'num_of_stories':stories_count})

def sports_query(request):
    
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
            # print("___________________________________________________")

            all_data.append((img, title, url, date, desc))
            
            context = {
                "img": img,
                "title": title,
                "url": url,
                "date": date,
                "desc": desc
            }

            for key, dic in context.items():
                ''' '''
                # print(key, " : ", dic) 
                # print()
            num_item = len(all_data)
            # print(num_item)
    else:
        HttpResponseRedirect("Not Found Out")
    return render(request, 'vsearch/sports.html', {'sports_data': all_data, "sport_count":num_item})

def education_query(request):
        
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
            

            all_post.append((img, title, desc, url, date))

            context = {
                'img': img,
                'title': title,
                'desc': desc,
                'url': url,
                'date': date
            }

            for i, j in context.items():
                ''' '''
                # print(i, " : " , j)
            ed_con = len(all_container)

    return render(request, 'vsearch/education.html', {'education_container': all_post, 'education_len':ed_con})

def agriculture_query(request):
            
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
                ''' '''
                # print(k + " : " + v)
            agi_count = len(all_agi_data)
    return render(request, 'vsearch/agriculture.html', {'agriculture_data': all_agi_data, 'agri_count':agi_count})
