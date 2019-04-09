import requests
import base64
import urllib.parse
from bs4 import BeautifulSoup

class Pcstore_crawler():
    def __init__(self, keyword):
        input_str = urllib.parse.quote(keyword)
        str_utf8 = input_str.encode("UTF-8")
        b_object = base64.b64encode(str_utf8)
        store_k_word = b_object.decode("utf-8") 
        self.url = "https://www.pcstore.com.tw/adm/psearch.htm?store_k_word="+store_k_word+"&slt_k_option=1&st_sort=1&page_count=60&s_page=1&stpa=_1__GraphWord_all_____2"
    def get_item_title(self):
        r = requests.get(self.url)
        r.encoding = 'big5'
        soup = BeautifulSoup(r.text, 'html.parser')
        divs = soup.findAll("div", {"class": "pic2t pic2t_bg"})
        result = []
        for div in divs:
            result.append(div.text)
        return result