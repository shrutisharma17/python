import smtplib

#sender's details
sender_mail = input("Enter the e-mail i'd of the sender: ")
sender_name = input("Enter the name of the sender: ")
sender_email_id_password = input("Enter password of sender's e-mail:")

#receiver's details
receiver_mail = input("Enter the e-mail i'd of the receiver: ")
receiver_name = input("Enter the name of the receiver: ")

#e-mail's details
subject = input("Enter the subject of the e-mail: ")
body = input("Enter the body of the e-mail: ")

message = f"""
            From: {sender_name}
                  {sender_mail}
            To: {receiver_name}
                {receiver_mail}
            Subject: {subject}

            {body}"""

try:
   s = smtplib.SMTP('smtp.gmail.com', port=587)

   # start TLS for security
   s.starttls()
  
   # Authentication
   s.login(sender_mail, sender_email_id_password)
  
   # sending the mail
   s.sendmail(sender_mail, receiver_mail,  message)
  
   # terminating the session
   s.quit() 
        
   print("Successfully sent email")
except smtplib.SMTPException as excep:
   print("Error: unable to send email ...", excep)