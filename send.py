import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


mail_content = '''Hello,
This is a test mail.
In this mail we are sending some attachments.
The mail is sent using Python SMTP library.
Thank You
'''
#The mail addresses and password
sender_address = 'sih987659@gmail.com'
sender_pass = 'ABCDE1234'
receiver_address = 'shalinisaigal0@gmail.com'
#Setup the MIME
massege_text = 'A test mail sent by Python. It has an attachment.'




def send_mail(reciever_email, massege_content_1 = mail_content, file_name = "prescription.pdf" ,massege_text1 = massege_text,sender_email = 'sih987659@gmail.com'):
	message = MIMEMultipart()
	message['From'] = sender_email
	message['To'] = receiver_address
	message['Subject'] = massege_text

#The subject line
#The body and the attachments for the mail
	message.attach(MIMEText(mail_content, 'plain'))
	
	attach_file = open(file_name, 'rb') # Open the file as binary mode
	payload = MIMEBase('application', "pdf", Name=file_name)
	payload.set_payload((attach_file).read())
	encoders.encode_base64(payload) #encode the attachment
#add payload header with filename
	payload.add_header('Content-Decomposition', 'attachment', filename=file_name)
	message.attach(payload)
#Create SMTP session for sending the mail
	session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
	session.starttls() #enable security
	session.login(sender_address, sender_pass) #login with mail_id and password
	text = message.as_string()
	session.sendmail(sender_address, receiver_address, text)
	session.quit()
	print('Mail Sent')

#send_mail('shalinisaigal0@gmail.com',mail_content,"prescription.pdf",massege_text,'sih987659@gmail.com')
