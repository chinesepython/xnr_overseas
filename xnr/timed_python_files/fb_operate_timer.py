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
from fb_tweet_func import fb_publish, fb_retweet, fb_comment


# publish-发帖、retweet-转发、comment-评论、like-点赞、follow-关注、unfollow-取消关注、at-提到、private-私信
# add-发送添加好友请求、confirm-确认好友请求、delete-删除好友请求
# receive - 回复


def tweet_out_of_redis():


    while 1:    
        mark = False
        print re.lrange(FB_TWEET_PARAMS, 0, 10)
        tweet_params = re.rpop(FB_TWEET_PARAMS)
        if tweet_params:
            tweet_dict = json.loads(tweet_params)
            channel = tweet_dict['channel']
            operate_type = tweet_dict['operate']
            if channel == "facebook" and operate_type == "publish":
                print "facebook publish tweet =========================================================================channel = facebook operate_type = publish"

                account_name = tweet_dict['account_name']
                password = tweet_dict['password']
                text = tweet_dict['text']
                tweet_type = tweet_dict['tweet_type']
                xnr_user_no = tweet_dict['xnr_user_no']
                print "account_name, password, text, tweet_type, xnr_user_no,channel, operate_type----------------------------------"
                print account_name, password, text, tweet_type, xnr_user_no,channel, operate_type
                try:
                    mark = fb_publish(account_name, password, text, tweet_type, xnr_user_no)
                except Exception as e:
                    print e
                    send_email_to('80617252@qq.com', '/home/xnr_overseas/xnr/timed_python_files/fb_operate_timer.py/publish'.format(e))

            elif channel == "facebook" and operate_type == "retweet":
                print "facebook publish retweet =========================================================================channel = facebook operate_type = retweet"

                account_name = tweet_dict['account_name']
                password = tweet_dict['password']
                _id = tweet_dict['_id']
                uid = tweet_dict['uid']
                text = tweet_dict['text']
                tweet_type = tweet_dict['tweet_type']
                xnr_user_no = tweet_dict['xnr_user_no']
                   
                print "account_name, password, text, tweet_type, xnr_user_no,channel, operate_type----------------------------------"
                print account_name, password, _id, uid, text, tweet_type, xnr_user_no, channel, operate_type
                send_email_to('80617252@qq.com', 'will publish account_name is{}'.format(account_name))
                try:
                    mark = fb_retweet(account_name, password, _id, uid, text, tweet_type, xnr_user_no)
                except Exception as e:
                    print e
                    send_email_to('80617252@qq.com', '/home/xnr_overseas/xnr/timed_python_files/fb_operate_timer.py/retweet'.format(e))

            elif channel == "facebook" and operate_type == "comment":
                print "facebook publish retweet =========================================================================channel = facebook operate_type = retweet"

                account_name = tweet_dict['account_name']
                password = tweet_dict['password']
                _id = tweet_dict['_id']
                uid = tweet_dict['uid']
                text = tweet_dict['text']
                tweet_type = tweet_dict['tweet_type']
                xnr_user_no = tweet_dict['xnr_user_no']
                   
                print "account_name, password, text, tweet_type, xnr_user_no,channel, operate_type----------------------------------"
                print account_name, password, _id, uid, text, tweet_type, xnr_user_no, channel, operate_type
                send_email_to('80617252@qq.com', 'will publish account_name is{}'.format(account_name))
                try:
                    mark = fb_comment(account_name, password, _id, uid, text, tweet_type, xnr_user_no)
                except Exception as e:
                    print e
                    send_email_to('80617252@qq.com', '/home/xnr_overseas/xnr/timed_python_files/fb_operate_timer.py/comment'.format(e))

        else:
            print 'will end because no task in redis'
            break
    return mark    


if __name__ == "__main__":
    mark = tweet_out_of_redis()
    print mark





