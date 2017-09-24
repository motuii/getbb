#coding:utf-8
import os
import sys
import traceback

class HtmlOutputer(object):
	def __init__(self):
		self.datas = []		#定义一个收集数据的列表

	def collect_data(self,data):
		if data is None:
			return
		
		self.datas.append(data)		#将数据添加到列表
			
	def output_html(self):
		#将爬取信息保存至output文件夹中
		#os.mkdir("output")
		fout = open('output/info.html','w',encoding="utf-8")

		fout.write("<html>")
		fout.write("<head>")
		fout.write("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">")
		fout.write("<body>") 
		fout.write("<div>")
		fout.write("<ol>")
		
		try:	
			#依次输出列表中的内容	
			for data in self.datas:
				fout.write("<li>")
				if 'title' in data.keys():
					fout.write("<h2>%s</h2>"%data['title'])
					fout.write("<br/>")
				else:
					fout.write("<h2>木有标题</h2>")
					fout.write("<br/>")
				if 'url' in data.keys():
					fout.write("<a href=\"%s\" target=\"_blank\">%s</a>"%(data['url'],data['url']))
					fout.write("<br/>")
				else:
					fout.write("<a href=#>木有链接</a>")
					fout.write("<br/>")
				if 'summary' in data.keys():
					fout.write("<p>%s</p>"%data['summary'])
					fout.write("<br/>")
				else:
					fout.write("<p>木有简介</p>")
					fout.write("<br/>")
				fout.write("</li>")
				
			print("数据已保存在%s"%os.path.dirname(os.path.abspath('__file__')))
		except:
			print("保存失败")	#保存失败反馈信息
			info = sys.exc_info()
			print(info[0],":",info[1])
			traceback.print_exc()

		fout.write("</ol>")
		fout.write("</div>")
		fout.write("</body>")
		fout.write("</head>")
		fout.write("</html>")

		fout.close()
		


	


		