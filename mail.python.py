# Python script for sending mail via gmail SMTP

#import smtplib
#import random


#host = 'smtp.gmail.com'
#port = '587'
#user = 'akhilraj.app@gmail.com'
#passw = '**********'
#i = 0

#server = smtplib.SMTP()
#server.connect(host, port)
#server.ehlo()
#server.starttls()
#server.login(user, passw)


#while i < 1:
   # randno = random.randrange(0, 99999)
   # notice = "Finished %s" % randno
   # tolist = "akhilrajns@gmail.com"
   # fromaddr = "Mailer Application"
   # subject = "Pyhon mailer %d" % randno
   # message = '''This is My test Python SMTP Mail %s and from email %s ''' % (notice,user)
   # hdr = "From: %s\r\nTo: %s\r\nSubject: %s\r\nMIME-Version: 1.0\r\nContent-type: text/html\r\nX-Mailer: My-Mail\r\n\r\n" % (fromaddr, tolist, subject)
   # try:
      #  server.sendmail("akhilraj.app@gmail.com", tolist, hdr+message)
       # print 'Success'
    #except Exception, exc:
       # print 'Mail send Failed',exc
   # i=i+1

#server.quit
#import MySQLdb
# Open database connection
#db = MySQLdb.connect("127.0.0.1","root","","demo_tc" )

# prepare a cursor object using cursor() method
#cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
#sql = "SELECT * FROM languages"
#try:
   # Execute the SQL command
  # cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   #results = cursor.fetchall()
   #for row in results:
      #language = row[1]
     # fb_locale_code = row[2]
      # Now print fetched result
      #print "language=%s,fb_locale_code=%s" %(language, fb_locale_code)
#except:
   #print "Error: unable to fecth data"

# disconnect from server
#db.close()

#import time
from threading import Thread

def myfunc(i):
    print "sleeping 5 sec from thread %d \n" % i
    print "finished sleeping from thread %d \n" % i

for i in range(10):
    t = Thread(target=myfunc, args=(i,))
    t.start()
