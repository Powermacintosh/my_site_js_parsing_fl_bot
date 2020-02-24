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
	# print('---**???***--- && ---***???**---')
	soup = BeautifulSoup(html, 'lxml')
	# uas = soup.find('div', class_="page")
	uas = soup.find('tbody').find_all('tr')
	# print('--*-- Найдено', len(uas), 'элементов --*--')
	# print(uas)
	for index, ua in enumerate(uas):
		try:
			name = ua.find('td', class_="left").text
		except:
			name = '---'
		try:
			url = ua.find('td', class_="left").find('a').get('href')
		except:
			url = '- - - - -'
		try:
			price = ua.find('td', class_="text-center").find('div', class_="text-green").text
		except:
			price = 'Договорная'
		try:
			dates = ua.find_all('td', class_="text-center")
			for index, d in enumerate(dates):
				if index==2:
					try:
						date = d.find('div', class_="with-tooltip").find('h2').text
					except:
						date = '++++++'

		except:
			dates = '-----' 
		# print(name)
		# print(url)

		# print('-------------- && --------------')

		# strings = ['парс',]
		# for string in strings:
		# 	match = re.search(string, name)
		# 	if match:
		# print('Порядковый номер:', index+1)
		ref_link = refind_links(url)
		# print('Текст:', name.split('\n')[1])
		# print('Ссылка:', url)
		# print('Дата:', date)
		# print('Цена:', price)
		# print('Содержание:', ref_link)

		if date in [
			'31', '30', '29', '28', '27', 
			'26', '25', '24', '23', '22', 
			'21', '20', '19', '18', '17', 
			'16', '15', '14', '13', '12', 
			'11', '10', '9', '8', '7', 
			'6', '5', '4', '3', '2', '1'
				]:
			# print(date)
			continue
		else:
			link = url
			show = refind_name(name)
			date_p = str(datetime.now()).split(' ')[0]
			time_p = date
			image = 'images/freelancehunt.png'

			try:
				p = Fl.objects.get(link=link)
				p.show = show
				p.price = price
				p.ref_link = ref_link
				# p.date_p = date_p
				# p.time_p = time_p
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
			

	print('---**+++***--- && ---***+++**---')

def refind_name(a):
	return a.split('\n\n\n')[0]
	



def get_all_links(html):
	soup = BeautifulSoup(html, 'lxml')
	try:
		tds_20 = soup.find('div', class_="linkify-marker img-responsive-container").text
		tds_19 = tds_20.replace('\xa0', '\n')
		tds_18 = tds_19.replace('•', '\n •')
		tds_17 = tds_18.replace('10)', '\n 10)')
		tds_16 = tds_17.replace('1)', '\n 1)')
		tds_15 = tds_16.replace('2)', '\n 2)')
		tds_14 = tds_15.replace('3)', '\n 3)')
		tds_13 = tds_14.replace('4)', '\n 4)')
		tds_12 = tds_13.replace('5)', '\n 5)')
		tds_11 = tds_12.replace('6)', '\n 6)')
		tds_10 = tds_11.replace('7)', '\n 7)')
		tds_9 = tds_10.replace('8)', '\n 8)')
		tds_8 = tds_9.replace('9)', '\n 9)')
		tds_7 = tds_8.replace('https:', '\nhttps:')
		tds_6 = tds_7.replace(';', ';\n')
		tds_5 = tds_6.replace('!', '!\n')
		tds_4 = tds_5.replace('Требования к фрилансеру:', '\nТребования к фрилансеру:\n')
		tds_3 = tds_4.replace('Требования:', '\nТребования:\n')
		tds_2 = tds_3.replace('Условия:', '\n Условия:')
		tds_1 = tds_2.replace('ВАЖНО', '\n ВАЖНО \n')
		tds_01 = tds_1.replace('Дополнительная информация', '\n Дополнительная информация \n')
		tds_001 = tds_01.replace('Требования к кандидату:', '\nТребования к кандидату:\n')
		tds_0001 = tds_001.replace('Требования к работе:', '\nТребования к работе:\n')
		tds_00001 = tds_0001.replace('Требуется:', '\nТребуется:\n')
		tds_02 = tds_00001.replace('Задача:', '\nЗадача:\n')
		tds_002 = tds_02.replace('.10.', '.\n 10.')
		tds_0002 = tds_002.replace('.2.', '.\n 2.')
		tds_00002 = tds_0002.replace('.3.', '.\n 3.')
		tds_03 = tds_00002.replace('.4.', '.\n 4.')
		tds_003 = tds_03.replace('.5.', '.\n 5.')
		tds_0003 = tds_003.replace('.6.', '.\n 6.')
		tds_00003 = tds_0003.replace('.7.', '.\n 7.')
		tds_04 = tds_00003.replace('.8.', '.\n 8.')
		tds_004 = tds_04.replace('.9.', '.\n 9.')
		tds_0004 = tds_004.replace('.1.', '.\n 1.')
		tds_00004 = tds_0004.replace('С Уважением', '\n С Уважением')
		tds = tds_00004.replace('.-', '.\n-') 
		# tds = tds_10.split(' ')
		# print(tds)
	except:
		tds = '!-----!-----!'
	return tds


def refind_links(url):
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
					except:
						proxy = {'https': 'https://' + choice(proxies)}
						useragent = {'User-Agent': choice(useragents)}
						html = get_html(url, useragent, proxy)
						links = get_all_links(html)
				except:
					try:
						proxy = {'https': 'https://' + choice(proxies)}
						useragent = {'User-Agent': choice(useragents)}
						html = get_html(url, useragent, proxy)
						links = get_all_links(html)
					except:
						proxy = {'https': 'https://' + choice(proxies)}
						useragent = {'User-Agent': choice(useragents)}
						html = get_html(url, useragent, proxy)
						links = get_all_links(html)			
			except:
				try:
					try:
						proxy = {'https': 'https://' + choice(proxies)}
						useragent = {'User-Agent': choice(useragents)}
						html = get_html(url, useragent, proxy)
						links = get_all_links(html)
					except:
						proxy = {'https': 'https://' + choice(proxies)}
						useragent = {'User-Agent': choice(useragents)}
						html = get_html(url, useragent, proxy)
						links = get_all_links(html)
				except:
					try:
						proxy = {'https': 'https://' + choice(proxies)}
						useragent = {'User-Agent': choice(useragents)}
						html = get_html(url, useragent, proxy)
						links = get_all_links(html)
					except:
						proxy = {'https': 'https://' + choice(proxies)}
						useragent = {'User-Agent': choice(useragents)}
						html = get_html(url, useragent, proxy)
						links = get_all_links(html)
		except:
			try:
				try:
					try:
						proxy = {'https': 'https://' + choice(proxies)}
						useragent = {'User-Agent': choice(useragents)}
						html = get_html(url, useragent, proxy)
						links = get_all_links(html)
					except:
						proxy = {'https': 'https://' + choice(proxies)}
						useragent = {'User-Agent': choice(useragents)}
						html = get_html(url, useragent, proxy)
						links = get_all_links(html)
				except:
					try:
						proxy = {'https': 'https://' + choice(proxies)}
						useragent = {'User-Agent': choice(useragents)}
						html = get_html(url, useragent, proxy)
						links = get_all_links(html)
					except:
						proxy = {'https': 'https://' + choice(proxies)}
						useragent = {'User-Agent': choice(useragents)}
						html = get_html(url, useragent, proxy)
						links = get_all_links(html)			
			except:
				try:
					try:
						proxy = {'https': 'https://' + choice(proxies)}
						useragent = {'User-Agent': choice(useragents)}
						html = get_html(url, useragent, proxy)
						links = get_all_links(html)
					except:
						proxy = {'https': 'https://' + choice(proxies)}
						useragent = {'User-Agent': choice(useragents)}
						html = get_html(url, useragent, proxy)
						links = get_all_links(html)
				except:
					try:
						proxy = {'https': 'https://' + choice(proxies)}
						useragent = {'User-Agent': choice(useragents)}
						html = get_html(url, useragent, proxy)
						links = get_all_links(html)
					except:
						proxy = {'https': 'https://' + choice(proxies)}
						useragent = {'User-Agent': choice(useragents)}
						html = get_html(url, useragent, proxy)
						links = get_all_links(html)
	except:		
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
		pattern = 'https://freelancehunt.com/projects?page={}'
		for index, i in enumerate(range(1, 21)): # Max 130
			url = pattern.format(str(i))
			all_links.append(url)
		# print(all_links)
		
		with Pool(10) as p:
			p.map(make_all, all_links)	
		
		end = datetime.now()
		f = end - start
		print("Full Parsing FreelanceHunt:", f)
		print("--------------------------------------------------")