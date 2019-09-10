import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def healthline_web_scraping(symptom):
	base="https://www.healthline.com/symptom/"
	profile=base+symptom
	# print(profile)
	try:
		# post_data = {'age':'21'}

		# POST some form-encoded data:
		# post_response = requests.post(url='https://symptoms.webmd.com/default.htm#/info', data=post_data)
		# print(post_response)
		req = Request(profile, headers={'User-Agent': 'Mozilla/5.0'})
		web_byte = urlopen(req).read()
		webpage = web_byte.decode('utf-8')
		# print(webpage)
		soup=BeautifulSoup(webpage,'lxml')
		deepak=soup.select('.e1rb0dkr1')
		# print(deepak[0])
		# print(deepak[0].attrs['colour'])
		return 1,deepak
		# deepak=deepak.unicode('utf-8')
		# for i in deepak:
		# print(i)
	except urllib.error.HTTPError as err:
		if err.code == 404:
			print("Page1 not found!")
			return 0,symptom+" not found on "+"healthline!"
		elif err.code == 403:
			print("Access denied!")
			return 0,"Access denied!"
		else:
			print("Something happened! Error code", err.code)
			return 0,"Something happened! Error code "
	except urllib.error.URLError as err:
		print("Some other error happened:", err.reason)
		return 0,"Some other error happened:\check your internet connectivity"
