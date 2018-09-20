#!/usr/bin/env python
#encoding: utf-8

from launcher import Launcher
from Elasticsearch_tw import Es_twitter
import time

class Follower():
    def __init__(self, username, password, current_ts, consumer_key, consumer_secret, access_token, access_secret, *args):
        self.launcher = Launcher(username, password, consumer_key, consumer_secret, access_token, access_secret)
        self.api = self.launcher.api()
        self.es = Es_twitter()
        self.list = []
        self.update_time = int(time.time())
        try:
            self.uid = args[0]
        except Exception as e:
            print "no uid"

    def get_follower(self):
        try:
            for each in self.api.followers(self.uid):
                nick_name = each.name
                print 'nick_name:', nick_name
                user_name = each.screen_name
                print 'user_name:', user_name
                id = each.id
                print 'uid:', id
                photo_url = each.profile_image_url_https
                print 'photo_url:', photo_url
                profile_url = 'https://twitter.com/' + screen_name
                print 'profile_url:', profile_url
                item = {
                    'user_name':user_name,
                    'nick_name':nick_name,
                    'uid':id,
                    'photo_url':photo_url,
                    'profile_url':profile_url
                }
                self.list.append(item)
        except Exception as e:
            for each in self.api.followers():
                name = each.name
                screen_name = each.screen_name
                id = each.id
                photo_url = each.profile_image_url_https
                profile_url = 'https://twitter.com/' + screen_name
                item = {
                    'user_name':name,
                    'nick_name':screen_name,
                    'uid':id,
                    'photo_url':photo_url,
                    'profile_url':profile_url,
                    'update_time':self.update_time,
                }
                self.list.append(item)
        return self.list


    def save(self, indexName, typeName, follower_list):
        self.es.executeES(indexName, typeName, follower_list)


if __name__ == '__main__':
    current_ts = int(time.time())
    follower = Follower('18538728360@163.com','zyxing,0513',current_ts, 'N1Z4pYYHqwcy9JI0N8quoxIc1', 'VKzMcdUEq74K7nugSSuZBHMWt8dzQqSLNcmDmpGXGdkH6rt7j2', '943290911039029250-yWtATgV0BLE6E42PknyCH5lQLB7i4lr', 'KqNwtbK79hK95l4X37z9tIswNZSr6HKMSchEsPZ8eMxA9', "902921493155217409") #传uid
    
    follower_list = follower.get_follower()
    print follower_list
    follower.save('twitter_feedback_fans', 'text', follower_list)

