from django.http import JsonResponse
from urllib.parse import quote
from random import randint
from django.core.cache import cache

def get_state():
    #随机生成一个八位数
    res = ""
    for i in range(8):
        res += str(randint(0, 9))
    return res

def apply_code(request):
    appid = "6864"
    redirect_uri = quote("https://app6864.acapp.acwing.com.cn/settings/acwing/acapp/receive_code/") 
    scope = "userinfo"
    state = get_state()

    cache.set(state, True, 2 * 60 * 60) #将state存储到redius中，用于确认是否是另一端发送的消息。过期时间为两个小时。    



    return JsonResponse({
        'result': "success", 
        'appid': appid,
        'redirect_uri': redirect_uri, 
        'scope': scope, 
        'state': state
         
    })