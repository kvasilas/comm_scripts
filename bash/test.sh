#!/bin/bash
telnet smtp.example.org 25 <<_EOF
HELO relay.example.org
MAIL FROM:<kcvasilas@gmail.com> #joe@example.org
RCPT TO:<kvasilas@stevens.edu> #jane@example.org
DATA
From: Joe <kcvasilas@gmail.com>
To: Jane <kvasilas@stevens.edug>
Subject: Hello

Hello, world!
.
QUIT
_EOF
