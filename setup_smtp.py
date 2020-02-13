import smtplib
# set up the SMTP server
s = smtplib.SMTP(host=' smtp.gmail.com.', port=587)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)