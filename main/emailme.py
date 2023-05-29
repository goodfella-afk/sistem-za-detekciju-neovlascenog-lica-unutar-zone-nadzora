import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from mailassets.readtemplate import read_template
from mailassets.getcontacts import get_contacts
from email.mime.image import MIMEImage
import os

MY_ADDRESS = 'zivkovicbusiness@icloud.com'
PASSWORD = 'gnbe-hoqe-bozy-kvmc'

def sendmail(imagepath):
    names, emails = get_contacts('mycontacts.txt') # read contacts
    message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.mail.me.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        print(message)

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
