#coding:utf-8

import sys
import socket
import urllib.request
import traceback
import url_manager
import html_parser
import html_outputer
import html_downloader
#爬虫总调动程序

class SpiderMain(object):
	"""docstring for SpiderMain"""
	def __init__(self):		#爬虫初始化
		self.urls = url_manager.UrlManager()				#URL管理器
		self.downloader = html_downloader.HtmlDownloader()	#下载器
		self.parser = html_parser.HtmlParser()				#分析器
		self.outputer = html_outputer.HtmlOutputer()		#输出器
		pass

	def craw(self, root_utl):
		#爬虫调度程序
		count = 1	#网页爬取数量初始值
		self.urls.add_new_url(root_utl)
		print("已将%s加入到new_urls"%self.urls.new_urls)
		while self.urls.has_new_url():	
			try:
				print("\n###################################开始爬取网页####################################")
				new_url = self.urls.get_new_url()
				print ('正在爬取 第%d条url:\n%s'%(count,new_url))		#爬取第几个URL

				html_cont = self.downloader.download(new_url)
				#print("正在下载新的url:\n%s"%new_url)

				new_url,new_data = self.parser.parse(new_url,html_cont)
				#print("%s\n新的url解析完成"%(new_url))

				self.urls.add_new_urls(new_url)
				print("新的url已加入UrlManager:\n%s"%new_url)

				self.outputer.collect_data(new_data)	#收集新数据
				print("新的数据正在保存至本地:\n%s"%new_data)

				self.outputer.output_html()		#将数据保存至本地文件

				#设置爬取网页的数量
				if count == 100000:
					break
				count = count+1
				
			except:
				print("爬取失败")	#爬取失败反馈
				info = sys.exc_info()
				print(info[0],":",info[1])
				traceback.print_exc()

		
		print("################################爬虫结束######################################")


if __name__ == '__main__':
	#root_utl = 'www.site.baidu.com'
	webaddress = input("请输入爬虫初始URL：(无需加 \"http:\") 例如:www.boke.la\n>")
	root_utl = 'http://'+webaddress+'/'#通过用户输入的网址连接上网络协议，得到URL
	
	#超时测试
	timeout = 5	#设置超时
	socket.setdefaulttimeout(timeout)

	obj_spider = SpiderMain()		#爬虫主函数
	obj_spider.craw(root_utl)		#启动爬虫