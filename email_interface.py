import smtplib
import time
import imaplib
import email

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "bobbytables2019" + ORG_EMAIL
FROM_PWD    = "Xt55OyItnw8BuL9WCwt1"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

def readmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('Inbox',readonly=True)

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])

                    if (isSpam(msg)):
                        print("SPAM!")
                    else
                        print("Not spam.")

                    #email_subject = msg['subject']
                    #email_from = msg['from']
                    #print('From : ' + email_from)
                    #print('Subject : ' + email_subject)
                    #for part in msg.walk():
                        # each part is a either non-multipart, or another multipart message
                        # that contains further parts... Message is organized like a tree
                        #if part.get_content_type() == 'text/plain':
                            #print part.get_payload() # prints the raw text
                    #print('\n')

    except Exception, e:
        print str(e)

readmail()
