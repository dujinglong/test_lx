#
# from data import setting
# from report.log import atp_log
# import yagmail
#
#
# def sendmail(title, content, attrs=None):
#     m = yagmail.SMTP(host=setting.MAIL_HOST, user=setting.MAIL_USER,
#                      password=setting.MAIL_PASSWORD, smtp_ssl=True
#                  )
#     m.send(to=setting.TO, subject=title,
#            contents=content,
#            attachments=attrs)
#     atp_log.info('发送邮件完成')