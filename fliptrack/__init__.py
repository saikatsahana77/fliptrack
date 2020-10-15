import requests
from bs4 import BeautifulSoup
import re


class Fliptrack:

    def __init__(self, link):
        headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.wikipedia.org/',
            'Connection': 'keep-alive'
        }
        res = requests.get(link, headers=headers)
        soup = BeautifulSoup(res.text, 'lxml')
        self.soup = soup

    def price(self):
        prices = self.soup.find_all(text=re.compile('₹'))
        price_str = ""
        if prices[0][0] == "E":
            price_str = str(prices[1])
        else:
            price_str = str(prices[0])
        l = list(price_str.strip())
        for i in l:
            if (i.isdigit() == False):
                l.remove(i)
        price = "".join(l)
        price = int(price)
        return (price)

    def title(self):
        name = self.soup.find_all('span', {"class": "_35KyD6"})
        return (name[0].text)

    def rating(self):
        rating = self.soup.find_all('div', {"class": "hGSR34"})
        return (float(rating[0].text))

    def description(self):
        description = self.soup.find_all('div', {"class": "_3la3Fn _1zZOAc"})
        return (description[0].p.text)

    def mrp(self):
        mrp = self.soup.find_all('div', {"class": "_3auQ3N _1POkHg"})
        mrp_fin = 0
        mrp_str = ""
        if mrp != []:
            mrp_str = mrp[0].text
            l = list(mrp_str.strip())
            for i in l:
                if (i.isdigit() == False):
                    l.remove(i)
            mrp_fin = "".join(l)
            mrp_fin = int(mrp_fin)
            return (mrp_fin)
        else:
            return (-1)

    def discount(self):
        discount = self.soup.find_all('div', {"class": "VGWI6T _1iCvwn"})
        dis_fin = 0
        dis_str = ""
        if discount != []:
            dis_str = discount[0].span.text
            dis_fin = int("".join(list(dis_str[:2])))
            return (dis_fin)
        else:
            return (-1)

    def seller_name(self):
        seller_name = self.soup.find_all('div', {"id": "sellerName"})
        return (seller_name[0].span.span.text)

    def seller_ratings(self):
        seller_ratings = self.soup.find_all('div', {"id": "sellerName"})
        return (float(seller_ratings[0].span.div.text))

    def highlights(self):
        highlights = self.soup.find_all('li', {"class": "_2-riNZ"})
        h_arr = []
        for i in highlights:
            h_arr.append(i.text)
        return (h_arr)

    def ratings_star(self, k=6):
        ratings_star = self.soup.find_all('div', {"class": "CamDho"})
        r_arr = []
        for i in ratings_star:
            r_arr.append(i.text)
        if (k in range(1, 6)):
            x_1 = (r_arr[-k])
            x = list(x_1)
            for i in x:
                if (i.isdigit() == False):
                    x.remove(i)
            rating = "".join(x)
            rating = int(rating)
            return (rating)
        else:
            r_arr_rating = []
            for x_1 in r_arr:
                x = list(x_1)
                for i in x:
                    if (i.isdigit() == False):
                        x.remove(i)
                rating = "".join(x)
                rating = int(rating)
                r_arr_rating.append(rating)
            return (r_arr_rating)

    def ratings_cnt(self):
        ratings_cnt = self.soup.find_all('div', {"class": "row _2yc1Qo"})
        rate = ratings_cnt[0].div.span.text.strip()
        rate1 = re.sub('\D', '', rate)
        return (int(rate1))
    def reviews_cnt(self):
        review_cnt = self.soup.find_all('div', {"class": "row _2yc1Qo"})
        rev = review_cnt[1].div.span.text.strip()
        rev1 = re.sub('\D', '', rev)
        return (int(rev1))
