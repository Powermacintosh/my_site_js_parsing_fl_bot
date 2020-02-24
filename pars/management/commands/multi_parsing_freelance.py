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
		tds = soup.find('div', class_="s_box").find('h1', class_="proj_tophead").text.strip()
		tds_z = soup.find('p', class_="txt href_me").text.strip()
		ref_tds_z = refind_tds_z(tds_z)
		return ref_tds_z
	except:
		r = '**-Для Бизнес-аккаунтов-**'
		return r
	

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
        
		strings = ['Парсинг', 'парсинг', 'Парсер', 'парсер']
		for string in strings:
			match = re.search(string, name)
			if match:
				# print('Порядковый номер:', index+1)
				link = 'https://freelance.ru' + name_2
				ref_link = refind_link(link)
				# print('===', ref_link)
				
				# print('Текст:', name)
				# print('Дата:', date_pub)
				# print('Ответов:', name_4)
				# print('Просмотров:', ref_name_5)
				# print('Вид:', ref_name_6)


				show = name
				date_p = date_pub
				time_p1 = str(datetime.now()).split(' ')[1]
				time_p001 = time_p1.split('.')[0]
				time_p01 = time_p001.split(':')[0]
				time_p02 = time_p001.split(':')[1]
				time_p = time_p01 + ':' + time_p02
				price = 'Договорная'
				image = 'images/freelance.png'

				try:
					p = Fl.objects.get(link=link)
					p.show = show
					p.price = price
					p.ref_link = ref_link
					p.date_p = date_p
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
		try:
			return re.search('Для Бизнес-аккаунтов', string)[0]
		except:
			return re.search('Безопасная Сделка', string)[0]
	except:
		string = '---'
		return string



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
		pattern = 'https://freelance.ru/projects/filter/?page={}'
		for index, i in enumerate(range(1, 21)): # max 94
			url = pattern.format(str(i))
			all_links.append(url)
		# print(all_links)
		
		with Pool(10) as p:
			p.map(make_all, all_links)	
	
		end = datetime.now()
		f = end - start
		print("Full Parsing freelance:", f)
		print("--------------------------------------------------")