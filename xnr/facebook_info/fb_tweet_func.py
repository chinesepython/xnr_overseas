#-*-coding:utf-8-*-
import sys
sys.path.append('/home/xnr_overseas/xnr/util_tools/')
sys.path.append('/home/xnr_overseas/xnr_spider/facebook/')
from fb_operate import Operation
from send_mail import send_email_to



# 发帖
def fb_publish(account_name, password, text, tweet_type, xnr_user_no):
    print 'account_name,password..',account_name,password
    try:
        operation = Operation(account_name,password)
        print 'operation...',operation
        print operation.publish(text)
        mark = True
    except Exception as e:
        send_email_to('80617252@qq.com', 'somethin occur in your project details is /home/xnr_overseas/xnr/facebookinfo/fb_tweet_func{}'.format(e))
    # except:
    #     mark = False

    #message_type = 1 # 原创

    #try:
    #save_mark = fb_save_to_xnr_flow_text(tweet_type,xnr_user_no,text,message_type)
    #print 'save_mark..',save_mark
    #except:
    #    print '保存微博过程遇到错误！'
    #    save_mark = False

    return mark


# 转发
def fb_retweet(account_name, password, _id, uid, text, tweet_type, xnr_user_no):

    operation = Operation(account_name,password)
    _id = _id.split('_')[1]
    print 'fid', _id, type(_id)
    try:
        print operation.share(uid, _id, text)
    except Exception as e:
        send_email_to('80617252@qq.com', 'somethin occur in your project details is /home/xnr_overseas/xnr/facebookinfo/fb_tweet_func{}'.format(e))

    return True


# 评论
def fb_comment(account_name, password, _id, uid, text, tweet_type, xnr_user_no):

    operation = Operation(account_name,password)
    print '===============================------------------------------================================-------------------======================-------------------============'
    print _id, "--------------------------------------------------------" 
    _id = _id.split('_')[1]
    print uid, _id
    #try:
    try:
        print operation.comment(uid,_id,text)
    except Exception as e:
        send_email_to('80617252@qq.com', 'somethin occur in your project details is /home/xnr_overseas/xnr/facebookinfo/fb_tweet_func{}'.format(e))

    return True
