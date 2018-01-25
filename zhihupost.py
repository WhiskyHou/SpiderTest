# encoding=utf-8
import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib
import re
import time
import os.path
try:
    from PIL import Image
except:
    pass


# 构造 Request headers
agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': agent
}

# 使用登录cookie信息
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")


# 获取验证码
def get_captcha():
    t = str(int(time.time() * 1000))
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    # 用pillow 的 Image 显示验证码
    # 如果没有安装 pillow 到源代码所在的目录去找到验证码然后手动输入
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    captcha = input("please input the captcha\n>")
    return captcha


def isLogin():
    # 通过查看用户个人信息来判断是否已经登录
    url = "https://www.zhihu.com/settings/profile"
    login_code = session.get(url, headers=headers, allow_redirects=False).status_code
    if login_code == 200:
        return True
    else:
        return False


def login(secret, account):
    headers["X-Requested-With"] = "XMLHttpRequest"
    # 通过输入的用户名判断是否是手机号
    if re.match(r"^1\d{10}$", account):
        print("手机号登录 \n")
        post_url = 'https://www.zhihu.com/login/phone_num'
        postdata = {
            'password': secret,
            'phone_num': account
        }
    else:
        if "@" in account:
            print("邮箱登录 \n")
        else:
            print("你的账号输入有问题，请重新登录")
            return 0
        post_url = 'https://www.zhihu.com/login/email'
        postdata = {
            'password': secret,
            'email': account
        }
    # 不需要验证码直接登录成功
    login_page = session.post(post_url, data=postdata, headers=headers)
    print(login_page.content)
    r = requests.get("http://zhihu.com")
    print(r.text)
    login_code = login_page.json()
    if login_code['r'] == 1:
        # 不输入验证码登录失败
        # 使用需要输入验证码的方式登录
        postdata["captcha"] = get_captcha()
        login_page = session.post(post_url, data=postdata, headers=headers)
        print(login_page.content)
        r = requests.get("http://zhihu.com", cookies=cookielib.LWPCookieJar(filename='cookies'))
        print(r.text)
        login_code = login_page.json()
        print(login_code['msg'])
    # 保存 cookies 到文件，
    # 下次可以使用 cookie 直接登录，不需要输入账号和密码
    session.cookies.save()

try:
    input = raw_input
except:
    pass


if __name__ == '__main__':
    if isLogin():
        print('您已经登录')
        cookies = '_zap=871dff53-fca9-4c56-b8dd-7e30a819d2ca; _xsrf=f4505c69f9aea21426bc2c4cafdafb03; d_c0="ADCjVCJm9QyPTphs3lm0WhYvupfIbBuQPCk=|1515406875"; __utma=51854390.2083587178.1515406875.1515406875.1515406875.1; __utmz=51854390.1515406875.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100-1|2=registration_date=20151016=1^3=entry_date=20151016=1; q_c1=fbaae3cc7eaf4939aa25b1b2dd29fd8a|1516766682000|1509117430000; aliyungf_tc=AQAAAGDQzlrBMgwArzPCbzOL5Q4/TV5z; _xsrf=f4505c69f9aea21426bc2c4cafdafb03; r_cap_id="ZWU4ODk0YmFjMjFkNGE4N2JjNGY4NTI4MmYyMTQ5Yzc=|1516868001|3627df131b1b45c2c46ac79a364a3df2db93cc85"; cap_id="OWUyMzE0YmM5YWE5NGI1MDgzM2E4M2I5ZWNhMDY5ZjA=|1516868001|e66953f6a5b75f808a3d132bc0d719c13ed58b93"; l_cap_id="N2I0NjI1ODdmMmE3NDNjNmJhNWE3NTUzOTg4ZmRmZDY=|1516868001|05dbc5aa61dcab6f18db173202c735906496552c"; capsion_ticket="2|1:0|10:1516870714|14:capsion_ticket|44:YTc0MzVkYTkyYzc5NGMzYmJhZTEzODVmZTYzMzE3MTE=|03df9369e17815d84ecfc5a77ebd5bd5f4c68f4f6ea70ee783149a4077adab01"; z_c0="2|1:0|10:1516870715|4:z_c0|92:Mi4xeHNJeEFnQUFBQUFBTUtOVUltYjFEQ1lBQUFCZ0FsVk5PLXBXV3dBSUhKSEhuT0FYZzJLX1B0MURobHd5b3UwQmxn|0430edcf8d445c4ca15f3dc539a0277c2b66729be86ca7341d34543969f5c451"'
        r = session.get("http://www.zhihu.com")
        print(r.text)
    else:
        account = input('请输入你的用户名\n>  ')
        secret = input("请输入你的密码\n>  ")
        login(secret, account)