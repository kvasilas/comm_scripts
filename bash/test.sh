#!/bin/bash
telnet smtp.example.org 25 <<_EOF
HELO relay.example.org
MAIL FROM:<myemail@gmail.com> #joe@example.org
RCPT TO:<myemail2@gmail.com> #jane@example.org
DATA
From: Joe <myemail@gmail.com>
To: Jane <myemail2@gmail.com>
Subject: Hello

Hello, world!
.
QUIT
_EOF
