#Importing Necessary Libraries
from bs4 import BeautifulSoup
import requests
import csv 
import pandas as pd

#Flipkart URL which is going to be extracted
url="https://www.flipkart.com/wearable-smart-devices/smart-headphones/pr?sid=ajy%2Cvam&otracker=nmenu_sub_Electronics_0_Smart+Headphones&p%5B%5D=facets.usage%255B%255D%3DFitness%2B%2526%2BOutdoor"
response = requests.get(url).text
soup=BeautifulSoup(response,'lxml')
#print(soup.prettify)

#Taking a Sample
products=[]
offer_prices=[]
original_prices=[]
discounts=[]
ratings=[]
rating_counts=[]
product=soup.find('a',class_='s1Q9rs').text
offer_price=soup.find('div',attrs={'class':'_30jeq3'})
original_price=soup.find('div',attrs={'class':'_3I9_wc'})
discount=soup.find('div',attrs={'class':'_3Ay6Sb'})
rating=soup.find('div',attrs={'class':'_3LWZlK'})
rating_count=soup.find('span',attrs={'class':'_2_R_DZ'})
#print(product)
#print(offer_price.text)
#print(original_price.text)
#print(discount.text)
#print(rating.text)
#print(rating_count.text)

watches=soup.find_all('div',class_='_4ddWXP')
#print(watches)
for watch in watches:
    product=watch.find('a',class_='s1Q9rs').text
    offer_price=watch.find('div',class_='_30jeq3').text
    original_price=watch.find('div',class_='_3I9_wc').text
    discount=watch.find('div',attrs={'class':'_3Ay6Sb'}).text.replace(' off','')
    rating=watch.find('span',class_="_1lRcqv")
    rating_count=watch.find('span',class_='_2_R_DZ')
    products.append(product)
    offer_prices.append(offer_price)
    original_prices.append(original_price)
    discounts.append(discount)
    ratings.append(rating)
    rating_counts.append(rating_count)

df=pd.DataFrame({"Product Name":products,"Current Price":offer_price,"Orginal Price":original_prices,"Percent Offer":discounts,"Rating":ratings,"Rating Count":rating_counts})
#print(df.head())

#df['Rating']=df['Rating'].str.replace("<div class=\"_3LWZlK\">3.3<img class=\"_1wB99o\" src=\"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==\"/></div>", "0")
#print(df.Rating.head())
df['Rating Count']=df['Rating Count'].str.replace('(', '').replace(')','0')
print(df['Rating Count'].head())
df['Percent Offer']=df['Percent Offer'].str.replace(' off', '')
print(df['Percent Offer'].head())


df.head()
df.to_excel('watches1.xlsx')
print('DataFrame is written to Excel File successfully.')