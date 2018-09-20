#-*-coding:utf-8-*-
import sys
sys.path.append('/home/xnr_overseas/xnr/util_tools/')
sys.path.append('/home/xnr_overseas/xnr_spider/facebook/')
from fb_operate import Operation




# 发帖
def fb_publish(account_name, password, text, tweet_type, xnr_user_no):
    print '123'
    print 'account_name,password..',account_name,password
    operation = Operation(account_name,password)
    print 'operation...',operation
    print operation.publish(text)
    mark = True
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
