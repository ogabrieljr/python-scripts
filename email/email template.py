import smtplib
from string import Template
from pathlib import Path
from email.message import EmailMessage

html = Template(Path("email\index.html").read_text())
content = html.substitute(name="NAME")

msg = EmailMessage()

msg["from"] = "HELLO"
msg['to'] = to
msg['subject'] = 'Subject'

msg.set_content(content, "html")

smtp = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp.ehlo()
smtp.starttls()
smtp.login(strfrom, password)
smtp.send_message(msg)
smtp.quit()
