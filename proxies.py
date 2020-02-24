from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from datetime import datetime
from random import uniform
from time import sleep


start = datetime.now()


def main():
	opts = Options()
	opts.set_headless()

	time_out_1 = 3
	time_out_2 = 8
	# ------------------- clear-txt ---------------------
	p_del = ''
	with open(r"txt/proxies_new_ipv4.txt", "w") as file:
	    file.writelines("%s\n" % line for line in p_del)

	m_del = ''
	with open(r"txt/parsing_proxies.txt", "w") as file:
	    file.writelines("%s\n" % line for line in m_del)

	iter_n = '3'
	with open(r"txt/pagging_proxies.txt", "w") as file:
	    file.writelines("%s\n" % line for line in iter_n)
	# ------------------- clear-txt ---------------------


	driver = webdriver.Firefox(options=opts)
	driver.get("https://advanced.name/ru/freeproxy?page=1")
	# driver.get("https://advanced.name/ru/freeproxy")

	while True:

		for index, element in enumerate(driver.find_elements_by_xpath('//*[@id="table_proxies"]/tbody')):
			ref_11 = element.text
			# print(element.text)

		m = element.text
		text_a = m.split('\n')
		with open(r"txt/parsing_proxies.txt", "w") as file:
		    file.writelines("%s\n" % line for line in text_a)


		iter_n = open('txt/pagging_proxies.txt').read().split('\n')[0]
		iter_n_d = str(int(iter_n) + 1)

		# ----------------- smart-parsing-txt -------------------
		rows = open('txt/parsing_proxies.txt').read().split('\n')
		rows_i = int(len(rows))-1
		print(rows_i)
		s = []
		for i in range(0, rows_i):
			s.append(i)
		# print(s)
		proxi = []
		for index, row in enumerate(rows):
			if index in s:	
				ref_1 = row.split(' ')[1]
				pr = ref_1
				ref_2 = row.split(' ')[2]
				port = ref_2
				ref_p = pr + ':' + port
				proxi.append(ref_p)

		# print(proxi)
		# ----------------- smart-parsing-txt -------------------
		
		# ---------------- full-parsing-proxies -----------------
		for index, p in enumerate(proxi):
			text_p = p.split('\n')
			with open(r"txt/proxies_new_ipv4.txt", "a") as file:
			    file.writelines("%s\n" % line for line in text_p)
		# ---------------- full-parsing-proxies -----------------

		sleep(uniform(time_out_1,time_out_2))
		try:
			# print(iter_n)
			next_page = driver.find_element_by_css_selector(".pagination > li:nth-child(" + iter_n + ") > a:nth-child(1)")
			next_page_d = driver.find_element_by_css_selector(".pagination > li:nth-child(" + iter_n_d + ") > a:nth-child(1)")
			iter_new = int(iter_n) + 1
			iter_new_w = str(iter_new)

			with open(r"txt/pagging_proxies.txt", "w") as file:
			    file.writelines("%s\n" % line for line in iter_new_w)
		except:
			# print('Finish')
			break
		next_page.click()
		sleep(uniform(time_out_1,time_out_2))
		

	driver.quit()



if __name__ == '__main__':
    main()

end = datetime.now()
f = end - start
print("**************************************")
print("  Full Parsing:", f)