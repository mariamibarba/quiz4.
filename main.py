import requests
import csv
from bs4 import BeautifulSoup
from time import sleep
from random import randint


f = open('Alta_all_product.csv', 'w', newline='\n')

f.write('Title, Price\n')
file_obj = csv.writer(f)
file_obj.writerow(['Title', 'Price'])
h = {'accept-Language': 'en-US'}
page = 1

while page < 5:
    url_laptops = f'https://alta.ge/index.php?subcats=Y&pcode_from_q=Y&pshort=Y&pfull=Y&pname=Y&pkeywords=Y&search_performed=Y&hint_q=%E1%83%9E%E1%83%A0%E1%83%9D%E1%83%93%E1%83%A3%E1%83%A5%E1%83%A2%E1%83%94%E1%83%91%E1%83%98%E1%83%A1+%E1%83%AB%E1%83%98%E1%83%94%E1%83%91%E1%83%90+&dispatch=products.search&page={str(page)}'
    r = requests.get(url_laptops, headers=h)
    content = r.text

    soup = BeautifulSoup(content, 'html.parser')

    all_product_block = soup.find('div', class_='grid-list')
    all_product = all_product_block.find_all(class_='ty-column3')


    for each in all_product:

        title = each.find('a', class_='product-title').text
        price = each.find('span', class_='ty-price-num').text
        # print(f'title:{title}')
        # print(f'price:{price}')
        file_obj.writerow([title, price])

    page += 1
    sleep(randint(15,25))

print('გილოცავთ თქვენ წარმატებით წამოიღეთ მონაცემები!')