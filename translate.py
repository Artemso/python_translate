#!/usr/bin/python3

import sys
import scrapy
from bs4 import BeautifulSoup
import json
import urllib

def	char_to_hex(c):
	temp = ord(c)
	return(hex(temp))

def	str_to_hex(str):
	new = ""
	for x in str:
		new += '%' + char_to_hex(x)[2:]
	return(new)

def	check_args():
	if len(sys.argv) != 4:
		sys.exit("Usage: python3 translate.py <Source Language> <Destination Language> <String>")
	fd = open("langs.json", "r")
	langs = fd.read()
	langs_data = json.loads(langs)
	source_lang = ""
	dest_lang = ""
	for key, value in langs_data.items():
		if sys.argv[1] == value:
			source_lang = key
		if sys.argv[2] == value:
			dest_lang = key
	string = sys.argv[3]
	if not source_lang or not dest_lang:
		sys.exit("Languages are misspelled or missing")
	else:
		return(source_lang, dest_lang, string)

def	get_full_url(base_url, source_lang, dest_lang, string):
	source_lang = '&sl=' + source_lang
	dest_lang = '&tl=' + dest_lang
	string = str_to_hex(string)
	string = '&q=' + string
	full_url = base_url + source_lang + dest_lang + string
	return(full_url)

def	main():
	base_url = 'https://translate.google.com/m?hl=en'
	source_lang, dest_lang, string = check_args()
	full_url = get_full_url(base_url, source_lang, dest_lang, string)
	user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
	request = urllib.request.Request(full_url,headers={'User-Agent': user_agent})
	response = urllib.request.urlopen(request)
	html = response.read()
	soup = BeautifulSoup(html, 'html.parser')
	output = soup.find('div', {'class':'t0'}).text
	print(output)
main()