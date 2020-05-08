import requests
from bs4 import BeautifulSoup

hospital_html = requests.get('https://www.mohw.go.kr/react/popup_200128_3.html')
hospital_html.encoding = 'utf-8'

hospital_soup = BeautifulSoup(hospital_html.text, "html.parser")

# 이제부터 시도, 시군구, 선별진료소(이름), 전화번호 크롤링 후 csv 파일에 저장하시면 됩니다!155
hospital_list_box = hospital_soup.find("table",{"class": "tb_base corona"}).find("tbody",{"class":"tb_center"})
hospital_list = hospital_list_box.find_all("tr")
# print(len(hospital_list))
# print(hospital_list[0])

# hospital_list_row = hospital_list[0].find_all("td")
# city = hospital_list_row[0].text
# print(city)
# gu = hospital_list_row[1].text
# print(gu)
# name = hospital_list_row[2].text.replace('*(검체채취 가능)','').strip()
# print(name)
# phone_num = hospital_list_row[3].text
# print(phone_num)

import csv
file = open("corona_hospital.csv", mode="w", newline='')
writer = csv.writer(file)
writer.writerow(['시도','시군구','선별진료소(이름)','전화번호'])

corona_info_list = []
for i in range(len(hospital_list)):
    hospital_list_row = hospital_list[i].find_all("td")
    city = hospital_list_row[0].text
    gu = hospital_list_row[1].text
    name = hospital_list_row[2].text.replace('*(검체채취 가능)','').strip()
    phone_num = hospital_list_row[3].text
    corona_info = {
            'city':city,
            'gu' : gu,
            'name' : name,
            'phone_num': phone_num
            }
    corona_info_list.append(corona_info)


for corona_info in corona_info_list:
    row = []
    row.append(corona_info['city'])
    row.append(corona_info['gu'])
    row.append(corona_info['name'])
    row.append(corona_info['phone_num'])
    writer.writerow(row)


