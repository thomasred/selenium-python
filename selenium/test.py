#coding=utf-8
#environment python2.7
import random
import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
	cwd = os.getcwd() + '/' # 取地目前資料夾路徑
	browser = webdriver.Chrome(cwd + 'tool/chromedriver') # 啟動 chromedriver
	wait = WebDriverWait(browser, 10) # 只指定超時時間

	f = open('link.txt', 'a+') # 儲存抓到連結的檔案
	query = u'下雪' # 指定要查詢的Query


	try:
		search_google(browser, query);
		#page = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//td/a[@class='fl']")))
		#print len(page)

		# 開始抓取搜尋結果中前10頁的連結
		for i in xrange(0, 10):
			#links = browser.find_elements_by_xpath("//h3[@class='r']/a")
			links  = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//h3[@class='r']/a")))
			
			for link in links:
				#print link.text
				f.write(link.get_attribute("href")+'\n')
			time.sleep(random.uniform(1, 3)) # 等待
			
			page = wait.until(EC.presence_of_element_located((By.ID, 'pnnext'))) # 找到"下一頁"的按鍵
			page.click()
	except:
		# 一旦出現狀況就顯示這個，例如搜尋結果只有一頁
		print "Out of page!"

	finally:
		f.close()


	time.sleep(10) # 等待
	browser.quit()


	#pageSource = driver.page_source
	#print pageSource.encode('utf-8')
	#f.write(pageSource.decode("utf-8"))



def search_google(browser, query):
	browser.get('http://www.google.com.tw/') # 前往 google 首頁
	time.sleep(random.uniform(2, 8)) # 隨機等待
	search = browser.find_element_by_xpath("//input[@id='lst-ib']") # 取得搜尋框
	search.send_keys(query) # 在搜尋框內輸入
	search.submit() # 令 chrome driver 按下 submit




#'''
if __name__ == '__main__':
	main()