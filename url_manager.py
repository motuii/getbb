#coding:utf-8

class UrlManager(object):
	"""docstring for __init__"""
	def __init__(self):
		self.new_urls = set()
		self.old_urls = set()
		
	#添加一个url
	def add_new_url(self,url):
		if url is None:
			return

		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)

	#批量添加URL
	def add_new_urls(self,urls):
		if urls is None or len(urls) == 0:
			return

		for url in urls:
			self.add_new_url(url)

	#是否有未爬取的URL
	def has_new_url(self):
		return len(self.new_urls) != 0

	#获取新的未爬取URL
	def get_new_url(self):
		new_url = self.new_urls.pop()
		self.old_urls.add(new_url)
		return new_url

