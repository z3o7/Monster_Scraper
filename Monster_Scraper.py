import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy
import openpyxl

def scrape_all(ln):
    job_list = []
    for b in range(0, ln):
        for page in range(1, 401):
            url = link_info['Links'][b]
            url = url[29:-5] + '-'
            url = 'https://www.monsterindia.com/search/' + url + str(page) + '?'
            print(url)
            response = requests.get(url)
            data = response.text
            soup = BeautifulSoup(data, 'html.parser')
            data = soup.find_all('div', attrs={"class":"card-panel apply-panel job-apply-card"})
            if data == []:
                break
            x = ''
            for i in data:
                tmp = {}

                tmp['job-catagory'] = link_info['Jobs'][b]
                try:
                    x = i.find('h3', attrs={'class':"medium"}).text
                except:
                    x ='-'
                x = ' '.join(x.split())
                x = x.replace("\n", "")
                tmp['job-tittle'] = x

                try:
                    x = i.find('span', attrs={'class':"company-name"}).text
                except:
                    x ='-'
                x = ' '.join(x.split())
                x = x.replace("\n", "")
                tmp['company-name'] = x

                try:
                    x = i.find('div', attrs={'class':'col-xxs-12 col-sm-5 text-ellipsis'}).text
                except:
                    x ='-'
                x = ' '.join(x.split())
                x = x.replace("\n", "")
                tmp['city'] = x

                try:
                    x = i.find('div', attrs={'class':'exp col-xxs-12 col-sm-3 text-ellipsis'}).text
                except:
                    x ='-'
                x = ' '.join(x.split())
                x = x.replace("\n", "")
                tmp['experience'] = x

                try:
                    x = i.find('div', attrs={'class':'package col-xxs-12 col-sm-4 text-ellipsis'}).text
                except:
                    x ='-'
                x = ' '.join(x.split())
                x = x.replace("\n", "")
                tmp['package'] = x

                try:
                    x = i.find('p', attrs={'class':"job-descrip"}).text
                except:
                    x ='-'
                x = ' '.join(x.split())
                x = x.replace("\n", "")
                x = x.replace("<br>", "")
                tmp['job-description'] = x

                try:
                    x = i.find('p', attrs={'class':"descrip-skills"}).text
                except:
                    x ='-'
                x = ' '.join(x.split())
                x = x.replace("\n", "")
                x = x.replace("Skills : ", "")
                tmp['job-skills'] = x

                try:
                    x = i.find('span', attrs={'class':"posted"}).text
                except:
                    x ='-'
                x = ' '.join(x.split())
                x = x.replace("\n", "")
                x = x.replace("Posted: ", "")
                tmp['job-posted'] = x

                x = ''
                job_list.append(tmp)
    job_le = pd.DataFrame(job_list)
    job_le.to_excel(r'job_list1.xlsx')
    return('done')


def scrape_selctd(index):
    job_list = []
    for page in range(1, 401):
        url = link_info['Links'][index]
        url = url[29:-5] + '-'
        url = 'https://www.monsterindia.com/search/' + url + str(page) + '?'
        print(url)
        response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')
        data = soup.find_all('div', attrs={"class":"card-panel apply-panel job-apply-card"})
        if data == []:
            break
        x = ''
        for i in data:
            tmp = {}

            tmp['job-catagory'] = link_info['Jobs'][index]
            try:
                x = i.find('h3', attrs={'class':"medium"}).text
            except:
                x ='-'
            x = ' '.join(x.split())
            x = x.replace("\n", "")
            tmp['job-tittle'] = x

            try:
                x = i.find('span', attrs={'class':"company-name"}).text
            except:
                x ='-'
            x = ' '.join(x.split())
            x = x.replace("\n", "")
            tmp['company-name'] = x

            try:
                x = i.find('div', attrs={'class':'col-xxs-12 col-sm-5 text-ellipsis'}).text
            except:
                x ='-'
            x = ' '.join(x.split())
            x = x.replace("\n", "")
            tmp['city'] = x

            try:
                x = i.find('div', attrs={'class':'exp col-xxs-12 col-sm-3 text-ellipsis'}).text
            except:
                x ='-'
            x = ' '.join(x.split())
            x = x.replace("\n", "")
            tmp['experience'] = x

            try:
                x = i.find('div', attrs={'class':'package col-xxs-12 col-sm-4 text-ellipsis'}).text
            except:
                x ='-'
            x = ' '.join(x.split())
            x = x.replace("\n", "")
            tmp['package'] = x

            try:
                x = i.find('p', attrs={'class':"job-descrip"}).text
            except:
                x ='-'
            x = ' '.join(x.split())
            x = x.replace("\n", "")
            x = x.replace("<br>", "")
            tmp['job-description'] = x

            try:
                x = i.find('p', attrs={'class':"descrip-skills"}).text
            except:
                x ='-'
            x = ' '.join(x.split())
            x = x.replace("\n", "")
            x = x.replace("Skills : ", "")
            tmp['job-skills'] = x

            try:
                x = i.find('span', attrs={'class':"posted"}).text
            except:
                x ='-'
            x = ' '.join(x.split())
            x = x.replace("\n", "")
            x = x.replace("Posted: ", "")
            tmp['job-posted'] = x

            x = ''
            job_list.append(tmp)
    job_le = pd.DataFrame(job_list)
    job_le.to_excel(r'job_list.xlsx')
    return('done')

url = 'https://www.monsterindia.com/jobs-by-skill.html'
response = requests.get(url)
data = response.text
soup_1 = BeautifulSoup(data, 'html.parser')
data_1 = soup_1.find_all('a',attrs={'class':'ar_lnk'})
url_list = []
for info in data_1:
    url_dict = {}
    url_dict['Jobs'] = info.text
    url_dict['Links'] = 'https:' + info.get('href')
    url_list.append(url_dict)
link_info = pd.DataFrame(url_list)
link_info.to_excel(r'jobs_links.xlsx')
lng = len(url_list)
print('[A] for scraping whole catagory\n[S] for scraping selected website')
c = input('Enter ur Choice : ')
c = c.lower()
if c == 'a':
    print(scrape_all(lng))
elif c == 's':
    catg = input('enter ur catogory : ')
    ar = numpy.array(link_info)
    ar = numpy.where(ar==catg)
    ar = list(ar) 
    indx = int(str(ar[0])[1:-1])
    print(scrape_selctd(indx))
