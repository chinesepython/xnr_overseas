# -*-coding:utf-8-*-
# 本文件作为定时执行的文件，从redis取出参数------发帖。
# fb_tweet_timer.py

import json
import sys

sys.path.append('/home/xnr_overseas/xnr/util_tools/')
sys.path.append('/home/xnr_overseas/xnr/facebook_info/')
sys.path.append('/home/BingquLee/xnr2/xnr_0429/xnr/')
from global_utils1 import FB_TWEET_PARAMS, RE_QUEUE as re
from send_mail import send_email_to
from fb_tweet_func import fb_publish



def tweet_out_of_redis():


    while 1:    
        mark = False
        # 此处应该有while true循环 不断弹出redis任务      
        print re.lrange(FB_TWEET_PARAMS, 0, 10)
        tweet_params = re.rpop(FB_TWEET_PARAMS)
        if tweet_params:
            tweet_dict = json.loads(tweet_params)
            account_name = tweet_dict['account_name']
            password = tweet_dict['password']
            text = tweet_dict['text']
            tweet_type = tweet_dict['tweet_type']
            xnr_user_no = tweet_dict['xnr_user_no']
            print account_name, password, text, tweet_type, xnr_user_no
            send_email_to('80617252@qq.com', 'will publish account_name is{}'.format(account_name))
            mark = fb_publish(account_name, password, text, tweet_type, xnr_user_no)
        else:
            print 'will end because no task in redis'
            break
    return mark    


if __name__ == "__main__":
    mark = tweet_out_of_redis()
    print mark





