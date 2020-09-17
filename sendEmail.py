 # python code to send email  
import smtplib 

# creates SMTP session with port 
s = smtplib.SMTP('smtp.gmail.com', port_num) #replace port_num with portnumber eg. 587

# start TLS for security 
s.starttls() 

# Authentication 
s.login("sender_email_address", "sender_email_address_password") 

# message to be sent 
message = "Message_to_send"

# sending the mail 
s.sendmail("sender_email_address", "receiver_email_address", message) 

s.quit() 
