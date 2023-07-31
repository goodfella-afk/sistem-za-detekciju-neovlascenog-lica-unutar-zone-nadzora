#!/usr/bin/env python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from mailassets.readtemplate import read_template
from mailassets.getcontacts import get_contacts
import os

MY_ADDRESS = 'mail@mail.com'
PASSWORD = 'token or 3rd party access key'

def sendmail(imagepath):
    names, emails = get_contacts('mycontacts.txt') # read contacts
    message_template = read_template('message.txt') # read message template

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.mail.me.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact from mycontacts send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # Swap $person_name with first row from mycontacts 
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints message in term for test purpose
        print('\n Alert Sent to >>\n\n',message,'\n')

        # Read img
        with open(imagepath, 'rb') as f:
            img_data = f.read()

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="NEPOZNATA OSOBA"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # add attachment
        image = MIMEImage(img_data, name=os.path.basename(imagepath))
        msg.attach(image)
        
        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    sendmail()
