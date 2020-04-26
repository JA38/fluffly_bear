import requests
from bs4 import BeautifulSoup 
from note import extract_info

import csv
file = open("notes.csv", mode="w", newline='')
writer = csv.writer(file)
writer.writerow(['title','price','img_src','link'])

naver_html = requests.get('http://www.naver.com') #get:웹에서 배운것
#print(naver_html.text)
naver_soup = BeautifulSoup(naver_html.text, "html.parser") #parsing: 분석한다
#print(naver_soup) #그래도 딱히 naver_html.text랑 안다름


#노트크롤링 ; 4-- : Error 2--:잘 돌아갔구나 

note_html = requests.get('https://search.shopping.naver.com/search/all.nhn?pagingIndex=29&pagingSize=80&query=%EB%85%B8%ED%8A%B8')
#print(note_html.text)
note_soup = BeautifulSoup(note_html.text, "html.parser") #parsing: 분석한다
#print(note_soup)
note_list_box = note_soup.find("ul",{"class": "goods_list"} )
note_list = note_list_box.find_all("li",{"class":"_itemSection"})
#print(note_list)

#첫번째 상품 이름 보기
title = note_list[0].find("div", {"class": "tit"}).find("a").string
#print(title)

#첫번째 상품 가격 보기
price = note_list[0].find("span", {"class": "price"}).text.strip()
#print(price)
# string과 text의 차이?
#price = note_list[0].find("span", {"class": "price"}).string
#print(price) -> None이라고 뜸. 왜냐하면 string은 얘 안에 있는 문자열을 가져오는거  

#첫번째 상품 이미지 불러오기
img_src = note_list[0].find("img",{"class": "_productLazyImg"})['data-original']
#print(img_src)


#데이터를 하나로 묶어주자
note_info = {
    'title' : title,
    'price' : price
}
#print('노트 정보를 묶어봤다:',note_info) 


result = []
for note in note_list: #각각의 상품에 접근
    title = note.find("div", {"class": "tit"}).find("a").string
    price = note.find("span", {"class": "price"}).text.strip()
    note_info = {
        'title' : title,
        'price' : price
        }
    result.append(note_info)

#print(result)
#print('총 길이는:',len(result))

#print(extract_info(note_list))
#print(f'제목은 {title}, 가격은 {price}')

#what = note_list[0].find("div", {"class": "tit"}).find("a")['href']
#print(what)

final_result = []
for i in range (5):
    print(f'{i+1}번째 페이지를 크롤링 중,,,')
    note_html = requests.get(f'https://search.shopping.naver.com/search/all.nhn?pagingIndex={i+1}&pagingSize=80&query=%EB%85%B8%ED%8A%B8')
    note_soup = BeautifulSoup(note_html.text, "html.parser") #parsing: 분석한다
    note_list_box = note_soup.find("ul",{"class": "goods_list"} )
    note_list = note_list_box.find_all("li",{"class":"_itemSection"})
    result = extract_info(note_list) #이때 result 는 한페이지의 모든 상품
    final_result = final_result + result 

#print(final_result)

for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['price'])
    row.append(result['img_src'])
    row.append(result['link'])
    writer.writerow(row)

print('크롤링 끝')

#주석달기 ctrl k c  풀기 ctrl k u