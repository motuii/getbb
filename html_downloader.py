#coding:utf-8
import urllib.request

class HtmlDownloader(object):
	"""docstring for HtmlDownloader"""
	def download(self, url):
		if url is None:
			return None
		response = urllib.request.urlopen(url)		#下载网页数据
		#超时判断
		if response.getcode() != 200:
			return None

		return response.read()

