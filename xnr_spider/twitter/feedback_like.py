#!/usr/bin/env python
#encoding: utf-8

from launcher import Launcher
from Elasticsearch_tw import Es_twitter
import time

class Like():
	def __init__(self, username, password, consumer_key, consumer_secret, access_token, access_secret):
		self.launcher = Launcher(username, password, consumer_key, consumer_secret, access_token, access_secret)	
		#self.driver = self.launcher.login()
		self.es = Es_twitter()
		self.api = self.launcher.api()
		#self.driver.get('https://twitter.com/i/notifications')
		time.sleep(2)
		#self.lis = self.driver.find_elements_by_xpath('//li[@data-item-type="activity"]')
		self.like_list = []
		self.update_time = int(time.time())

	def date2timestamp(self, date):
		format_time = time.strptime(date, '%a %b %d %H:%M:%S +0000 %Y')
		timestamp = int(time.mktime(format_time))
		return timestamp


	def get_like(self):
		favorites = self.api.favorites()
		#for li in self.lis:
		for favorite in favorites:
			#type = li.get_attribute('data-component-context')
			#if type == "favorite_activity":
			#	user_name = li.find_element_by_xpath('./div/div/div/div[2]/div[1]/a/strong').text
			user_name = favorite._json['user']['screen_name']
			print "user_name", user_name
				#screen_name = li.find_element_by_xpath('./div/div/div/div[2]/div[1]/a').get_attribute('href').replace('https:twitter.com/','')
			nick_name = favorite._json['user']['name']
			print "nick_name", nick_name
				#timestamp = li.find_element_by_xpath('./div/div/div/div[2]/div[1]/div[1]/div/span').get_attribute('data-time')
			timestamp = self.date2timestamp(favorite._json['user']['created_at'])
			print "timestamp", timestamp
				#user_id = li.find_element_by_xpath('./div/div/div/div[2]/div[1]/a').get_attribute('data-user-id')
			uid = favorite._json['user']['id']
			print "uid", uid
			#	root_user_id = li.find_element_by_xpath('./div/div/div/div[2]/div[2]/div/div/div').get_attribute('data-user-id')
			
			#print "root_user_id", root_user_id
			#	root_content = li.find_element_by_xpath('./div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]').text
			root_text = favorite.text
			print "root_text", root_text
			#	mid = li.get_attribute('data-item-id')
			root_mid = favorite.id
			print "root_mid", root_mid
			#	photo_url = li.find_element_by_xpath('./div/div/div/div[2]//img').get_attribute('src')
			photo_url = favorite._json['user']['profile_image_url_https']
			print "photo_url", photo_url

			item = {
					'uid':uid,
					'photo_url':photo_url,
					'user_name':user_name,
					'nick_name':nick_name,
					'timestamp':int(timestamp),
					'root_text':root_text,
					'update_time':self.update_time,
					#'root_text':root_content,
					'root_mid':root_mid
			}
			self.like_list.append(item)

		#self.driver.quit()
		return self.like_list

	def save(self,indexName,typeName,like_list):
		self.es.executeES(indexName,typeName,self.like_list)

if __name__ == '__main__':
	like = Like('18538728360@163.com', 'zyxing,0513', 'N1Z4pYYHqwcy9JI0N8quoxIc1', 'VKzMcdUEq74K7nugSSuZBHMWt8dzQqSLNcmDmpGXGdkH6rt7j2', '943290911039029250-yWtATgV0BLE6E42PknyCH5lQLB7i4lr', 'KqNwtbK79hK95l4X37z9tIswNZSr6HKMSchEsPZ8eMxA9')
	like_list = like.get_like()
	print(like_list)
	#like.save('twitter_feedback_like','text',list)

