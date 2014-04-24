#!/usr/bin/python
# Author: Jacolon Walker
# SMTP Internal Relay Tool (SIRT)
import smtplib
import email.utils
from email.mime.text import MIMEText
import logging, sys

# check for arguments
if len(sys.argv) < 5:
	sys.exit('Usage: %s <smtp_servers.txt> <client/hostname> <target@hostname.com> <spoofed@hostname.com> <Subject> <data to send>' %sys.argv[0])
else:
	print "Got all arguments"
	smtp_file = sys.argv[1]
	hostname = sys.argv[2]
	rcpt = sys.argv[3]
	fromaddr = sys.argv[4]
	subject = sys.argv[5]
	data = sys.argv[6]

# SMTP internal relay check
def sirc(smtp_file, hostname, rcpt, fromaddr, subject, data):
	# SMTP empty array
	smtpsvrs = []

	# Build the array from the files and close immediately
	# store it in memory to reduce file reads
	file = open(smtp_file)
	for line in file:
		smtpsvrs.append(line.rstrip())
	file.close()


	# Loop through smtp servers
	for smtp in smtpsvrs:
		msg = MIMEText(data)
		msg['To'] = email.utils.formataddr(('Recipient', rcpt))
		msg['From'] = email.utils.formataddr((fromaddr, fromaddr))
		msg['Subject'] = subject

		server = smtplib.SMTP(smtp)
		print "\n[+] Testing SMTP server: %s" %(smtp)
		server.set_debuglevel(True) # show communication with the server
		try:
			server.sendmail(fromaddr, [rcpt], msg.as_string())
		except smtplib.SMTPRecipientsRefused:
			continue
		finally:
			server.quit()

if __name__ == '__main__':
	sirc(smtp_file, hostname, rcpt, fromaddr, subject, data)
