import codecs
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

strFrom = emailfrom
strTo = emailto

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'SUBJECT'
msgRoot['From'] = strFrom
msgRoot['To'] = strTo

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('')
msgAlternative.attach(msgText)

html = codecs.open("index.html", "r", "utf-8")
msgText = MIMEText(html.read(), 'html')
msgAlternative.attach(msgText)

fp = open("../imaging\images\danielle-rice-LbCtwTksU5w-unsplash.jpg", 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

smtp = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp.ehlo()
smtp.starttls()
smtp.login(strFrom, password)
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
smtp.quit()
