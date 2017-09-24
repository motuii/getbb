#coding:utf-8
from bs4 import BeautifulSoup
import urllib
import chardet
import re

class HtmlParser(object):
	"""docstring for HtmlParser"""
	def _get_new_urls(self,page_url,soup):
		new_urls = set()
		#/^http:\/\/www\.\w.+\.\w+(\.\w+)?$/
		links = soup.find_all(href=re.compile(r"^[a-zA-z]+://([a-zA-Z])+.[0-9a-zA-Z]+.([a-zA-Z])+$"))
		for link in links:

			new_url = link['href']
			#new_full_url = urllib.parse.urljoin(page_url,new_url)
			new_urls.add(new_url)
		return new_urls



	def _get_new_data(self,page_url,soup):
		#从网页解析中获得数据
		res_data = {}	#存储字典

		#获取标题内容
		title_node = soup.title
		if title_node != None:
			res_data['title'] = title_node.get_text()
			#print(title_node)

		#获取摘要内容<div class="lemma-summary"
		summary_node = soup.find(attrs={"name":"description"})
		if summary_node != None:
			res_data['summary'] = summary_node['content']
			#print(summary_node)
		#保存网页内容
		
		res_data['url'] = page_url
		
		return res_data


	def parse(self, page_url,html_cont):
		if page_url is None or html_cont is None:
			return

		#转码 默认utf-8
		content = chardet.detect(html_cont)	#判断网页编码类型
		type_code =  content['encoding'] #将网页编码类型赋值给type_code
		if type_code != 'utf-8':	#对非utf-8编码进行解码和编码
			html_cont = html_cont.decode(type_code)	#解码
			html_cont = html_cont.encode('utf-8')	#编码utf-8格式

		soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
		new_urls = self._get_new_urls(page_url,soup)
		new_data = self._get_new_data(page_url,soup)
		return new_urls,new_data


