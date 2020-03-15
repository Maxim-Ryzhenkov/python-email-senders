import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Конфигурация
port = 465  # для SSL подключения
smtp_server = "smtp.yandex.ru"  # или, например, smtp.gmail.com
sender_email = "xxxxxxxxx@yandex.ru"
receiver_email = "xxxxxxxxxxx@gmail.com"
password = "xxxxxxxxxx"


message = MIMEMultipart("alternative")
message["Subject"] = "Тестовый отчёт"
message["From"] = sender_email
message["To"] = receiver_email

text = """\
Привет!
У нас всё работает!
Отправлено из скрипта!"""

html = """\
<html>
  <body>
    <p>Привет!<br>
       У нас всё работает!<br>
       <i><h3>Отправлено из скрипта с html форматированием!</h3></i>
    </p>
  </body>
</html>
"""

# Сделать их текстовыми\html объектами MIMEText
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Внести HTML\текстовые части сообщения MIMEMultipart
# Почтовый клиент сначала попытается отрендерить последнюю часть
message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
