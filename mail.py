# Python script for sending mail via gmail SMTP
import smtplib
import random
from threading import Thread
import Queue
import MySQLdb
import re

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email import Utils


END_OF_WORK = "ENDOFWORK"


class Sendmail(Thread):
    def __init__(self,que_email,threadno):
        Thread.__init__(self)
        self.sendmailQ = que_email
        self.theradno = threadno

    def stop(self):
        self._Thread__stop()


    def run(self):
        while True:

            email = self.sendmailQ.get()

            if email == END_OF_WORK:
                Sendmail.stop(self)
                print "All threads stopped",self.theradno
                break

            mail(email)


            

def mail(email):
    host = 'smtp.gmail.com'
    port = '587'
    user = 'akhilraj.app@gmail.com'
    password = '9744894237'

    fromaddr = "Mailer Application"
    fromAddress = Utils.formataddr((fromaddr,user))
    toAddress = "akhilrajns@gmail.com"


    randno = random.randrange(0, 99999)


    subject = "Python mailer %d" % randno
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['From'] = fromAddress
    msgRoot['To'] = toAddress
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)


    ft = open('mail-content.html', 'rb')
    msgTexts = MIMEText(ft.read(), 'html',_charset="utf-8")
    ft.close()
    msgAlternative.attach(msgTexts)

    # We reference the image in the IMG SRC attribute by the ID we give it below
    #msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><img src="cid:image2"><br>Nifty!', 'html')
    #msgAlternative.attach(msgText)


    # This example assumes the image is in the current directory
    fp = open('images/moneybooker.jpeg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp2 = open('images/payex.png', 'rb')
    msgImage2 = MIMEImage(fp2.read())
    fp.close()
    fp2.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)
    msgImage2.add_header('Content-ID', '<image2>')
    msgRoot.attach(msgImage2)



    smtp = smtplib.SMTP()
    smtp.connect(host, port)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user, password)
    #mailid = re.sub("([(',)])","",str(email))
    #print 'mail send to ',mailid

    try:
        smtp.sendmail(user, toAddress, msgRoot.as_string())
        print 'Success'
    except Exception, exc:
        print 'Mail send Failed',exc

    smtp.quit
# Open database connection
db = MySQLdb.connect("127.0.0.1","root","","demo_tc")

# prepare a cursor object using cursor() method



no = raw_input("Enter  the count:")


cursor = db.cursor()
sql = "SELECT Email FROM subscribers LIMIT %d" % int(no)
cursor.execute(sql)
results = cursor.fetchall()
db.close()
que_email = Queue.Queue()

threadcount = 2

for emails in results:
    que_email.put(emails)

for i in range(threadcount):
    que_email.put(END_OF_WORK)




threads = []

for i in range(threadcount):
    #t = Thread(target=mail, args=(que_email,))
    t = Sendmail(que_email,i)
    t.setDaemon(True)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
    
del threads
del que_email

print "\n send all mails"








