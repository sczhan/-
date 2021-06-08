
from email.header import Header
from email.mime.text import MIMEText

msg = MIMEText("Hello wold",  "plain", "utf-8")
# 下面代码故意写错，说明，所谓的发送者的地址，只是从一个Header的第一个参数作为字符串构建的内容
# 用utf8编码是因为很可能内容包含非英文字符
header_from = Header("从5481493@qq.com发出去的<5481493@qq.cn>", "utf-8")
msg['From'] = header_from

# 填写接受者信息
header_to = Header("去scwyzhan@sina.com的地方<scwyzhan@sina.com>", 'utf-8')
msg['To'] = header_to

header_sub = Header("这是我的主题", 'utf-8')
msg['Subject'] = header_sub

# 发送email地址，此处地址直接使用我的qq邮箱，密码一般需要临时输入，此处偷懒
from_addr = "5481493@qq.com"
# 此处密码是经过申请设置后的授权码，不是不是不是你的qq邮箱密码
from_pwd = "njnlfzzzmlhubgge"

# 收件人信息
# 此处使用qq邮箱，我给自己发送
to_addr = "scwyzhan@sina.com"


# 输入SMTP服务器地址
# 此处根据不同的邮件服务商有不同的值，
# 现在基本任何一家邮件服务商，如果采用第三方收发邮件，都需要开启授权选项
# 腾讯qq邮箱所的smtp地址是 smtp.qq.com

smtp_srv = "smtp.qq.com"

try:
    import smtplib
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465) #SMTP协议默认端口25
    # 登录邮箱发送
    srv.login(from_addr, from_pwd)
    # 发送邮件
    # 三个参数
    # 1. 发送地址
    # 2. 接受地址，必须是list形式
    # 3. 发送内容，作为字符串发送
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()
except Exception as e:
    print(e)