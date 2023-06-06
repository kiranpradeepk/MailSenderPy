import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("sender's_mail", "sender's_password")  #actual password won't work...enable 2 step verification and set up app password(just serach app password in google account settings)
 
message = "msg_to_send"

s.sendmail("sender's_mail", "receiver's_mail", message)
 
# terminating the session
s.quit()