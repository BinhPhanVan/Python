from os import umask
from re import A
import csv
import json
import requests
from bs4 import BeautifulSoup
url = "https://www.dienmayxanh.com/dong-ho-deo-tay"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
def get_info(url):
    reponse = requests.get(url, headers=headers)
    soup = BeautifulSoup(reponse.text,features="html.parser")
    return soup.find_all('li',class_="item")

def get_list_page(url):
    i=0
    arr=[]
    while get_info(url +"#c=7264&o=8&pi="+ str(i)) != [] : 
        arr.append(url +"#c=7264&o=8&pi="+ str(i))
        i+=1
        # chỉ lấy data 100 page đầu tiên
        if i==100:
            break
    return arr 
    
def get_all_data(url):
    data = []
    list_data = get_list_page(url)
    for url_child in list_data:
        items = get_info(url_child)
        items = get_info(url_child)
        for item in items:  
            new_item={
                "Url" : "https://www.dienmayxanh.com" + item.find('a').get('href'),
                "Name_item": edit_text(item.find(class_="fashionWatch-name").getText()),
                "Link_img": item.find(class_="thumb").get("data-src"),
                "Price": edit_text(item.find(class_="price").getText()),
                "Discount": edit_text(item.find(class_="percent").getText()),
                "Price_old": edit_text(item.find(class_="price-old").getText())
            }
            data.append(new_item)
    return data

def save_to_file_csv(data,  file):
    with open(f'{file}.csv', 'w', newline='', encoding="utf-8") as file:
        headers = ['Url', 'Name_item', 'Link_img','Price','Discount','Price_old']
        writer = csv.DictWriter(file, delimiter=',',lineterminator='\n', fieldnames=headers)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

def save_to_file_json(data,  file):
    with open(f"{file}.json", "w",encoding='utf-8') as f:
        json.dump(data, f, indent=2,ensure_ascii=False)

def edit_text(str):
    str = str.replace("\n", " ")
    str = str.replace("₫", " ")
    str = str.strip()
    str = " ".join(str.split(' '))
    return str

save_to_file_csv(get_all_data(url), 'clock_table')
save_to_file_json(get_all_data(url), 'clock_info')
save_to_file_json(get_list_page(url), 'list_page')

