#Importing Beautifull Soup
from bs4 import BeautifulSoup
import requests
import time

print('Put some skill that you are unfamiliar with')
unfamiliar_skill=input(':')
print(f"Filtering Out:{unfamiliar_skill}")
def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    #print(html_text)
    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    #print(jobs)
    for index,job in enumerate(jobs):
        published_date=job.find('span',class_='sim-posted').span.text
        #print(published_date)
        if 'few' in published_date:
            company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            #print(company_name)
            skills=job.find('span',class_='srp-skills').text.replace(' ','')
            #print(skills)
            more_info=job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required Skills:{skills.strip()}\n")
                    f.write(f"More Info:{more_info}")

                    #print(f'''
                    #Company Name: {company_name}
                    #Required Skills:{skills}
                     #     ''')
                    print(f'File Saved:{index}')

if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=100
        print(f"Wating for {time_wait} minutes...")
        time.sleep(time_wait*60)