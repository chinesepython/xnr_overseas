#-*-coding:utf-8-*-
import sys
import redis



RE_QUEUE = redis.Redis(host='60.205.190.67', port=6379)


# facebook用户信息更新 
# facebook45提交的参数队列
FB_USER_PARAM = 'params'

# facebook爬虫的结果队列
FB_SPIDER_RESULT = 'result_info'



# 境外互动操作所需参数
FB_TWEET_PARAMS = 'fb_tweet_params'

