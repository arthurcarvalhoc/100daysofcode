from easymail import Email
from smtplib import  SMTP_SSL

user = 'arthurcarvalhoc@gmail.com'
password = 'Pedrinho2014!@#'

e = Email('arthurcarvalhoc@gmail.com', 'arthurcarvalhoc@gmail.com')
e.subject = 'hello world'
e.body = 'with some non-äscii charöcters'

smtp = SMTP_SSL('smtp.gmail.com',465)
smtp.login(user, password)
smtp.sendmail(*e.args,)
