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
	uas = soup.find('ul', class_="content-list") # Первое название, оглавление
	# print('--*-- Найдено', len(uas), 'элементов --*--')
	for index, ua in enumerate(uas):
		try:
			name = ua.find(class_="task__title").text
			# ref_name = refind_name(name)
		except:
			name = '- - - - -'
		try:
			url = 'https://freelansim.ru' + ua.find('a').get('href')
		except:
			url = '- - - - -'

		# print('-------------- && --------------')
		strings = ['Django', 'django']
		for string in strings:
			match = re.search(string, name)
			if match:
				# print('Порядковый номер:', index+1)
				# print('Текст:', name)
				# print('Ссылка:', url)
					
				ref_link = refind_links(url)
				# print('===', ref_link)
			

	# print('---**+++***--- && ---***+++**---')

def refind_name_d(s):
	return s.split(' ')[0]

def refind_name_y(s):
	s1 = s.split(',')[0]
	return s1.split(' ')[2]

def refind_name_m(s):
	return s.split('-')[1]


def refind_date_1(a):
	a1 = a.replace('\n', '')
	return a1.split('•')[0]

def refind_date_2(a):
	a1 = a.replace('\n', '')
	return a1.split('• ')[1]

def refind_date_3(a):
	a1 = a.replace('\n', '')
	return a1.split('• ')[2]


def refind_t(string):
    return re.search(r'\d\d:\d\d', string)[0]

def get_all_links(html):
	soup = BeautifulSoup(html, 'lxml')
	try:
		tds = soup.find('div', class_="task__description").text
	except:
		tds = '!-----!-----!'
	try:
		name = soup.find('h2', class_="task__title").text
	except:
		name = '!-----!-----!'
	try:
		date = soup.find('div', class_="task__meta").text
	except:
		date = '!-----!-----!'
	ref_date_1 = refind_date_1(date)
	ref_date_2 = refind_date_2(date)
	ref_date_3 = refind_date_3(date)
	try:
		prise = soup.find('div', class_="task__finance").text
	except:
		prise = '!-----!-----!'
	try:
		url_l = soup.find('div', class_="dropdown__menu").find('a').get('href')
	except:
		url_l = '!-----!-----!'
	try:
		ref_url_l = 'https' + url_l.split('+http')[1]
	except:
		ref_url_l = '!-----!-----!'
	# print(name)
	# print(ref_date_1)
	# print(ref_date_2)
	# print(ref_date_3)
	# print(prise)
	# print(tds)
	date_y = refind_name_y(ref_date_1)
	# print(date_y)
	date_d = refind_name_d(ref_date_1)
	# print(date_d)
	date_m = refind_name_m(str(datetime.now()).split(' ')[0])
	# print(date_m)


	ref_date = date_y + '-' + date_m + '-' + date_d
	# print(ref_date)

	link = ref_url_l
	show = name
	ref_link = tds
	date_p = ref_date
	time_p = refind_t(ref_date_1)
	price = prise
	image = 'images/freelansim.png'
	
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
		pattern = 'https://freelansim.ru/tasks?page={}'
		for index, i in enumerate(range(1, 11)): # max 94
			url = pattern.format(str(i))
			all_links.append(url)
		# print(all_links)
		
		with Pool(5) as p:
			p.map(make_all, all_links)	
		
		end = datetime.now()
		f = end - start
		print("Full Parsing freelansim:", f)
		print("--------------------------------------------------")