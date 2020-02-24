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



def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        web = soup.find('div', class_="b-layout__txt b-layout__txt_padbot_20").text.strip()
        return web
    except:
        r = '**----------------------------**'
        return r

def get_all_links_2(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        w = soup.find('div', class_="b-layout__txt b-layout__txt_padbot_30").text.strip()
        return w
    except:
        r = '--Дата публикации отсутвтвует--'
        return r

def get_all_links_3(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        w = soup.find('span', class_="b-layout__bold").text.strip()

        # print(w)

        return w
    except:
        r = '--Price отсутвтвует--'
        return r


def get_urls_pars(html):
    soup = BeautifulSoup(html, 'lxml')
    web = soup.find('div', id="projects-list").find_all('div', class_="b-post")
    # print('--*-- Найдено', len(web), 'элементов --*--')
    for index, i in enumerate(web):
        show = i.find('a', class_="b-post__link").text
        url = i.find('a', class_="b-post__link").get('href')
        # ref_show = refind_show(show)
        
        
        strings = ['Django', 'django']
        for string in strings:
            match = re.search(string, show)
            if match:
                # print('Порядковый номер:', index+1)
                # print('show', show)
                # print('url', url)
                link = 'https://www.fl.ru' + url
                ref_link = refind_link(link)
                ref_link_2 = refind_link_2(link)
                ref_link_3 = refind_link_3(link)

                date_p1 = refind_w(ref_link_2)
                time_p = refind_t(ref_link_2)
                date_y = refind_name_y(date_p1)
                date_m = refind_name_m(date_p1)
                date_d = refind_name_d(date_p1)
                date_p = date_y + '-' + date_m + '-' + date_d
                # print('d', date_p)

                price = ref_link_3
                image = 'images/fl.png'

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
                        price=price,
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
    # a1 = a.replace(' ', '')
    # return a1.replace('\n', '')

def refind_t(string):
    return re.search(r'\d\d:\d\d', string)[0]


def refind_link(url):
    useragents = open('txt/list_useragents_1824_i_e.txt').read().split('\n')
    proxies = open('txt/proxies_new_ipv4.txt').read().split('\n')
    try:
        try:    
            try:
                try:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links(html)
                        # print(links)
                except:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links(html)
                        # print(links)         
            except:
                try:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links(html)
                        # print(links)
                except:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links(html)
                        # print(links)
        except:    
            try:
                try:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links(html)
                        # print(links)
                except:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links(html)
                        # print(links)         
            except:
                try:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links(html)
                        # print(links)
                except:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links(html)
                        # print(links)
    except:     
        print('**-get_all_links_NO_POWER_IN-**')
    return links

def refind_link_2(url):
    useragents = open('txt/list_useragents_1824_i_e.txt').read().split('\n')
    proxies = open('txt/proxies_new_ipv4.txt').read().split('\n')
    try:
        try:    
            try:
                try:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_2(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_2(html)
                        # print(links)
                except:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_2(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_2(html)
                        # print(links)         
            except:
                try:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_2(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_2(html)
                        # print(links)
                except:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_2(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_2(html)
                        # print(links)
        except:
            try:
                try:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_2(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_2(html)
                        # print(links)
                except:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_2(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_2(html)
                        # print(links)         
            except:
                try:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_2(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_2(html)
                        # print(links)
                except:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_2(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_2(html)
                        # print(links)

    except:     
        print('**-get_all_links_NO_POWER_IN2**')
    return links


def refind_link_3(url):
    useragents = open('txt/list_useragents_1824_i_e.txt').read().split('\n')
    proxies = open('txt/proxies_new_ipv4.txt').read().split('\n')
    try:
        try:    
            try:
                try:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_3(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_3(html)
                        # print(links)
                except:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_3(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_3(html)
                        # print(links)         
            except:
                try:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_3(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_3(html)
                        # print(links)
                except:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_3(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_3(html)
                        # print(links)
        except:
            try:
                try:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_3(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_3(html)
                        # print(links)
                except:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_3(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_3(html)
                        # print(links)         
            except:
                try:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_3(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_3(html)
                        # print(links)
                except:
                    try:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_3(html)
                        # print(links)
                    except:
                        proxy = {'https': 'https://' + choice(proxies)}
                        useragent = {'User-Agent': choice(useragents)}
                        html = get_html(url, useragent, proxy)
                        links = get_all_links_3(html)
                        # print(links)

    except:     
        print('**-get_all_links_NO_POWER_IN3**')
    return links


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
        pattern = 'https://www.fl.ru/projects/?page={}'
        for index, i in enumerate(range(1, 101)): # max 300
            url = pattern.format(str(i))
            all_links.append(url)
            # print('---', 'Номер страници', index+1, '---')
        # print(all_links)
        with Pool(50) as q:
            q.map(make_all, all_links)
        end = datetime.now()
        f = end - start
        print("Full Parsing Fl:", f)
        print("--------------------------------------------------")


