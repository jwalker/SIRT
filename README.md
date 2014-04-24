SMTP Internal Relay Tool aka (SIRT.py)

Can be use to check for SMTP relay servers and send (spoofed) emails of chosen target.

I wrote this tool on during an assessment, where vulnerability scanner had identified
a few mail servers. Instead of trying to check each system for internal relays, it was
much easier to have the script do it for me. 

The basis of the script reads in a targets.txt (or any filename you give it) and iterates
over each line to connect and send an email to a possibly known internal user of that 
environment. The script comes in handy to just identify servers that open to relaying messages
or for social engineering.

## Usage:
```
./sirt.py <smtp_servers.txt> <client/hostname> <target@hostname.com> <spoofed@hostname.com> <Subject> <data to send>

./sirt.py targets.txt gmail.com sirttest@mailismagic.com support@helpdesk.me "Testing your SE training" "Click All The Links"
Got all arguments

[+] Testing SMTP server: 127.0.0.1
send: 'ehlo [X.X.X.X]\r\n'
reply: '250-ext-shell Hello localhost [127.0.0.1], pleased to meet you\r\n'
reply: '250-ENHANCEDSTATUSCODES\r\n'
reply: '250-PIPELINING\r\n'
reply: '250-8BITMIME\r\n'
reply: '250-SIZE\r\n'
reply: '250-DSN\r\n'
reply: '250-ETRN\r\n'
reply: '250-DELIVERBY\r\n'
reply: '250 HELP\r\n'
reply: retcode (250); Msg: ext-shell Hello localhost [127.0.0.1], pleased to meet you
ENHANCEDSTATUSCODES
PIPELINING
8BITMIME
SIZE
DSN
ETRN
DELIVERBY
HELP
send: 'mail FROM:<support@helpdesk.me> size=240\r\n'
reply: '250 2.1.0 <support@helpdesk.me>... Sender ok\r\n'
reply: retcode (250); Msg: 2.1.0 <support@helpdesk.me>... Sender ok
send: 'rcpt TO:<sirttest@mailismagic.com>\r\n'
reply: '250 2.1.5 <sirttest@mailismagic.com>... Recipient ok\r\n'
reply: retcode (250); Msg: 2.1.5 <sirttest@mailismagic.com>... Recipient ok
send: 'data\r\n'
reply: '354 Enter mail, end with "." on a line by itself\r\n'
reply: retcode (354); Msg: Enter mail, end with "." on a line by itself
data: (354, 'Enter mail, end with "." on a line by itself')
send: 'Content-Type: text/plain; charset="us-ascii"\r\nMIME-Version: 1.0\r\nContent-Transfer-Encoding: 7bit\r\nTo: Recipient <sirttest@mailismagic.com>\r\nFrom: "support@helpdesk.me" <support@helpdesk.me>\r\nSubject: Testing your SE training\r\n\r\nClick All The Links\r\n.\r\n'
reply: '250 2.0.0 s3OLtDNB011330 Message accepted for delivery\r\n'
reply: retcode (250); Msg: 2.0.0 s3OLtDNB011330 Message accepted for delivery
data: (250, '2.0.0 s3OLtDNB011330 Message accepted for delivery')
send: 'quit\r\n'
reply: '221 2.0.0 ext-shell closing connection\r\n'
reply: retcode (221); Msg: 2.0.0 ext-shell closing connection
```
