import requests
from bs4 import BeautifulSoup 
from book import extract_info
import csv
file = open("naver_books.csv", mode="w", newline='')
writer = csv.writer(file)
writer.writerow(['title','img_src','page','author','publisher','original price','sale price'])

# # print(book_list)
# title = book_list[0].find("dl").find("a",{"class":"N=a:bta.title"}).string
# # print(title)
# author = book_list[0].find("dl").find("a",{"class":"txt_name"}).string
# # print(author)


# book_html = requests.get('https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page=1')
# book_soup = BeautifulSoup(book_html.text, "html.parser") #parsing: 분석한다
# book_list_box = book_soup.find("ol",{"class": "basic"} )
# book_list = book_list_box.find_all("li")
# orig_price = book_list[0].find("dl").find("dd",{"class":"txt_desc"}).find("strike").string
# print(orig_price)
# sale_price =  book_list[0].find("dl").find("dd",{"class":"txt_desc"}).find("em",{"class":"price"}).string
# print(sale_price)
# # publisher = book_list[0].find("dl").find("a",{"class":"N=a:bta.publisher"}).string
# # # print(publisher)
# # img_src = book_list[0].find("div",{"class":"thumb type_best"}).find("div",{"class":"thumb_type thumb_type2"}).find("a",{"class":"N=a:bta.thumb"}).find("img")['src']
# # # print(img_src)
# # page = book_list[0].find("div",{"class":"thumb type_best"}).find("div",{"class":"thumb_type thumb_type2"}).find("a",{"class":"N=a:bta.thumb"})['href']
# # print(page)

final_result = []
for i in range (1,8):
    print(f'{i+1}번째 페이지를 크롤링 중,,,')
    book_html = requests.get(f'https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page={i+1}')
    book_soup = BeautifulSoup(book_html.text, "html.parser") #parsing: 분석한다
    book_list_box = book_soup.find("ol",{"class": "basic"})
    book_list = book_list_box.find_all("li")
    result = extract_info(book_list) #이때 result 는 한페이지의 모든 상품
    final_result = final_result + result 

# i=0
# book_html = requests.get(f'https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page={i+1}')
# book_soup = BeautifulSoup(book_html.text, "html.parser") #parsing: 분석한다
# book_list_box = book_soup.find("ol",{"class": "basic"})
# book_list = book_list_box.find_all("li")
# print(book_list_box)
# print(book_list)
# print(len(book_list))
#(len(book_list))
# for t in range(len(book_list)):
#     print(f'book_list[{t}]번째는',book_list[t])

for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['img_src'])
    row.append(result['page'])
    row.append(result['author'])
    row.append(result['publisher'])
    row.append(result['original price'])
    row.append(result['sale price'])
    writer.writerow(row)

print('크롤링 끝')
