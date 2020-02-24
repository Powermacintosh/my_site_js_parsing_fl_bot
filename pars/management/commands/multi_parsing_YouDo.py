from django.core.management.base import BaseCommand
from pars.models import Fl

import requests
from bs4 import BeautifulSoup
from random import choice
from random import uniform
from time import sleep
from datetime import datetime
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
	uas = soup.find('ul', class_="b-tasks__items") # Первое название, оглавление
	# print('--*-- Найдено', len(uas), 'элементов --*--')
	for index, ua in enumerate(uas):
		try:
			name = ua.find('a').text
			# ref_name = refind_name(name)
		except:
			name = '- - - - -'
		try:
			url = 'https://youdo.com' + ua.find('a').get('href')
		except:
			url = '- - - - -'

		# print('-------------- && --------------')

		strings = ['Спарсить', 'спарсить', 'Парсинг', 'парсинг', 'Парсер', 'парсер']
		for string in strings:
			match = re.search(string, name)
			if match:
				# print('Порядковый номер:', index+1)
				# print('Текст:', name)
				# print('Ссылка:', url)
			
				ref_link = refind_links(url)
				# print('===', ref_link)
			

	# print('---**+++***--- && ---***+++**---')

def get_all_links(html):
	soup = BeautifulSoup(html, 'lxml')
	try:
		tds = soup.find('div', class_="b-task-block__description").text
		name = soup.find('h1', class_="b-task-block__header__title").text
		name_2 = soup.find('div', class_="js-task-item--brief").find('li', class_="b-task-brief__item").text
		ref_name_2 = refind_name_2(name_2)
		name_3 = soup.find('div', class_="js-task-item--brief").find('li', class_="b-task-brief__item").find_next_sibling('li').text
		# ref_name_3 = refind_name_3(name_3)
		name_4 = soup.find('span', class_="js-budget-text").text
		ref_name_4 = refind_name_4(name_4)
		name_5 = soup.find('div', class_="js-task-item--brief").find('li', class_="b-task-brief__item").find_next_sibling('li').find_next_sibling('li').find_next_sibling('li').find_next_sibling('li').text
		ref_name_5 = 'https://youdo.com/t' + refind_name_5(name_5)

		# print('1', name)
		# print('2', ref_name_2)
		# print('3', name_3)
		# print('4', ref_name_4)
		# print('5', ref_name_5)
		# print('6', tds)


		link = ref_name_5
		show = name
		ref_link = tds
		date_p = str(datetime.now()).split(' ')[0]
		# print(date_p)
		time_p1 = str(datetime.now()).split(' ')[1]
		time_p001 = time_p1.split('.')[0]
		time_p01 = time_p001.split(':')[0]
		time_p02 = time_p001.split(':')[1]
		time_p = time_p01 + ':' + time_p02
		# print(time_p)
		price = ref_name_4
		image = 'images/youdo.png'

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


		return tds
	except:
		r = '**-??????????????-**'
		return r

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
		print('---**-!!!!!!!!!!-**---')
	return links


def refind_name_2(a):
	a1 = a.replace(' ', '')
	return a1.replace('\r\n', '')
	
# def refind_name_3(a):
# 	return a.split(' ')

def refind_name_4(a):
	a1 = a.replace(' ', '')
	a2 = a1.replace('\n\r\n', '')
	a3 = a2.replace('\r\n', '')
	return a3.replace('\n\n', '')

def refind_name_5(a):
	a1 = a.replace(' ', '')
	a2 = a1.replace('\r\n\t\t', '')
	a3 = a2.replace('\r\n\t', '')
	return a3.split('№')[1]

def refind_ua_1(a):
    return a.split(' ')[1:6]

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
		pattern = 'https://youdo.com/tasks-all-any-webdevelopment-{}'
		for index, i in enumerate(range(1, 11)): # max 94
			url = pattern.format(str(i))
			all_links.append(url)
		# print(all_links)
		
		with Pool(10) as p:
			p.map(make_all, all_links)

		end = datetime.now()
		f = end - start
		print("Full Parsing YouDo:", f)
		print("--------------------------------------------------")