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


def get_all_links(html, url):
    # print('---**???***--- && ---***???**---')
    # print('url', url)
    soup = BeautifulSoup(html, 'lxml')
    try:
        tds = soup.find('div', class_="s_box").find('h1', class_="proj_tophead").text.strip()
        # print('show', tds)
        tds_z = soup.find('p', class_="txt href_me").text.strip()
    # ref_tds_z = refind_tds_z(tds_z)
    except:
        tds_z = '**-Для Бизнес-аккаунтов-**'
    try:
        tds_z_2 = soup.find('div', class_="s_box").find_all('tr')
        for index, t in enumerate(tds_z_2):
            if index == 0:
                td_1 = t.find('td').text.strip()
            # print(td_1)
            # if index == 1:
            # 	td_2 = t.find('td').find('p', class_="txt href_me").text.strip()
            # print(td_2)
            if index == 2:
                td_3 = t.find('td').text.strip()
            # print(td_3)
            if index == 3:
                td_4 = t.find('td').find('p', class_="txt href_me").text.strip()
            # print(td_4)

    # if td_3 == 'Пожаловаться':
    # 	tds_z_3 = td_1 + '\n' + tds_z
    # elif tdtu == 'Присоединенные файлы':
    # 	tds_z_3 = td_1 + '\n' + tds_z + '\n' + td_3 + '\n' + td_4 + '\n' + tdtu
    # else:
    # 	tds_z_3 = td_1 + '\n' + tds_z + '\n' + td_3 + '\n' + td_4

    except:
        tds_z_2 = '------'

    try:
        tds_z_u = soup.find('div', class_="s_box").find_all('tr')
        all_tds_z_u = []
        for index, t in enumerate(tds_z_u):
            if index == 4:
                try:
                    tdtu = t.find('td').find('h4').text.strip()
                except:
                    tdtu = '---------1////////'
                try:
                    tdnu = t.find('td').text.strip()
                except:
                    tdnu = '---------2////////'
                try:
                    tdu_1 = t.find('td').find_all('a')
                    for index, i in enumerate(tdu_1):
                        if index in [2, 5, 8, 11, 14, 17, 20]:
                            tdu = i.get('href')
                            all_tds_z_u.append(tdu)
                        # print(index, '++++++++++', tdu)
                except:
                    tdu_1 = '---------3////////'

            # print(tdtu)
            # print(tdnu)
    except:
        tds_z_u = '------'

    myString = '\n'.join(all_tds_z_u)
    # print('!!!', myString)

    if td_3 == 'Пожаловаться':
        tds_z_3 = td_1 + '\n\n' + tds_z
    elif tdtu == 'Присоединенные файлы':
        tds_z_3 = td_1 + '\n\n' + tds_z + '\n\n' + td_3 + '\n\n' + td_4 + '\n\n' + tdtu + '\n\n' + myString
    else:
        tds_z_3 = td_1 + '\n\n' + tds_z + '\n\n' + td_3 + '\n\n' + td_4

    # print('text', tds_z)
    # print('text_2', tds_z_3)
    if tds_z != '**-Для Бизнес-аккаунтов-**':
        prices = soup.find('div', class_="col-lg-12").find_all('tr')
        for index, p in enumerate(prices):
            if index == 0:
                price = p.find('td').find_next_sibling('td').text
            # print('price', price)
            if index == 3:
                date_1 = p.find('td').find_next_sibling('td').text
            # print('date_1', date_1)
            if index == 4:
                date_2 = p.find('td').find_next_sibling('td').text
            # print('date_2', date_2)

        link = url
        show = tds
        if date_1 != '':
            date_p = date_1.split(' ')[0]
            time_p = date_1.split(' ')[1]
        # print('date_1', date_1)
        else:
            date_p = date_2.split(' ')[0]
            time_p = date_2.split(' ')[1]
        # print('date_2', date_2)
        price = price
        image = 'images/freelance.png'
        if tds_z_3 != '':
            ref_link = tds_z_3
        else:
            ref_link = tds_z

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
                ref_link=ref_link,
                date_p=date_p,
                time_p=time_p,
                image=image,
            ).save()
            print('2 ', link)
    return tds_z


# except:
# 	r = '**-Для Бизнес-аккаунтов-**'
# 	return r


def refind_tds_z(a):
    a1 = a.replace('\t', '')
    return a1.replace('\r', '\n')


def get_urls_pars(html):
    # print('---**???***--- && ---***???**---')
    soup = BeautifulSoup(html, 'lxml')
    uas = soup.find('div', class_="projects")
    # print('--*-- Найдено', len(uas), 'элементов --*--')
    for index, ua in enumerate(uas):
        try:
            name = ua.find('div').text.strip()
        except:
            name = '- - - - -'
        try:
            name_2 = ua.find('a').get('href')
        except:
            name_2 = '- - - - -'
        try:
            name_3 = ua.find('li').text
        except:
            name_3 = '- - - - -'
        try:
            name_4 = ua.find('ul').find('i').text
        except:
            name_4 = '- - - - -'
        try:
            name_5 = ua.find('ul').text
            ref_name_5 = refind_name_5(name_5)
        except:
            name_5 = '- - - - -'
        try:
            name_6 = ua.find('ul').text.strip()
            ref_name_6 = refind_name_6(name_6)
        except:
            name_6 = '- - - - -'
        try:
            date_y = refind_name_y(name_3)
            date_m = refind_name_m(name_3)
            date_d = refind_name_d(name_3)
            ref_date = date_d + '.' + date_m + '.20' + date_y
            date_pub = '20' + date_y + '-' + date_m + '-' + date_d
        except:
            ref_date = '00000000000'

        # print('-------------- && --------------')

        # strings = ['Парсинг', 'парсинг', 'Парсер', 'парсер']
        # for string in strings:
        # 	match = re.search(string, name)
        # 	if match:
        # print('Порядковый номер:', index+1)
        link = 'https://freelance.ru' + name_2
        # link = 'https://freelance.ru/projects/dizajner-1166487.html'
        ref_link = refind_link(link)
    print('===', ref_link)

    print('Текст:', name)
    print('Дата:', date_pub)
    print('Ответов:', name_4)
    print('Просмотров:', ref_name_5)
    print('Вид:', ref_name_6)

    # if ref_link=='**-Для Бизнес-аккаунтов-**':
    # 	show = name
    # 	date_p = date_pub
    # 	time_p1 = str(datetime.now()).split(' ')[1]
    # 	time_p001 = time_p1.split('.')[0]
    # 	time_p01 = time_p001.split(':')[0]
    # 	time_p02 = time_p001.split(':')[1]
    # 	time_p = time_p01 + ':' + time_p02
    # 	price = 'Договорная'
    # 	image = 'images/freelance.png'

    # 	try:
    # 		p = Fl.objects.get(link=link)
    # 		p.show = show
    # 		p.price = price
    # 		p.ref_link = ref_link
    # 		#p.date_p = date_p
    # 		# p.time_p = time_p
    # 		p.save()
    # 	except Fl.DoesNotExist:
    # 		p = Fl(
    # 			link=link,
    # 			show=show,
    # 			price = price,
    # 			ref_link = ref_link,
    # 			date_p = date_p,
    # 			time_p = time_p,
    # 			image = image,
    # 			).save()
    # 		print('1 ', link)


# print('---**+++***--- && ---***+++**---')


def refind_name_y(a):
    return a.split('.')[2]


def refind_name_m(a):
    return a.split('.')[1]


def refind_name_d(a):
    return a.split('.')[0]


def refind_name_5(a):
    a1 = a.split('Для')[0]
    a2 = a1.split('Просмотров: ')[-1]
    return a2.split('Безопасная Сделка')[0]


def refind_name_6(string):
    try:
        return re.search('Для Бизнес-аккаунтов', string)[0]
    except:
        return re.search('Безопасная Сделка', string)[0]
    return string


def refind_link(url):
    useragents = open('txt/list_useragents_1824_i_e.txt').read().split('\n')
    proxies = open('txt/proxies_new_ipv4.txt').read().split('\n')
    try:
        try:
            proxy = {'https': 'https://' + choice(proxies)}
            useragent = {'User-Agent': choice(useragents)}
            html = get_html(url, useragent, proxy)
            links = get_all_links(html, url)
        except:
            proxy = {'https': 'https://' + choice(proxies)}
            useragent = {'User-Agent': choice(useragents)}
            html = get_html(url, useragent, proxy)
            links = get_all_links(html, url)
    except:
        # try:
        # 	try:
        # 		try:
        # 			try:
        # 				try:
        # 					proxy = {'https': 'https://' + choice(proxies)}
        # 					useragent = {'User-Agent': choice(useragents)}
        # 					html = get_html(url, useragent, proxy)
        # 					links = get_all_links(html, url)
        # 				except:
        # 					proxy = {'https': 'https://' + choice(proxies)}
        # 					useragent = {'User-Agent': choice(useragents)}
        # 					html = get_html(url, useragent, proxy)
        # 					links = get_all_links(html, url)
        # 			except:
        # 				try:
        # 					proxy = {'https': 'https://' + choice(proxies)}
        # 					useragent = {'User-Agent': choice(useragents)}
        # 					html = get_html(url, useragent, proxy)
        # 					links = get_all_links(html, url)
        # 				except:
        # 					proxy = {'https': 'https://' + choice(proxies)}
        # 					useragent = {'User-Agent': choice(useragents)}
        # 					html = get_html(url, useragent, proxy)
        # 					links = get_all_links(html, url)
        # 		except:
        # 			try:
        # 				try:
        # 					proxy = {'https': 'https://' + choice(proxies)}
        # 					useragent = {'User-Agent': choice(useragents)}
        # 					html = get_html(url, useragent, proxy)
        # 					links = get_all_links(html, url)
        # 				except:
        # 					proxy = {'https': 'https://' + choice(proxies)}
        # 					useragent = {'User-Agent': choice(useragents)}
        # 					html = get_html(url, useragent, proxy)
        # 					links = get_all_links(html, url)
        # 			except:
        # 				try:
        # 					proxy = {'https': 'https://' + choice(proxies)}
        # 					useragent = {'User-Agent': choice(useragents)}
        # 					html = get_html(url, useragent, proxy)
        # 					links = get_all_links(html, url)
        # 				except:
        # 					proxy = {'https': 'https://' + choice(proxies)}
        # 					useragent = {'User-Agent': choice(useragents)}
        # 					html = get_html(url, useragent, proxy)
        # 					links = get_all_links(html, url)
        # 	except:
        # 		try:
        # 			try:
        # 				try:
        # 					proxy = {'https': 'https://' + choice(proxies)}
        # 					useragent = {'User-Agent': choice(useragents)}
        # 					html = get_html(url, useragent, proxy)
        # 					links = get_all_links(html, url)
        # 				except:
        # 					proxy = {'https': 'https://' + choice(proxies)}
        # 					useragent = {'User-Agent': choice(useragents)}
        # 					html = get_html(url, useragent, proxy)
        # 					links = get_all_links(html, url)
        # 			except:
        # 				try:
        # 					proxy = {'https': 'https://' + choice(proxies)}
        # 					useragent = {'User-Agent': choice(useragents)}
        # 					html = get_html(url, useragent, proxy)
        # 					links = get_all_links(html, url)
        # 				except:
        # 					proxy = {'https': 'https://' + choice(proxies)}
        # 					useragent = {'User-Agent': choice(useragents)}
        # 					html = get_html(url, useragent, proxy)
        # 					links = get_all_links(html, url)
        # 		except:
        # 			try:
        # 				try:
        # 					proxy = {'https': 'https://' + choice(proxies)}
        # 					useragent = {'User-Agent': choice(useragents)}
        # 					html = get_html(url, useragent, proxy)
        # 					links = get_all_links(html, url)
        # 				except:
        # 					proxy = {'https': 'https://' + choice(proxies)}
        # 					useragent = {'User-Agent': choice(useragents)}
        # 					html = get_html(url, useragent, proxy)
        # 					links = get_all_links(html, url)
        # 			except:
        # 				try:
        # 					proxy = {'https': 'https://' + choice(proxies)}
        # 					useragent = {'User-Agent': choice(useragents)}
        # 					html = get_html(url, useragent, proxy)
        # 					links = get_all_links(html, url)
        # 				except:
        # 					proxy = {'https': 'https://' + choice(proxies)}
        # 					useragent = {'User-Agent': choice(useragents)}
        # 					html = get_html(url, useragent, proxy)
        # 					links = get_all_links(html, url)
        # except:
        print('**-get_all_links_NO_POWER_IN-**')
    return links


def make_all(url):
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
        pattern = 'https://freelance.ru/projects/filter/?page={}'
        for index, i in enumerate(range(1, 31)):  # max 94
            url = pattern.format(str(i))
            all_links.append(url)
        # print(all_links)

        with Pool(10) as p:
            p.map(make_all, all_links)

        end = datetime.now()
        f = end - start
        print("Full Parsing freelance:", f)
        print("--------------------------------------------------")
