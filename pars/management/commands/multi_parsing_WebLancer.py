from django.core.management.base import BaseCommand
from pars.models import Fl

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from random import choice
from random import uniform
from time import sleep
import time
import re
from multiprocess import Pool




def get_html(url, useragent=None, proxy=None):
    r = requests.get(url, headers=useragent, proxies=proxy, timeout=7)
    if r.ok:
        return r.text
    else:
        print('--*----------', r.status_code, '-----------*--')


def get_urls_pars(html):
    soup = BeautifulSoup(html, 'lxml')
    web = soup.find_all('div', class_="row")
    # print(web)
    # print('--*-- Найдено', len(web), 'элементов --*--')
    for index, i in enumerate(web):
        try:
            show = i.find('a', class_="text-bold show_visited").text.strip()
            date = i.find('span', class_="time_ago").get('title')
            status = i.find('span', class_="text-muted").text.strip()
            status_2 = i.find('div', class_="float-left float-sm-none text_field").text.strip()
            field = i.find('p', class_="text_field").text.strip()
            url = i.find('a', class_="text-bold show_visited").get('href')
        except:
            show = '-'
            date = '-'
            status = '-'
            status_2 = '-'
            field = '-'
            url = '-'


        strings = ['Спарсить', 'спарсить', 'Парсинг', 'парсинг', 'Парсер', 'парсер']
        for string in strings:
            match = re.search(string, show)
            if match:
                # print('Порядковый номер:', index+1)
                # print('show', show)
                # print('date', date)
                # print('status', status)
                # print('status_2', status_2)
                # print('field', field)
                # print('url', 'https://www.weblancer.net' + url)

                link = ('https://www.weblancer.net' + url)
                ref_link = field
                date_p1 = refind_w(date)
                time_p = refind_t(date)
                date_y = refind_name_y(date_p1)
                date_m = refind_name_m(date_p1)
                date_d = refind_name_d(date_p1)
                date_p = date_y + '-' + date_m + '-' + date_d
                price = 'По договорённости'
                image = 'images/weblancer.png'

                try:
                    p = Fl.objects.get(link=link)
                    p.show = show
                    p.price = price
                    p.ref_link = ref_link
                    p.date_p = date_p
                    p.time_p = time_p
                    p.save()
                except Fl.DoesNotExist:
                    p = Fl(
                        link=link,
                        show=show,
                        price = price,
                        ref_link = ref_link,
                        date_p = date_p,
                        time_p = time_p,
                        image = image,
                        ).save()
                    print(link)


def refind_name_d(s):
    return s.split('.')[0]

def refind_name_y(s):
    return s.split('.')[2]

def refind_name_m(s):
    return s.split('.')[1]

def refind_w(string):
    return re.search(r'\d\d.\d\d.\d{4}', string)[0]


def refind_t(string):
    return re.search(r'\d\d:\d\d', string)[0]



def make_all(url):
    useragents = open('txt/list_useragents_1824_i_e.txt').read().split('\n')
    proxies = open('txt/proxies_new_ipv4.txt').read().split('\n')
    try:
        try:    
            try:
                try:
                    try:
                        try:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                        except:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                    except:
                        try:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                        except:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                except:
                    try:
                        try:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                        except:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                    except:
                        try:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                        except:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
            except:
                try:
                    try:
                        try:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                        except:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                    except:
                        try:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                        except:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                except:
                    try:
                        try:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                        except:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                    except:
                        try:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                        except:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
        except:
            try:
                try:
                    try:
                        try:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                        except:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                    except:
                        try:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                        except:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                except:
                    try:
                        try:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                        except:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                    except:
                        try:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                        except:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
            except:
                try:
                    try:
                        try:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                        except:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                    except:
                        try:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                        except:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                except:
                    try:
                        try:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                        except:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                    except:
                        try:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
                        except:
                            proxy = {'https': 'https://' + choice(proxies)}
                            useragent = {'User-Agent': choice(useragents)}
                            html = get_html(url, useragent, proxy)
                            data = get_urls_pars(html)
    except:
        print('--------Except continue---------')

class Command(BaseCommand):
    help = 'Парсинг Fl'

    def handle(self, *args, **options):
        start = datetime.now()

        all_links = []
        url = 'https://www.weblancer.net/jobs/'
        html = get_html(url)
        soup = BeautifulSoup(html, 'lxml')
        url_finish = soup.find('div', class_="col-1 col-sm-2 text-right").find('a').get('href')
        url_finish_q = url_finish.split('=')[-1]
        pattern = 'https://www.weblancer.net/jobs/?page={}'
        for index, i in enumerate(range(1, int(url_finish_q)-70)):
            url = pattern.format(str(i))
            all_links.append(url)
            # print('---', 'Номер страници', index+1, '---')
        # print(all_links)
        with Pool(20) as q:
            q.map(make_all, all_links)

        end = datetime.now()
        f = end - start
        print("Full Parsing WebLancer:", f)
        print("--------------------------------------------------")