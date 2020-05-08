def extract_info(book_list):
    result = []
    for book in book_list: #각각의 상품에 접근
        title = book.find("dl").find("dt").find("a",{"class":"N=a:bta.title"}).string
        img_src = book.find("div",{"class":"thumb type_best"}).find("div",{"class":"thumb_type thumb_type2"}).find("a",{"class":"N=a:bta.thumb"}).find("img")['src']
        # img_src = book.find("div",{"class":"thumb type_best"})
        # if img_src != None:
        #     img_src = img_src.find("div",{"class":"thumb_type thumb_type2"}).find("a",{"class":"N=a:bta.thumb"}).find("img")['src']
        # else:
        #     img_src = '없음'
        page = book.find("div",{"class":"thumb type_best"}).find("div",{"class":"thumb_type thumb_type2"}).find("a",{"class":"N=a:bta.thumb"})['href']
        author = book.find("dl").find("a",{"class":"txt_name"}).text
        publisher = book.find("dl").find("a",{"class":"N=a:bta.publisher"}).text
        orig_price = book.find("dl").find("dd",{"class":"txt_desc"}).find("strike")
        if orig_price != None:
            orig_price = orig_price.text
        else:
            orig_price = '없음'
        sale_price =  book.find("dl").find("dd",{"class":"txt_desc"}).find("em",{"class":"price"})
        if sale_price != None:
            sale_price = sale_price.text
        else:
            sale_price = '없음'
        book_info = {
            'title' : title,
            'img_src' : img_src,
            'page' : page,
            'author': author,
            'publisher':publisher,
            'original price':orig_price,
            'sale price': sale_price
            }
        result.append(book_info)
    return result 


