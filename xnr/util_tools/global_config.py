# -*- coding: utf-8 -*-
'''
use to save database information
'''
import os
import time

# xnr system start date
SYSTEM_START_DATE = '2018-01-01'

#use to mark type:  run or test
S_TYPE = 'run'   #test/run
S_DATE = '2016-11-20' #when type=test, now_date=S_DATE
S_UID = '1910774981' #'3986246393'
S_DATE_BCI = '2016-11-27'
S_DATE_EVENT_WARMING = '2016-11-27'
S_DATE_WARMING = '2016-11-27'

WEIBO_COMMUNITY_DATE = '2016-11-27'

QQ_S_DATE = '2017-07-12'
QQ_S_DATE_NEW = '2017-08-25'
QQ_S_DATE_ASSESSMENT = '2018-03-07'
QQ_GROUP_MESSAGE_START_DATE = '2018-03-07'#'2017-08-23'
QQ_GROUP_MESSAGE_START_DATE_ASSESSMENT = '2018-03-01'#'2017-09-28'


S_DATE_FB = '2018-04-01'
S_DATE_TW = '2017-04-01'
S_UID_FB = '100018797745111'
S_UID_TW = '747226658457927680'
S_DATE_BCI_FB = '2017-10-25'
S_DATE_BCI_TW = '2017-10-25'
FACEBOOK_FLOW_START_DATE='2017-09-12'
TWITTER_FLOW_START_DATE='2017-10-25'

FACEBOOK_COMMUNITY_DATE = '2017-10-01'

R_BEGIN_TIME = '2017-07-07'

S_WEIBO_TEST_DATE = '2017-08-10'
XNR_CENTER_DATE_TIME=int(time.time())      #当前时间

PATH_ROOT = os.path.dirname(os.path.abspath(__file__))

#config es
#config xnr user info

ES_INTELLIGENT_HOST = ['192.168.169.45:9205','192.168.169.46:9205','192.168.169.47:9205']
#['219.224.134.213:9205', '219.224.134.214:9205',\
#                   '219.224.134.215:9205']
ES_INTELLIGENT_PORT = '9205'

ES_CLUSTER_HOST = ['192.168.169.45:9205','192.168.169.46:9205','192.168.169.47:9205']
#['219.224.134.213:9205', '219.224.134.214:9205',\
#                   '219.224.134.215:9205']
ES_CLUSTER_PORT = '9205'

ES_CLUSTER_HOST_2 = ['192.168.169.37:9206','192.168.169.38:9206']
ES_CLUSTER_PORT_2 = '9206'

#config flow text info
ES_FLOW_TEXT_HOST = ['10.128.55.75:9200','10.128.55.76:9200']
#['219.224.134.216:9201', \
#                          '219.224.134.214:9201']
ES_FLOW_TEXT_PORT = '9200' #'9201'

# need three ES identification 
USER_PROFILE_ES_HOST = ['10.128.55.81:9200','10.128.55.82:9200','10.128.55.83:9200']
#['219.224.134.216:9201', \
#                          '219.224.134.214:9201']
USER_PROFILE_ES_PORT = '9200' #'9201'

#config user portrat
ES_USER_PORTRAIT_HOST = ['10.128.55.69:9200','10.128.55.70:9200','10.128.55.71:9200']
#['219.224.134.216:9201', \
#                     '219.224.134.214:9201']
ES_USER_PORTRAIT_PORT = '9200' #'9201'

#es_path
ES_PATH = '/home/pkgs/elasticsearch-1.6.0/' #'/home/ubuntu8/huxiaoqian/elasticsearch-1.6.0/'

#config redis

REDIS_HOST_45 = '192.168.169.45'
REDIS_PORT_45 = '6666'

REDIS_HOST_46 = '192.168.169.46' #'219.224.134.212'
REDIS_PORT_46 = '6666' #'7392'

REDIS_HOST_47 = '192.168.169.47'
REDIS_PORT_47 = ''

REDIS_CLUSTER_HOST_FLOW2 = '10.128.55.68' #'219.224.134.213'
REDIS_CLUSTER_PORT_FLOW2 = '6666'

REDIS_HOST_37 = '192.168.169.37'
REDIS_PORT_37 = '6379'


#redis_path
REDIS_PATH = '/home/pkgs/redis-3.0.5/6666' #'/home/ubuntu7/huxiaoqian/redis-3.0.5/7392/'

# use to identify the db number of redis-97
R_BEGIN_TIME = '2016-03-21'

##　 weibo敏感词redis
REDIS_CLUSTER_HOST_FLOW3 = '219.224.134.214' #'10.128.55.71'
REDIS_CLUSTER_PORT_FLOW3 = '6379'

REDIS_HOST_SENSITIVE = '10.128.55.68'
REDIS_PORT_SENSITIVE = '6379'

#wx redis
REDIS_WX_PORT = '6667'
REDIS_WX_HOST = '192.168.169.45'#'219.224.134.213'

#flow3:retweet/be_retweet redis
RETWEET_REDIS_HOST = '10.128.55.69'
RETWEET_REDIS_PORT = '6379'
#flow3:comment/be_comment redis
COMMENT_REDIS_HOST = '10.128.55.70'
COMMENT_REDIS_PORT = '6379'

#使用七牛来存储捕获到的图片
#2018-1-2 放弃使用七牛，改为存储到本地
qiniu_access_key = "2QHQTgGYH8Ow3dy1jpuSKLAlTo-ZkRav1ty2Nok8"
qiniu_secret_key = "Q91z6hnj5H0LaRkbAN8IPdc8dypdAQ_n21S8tEcu"
qiniu_bucket_name = "publicbucket"
qiniu_bucket_domain = "ovorc2c4c.bkt.clouddn.com"

#微信多媒体数据存放地址
WX_IMAGE_ABS_PATH = '/home/xnr1/xnr_0429/xnr/static/WX/image'
WX_VOICE_ABS_PATH = '/home/xnr1/xnr_0429/xnr/static/WX/voice'

#wx
WX_S_DATE = '2017-10-25'
WX_S_DATE_NEW = '2017-10-25'
WX_S_DATE_ASSESSMENT = '2017-10-25'
WX_GROUP_MESSAGE_START_DATE = '2017-10-25'
WX_GROUP_MESSAGE_START_DATE_ASSESSMENT = '2017-10-25'
WX_GROUP_MESSAGE_START_DATE_ASSESSMENT = '2017-10-25'

#使用百度云语音API进行语音转文字
BAIDU_APP_ID = '10774458'
BAIDU_API_KEY = 'yGA0VfrGCWY86rLwvuYIzX9T'
BAIDU_SECRET_KEY = 'Yj4VZwozKEA3wovNbiBiNCXm37nFo42U'

#wxxnr qqxnr通道可用端口范围
port_range = [6002,6049]
