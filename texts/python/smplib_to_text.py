import smtplib
#max 158 char
def send_text_gateway_unknown(number, msg):
    gateways = ['@txt.att.net', '@messaging.sprintpcs.com','@pm.sprint.com', '@tmomail.net', 
                '@vtext.com', '@myboostmobile.com', '@sms.mycricket.com', '@mymetropcs.com',
                '@mmst5.tracfone.com', '@email.uscc.net', '@vmobl.com']
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login('el.senor456@gmail.com', 'dickdogg')
    for i in gateways:
        server.sendmail('el senor', number+i, msg+'\n')
    #server.sendmail('el senor', '3476965266@vtext.com', msg+'\n')
    server.quit()


def senf_text(number, msg, num):
    gateways = ['@txt.att.net', '@messaging.sprintpcs.com', '@pm.sprint.com', '@tmomail.net',
                '@vtext.com', '@myboostmobile.com', '@sms.mycricket.com', '@mymetropcs.com',
                '@mmst5.tracfone.com', '@email.uscc.net', '@vmobl.com']
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login('el.senor456@gmail.com', 'dickdogg')
    server.sendmail('el senor', number+gateways[num], msg+'\n')
    server.quit()

if __name__ == "__main__":
    #msg = "Did you ever hear the Tragedy of Darth Plagueis the wise? I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a D"       
    # send_text_gateway_unknown('3479960281', msg)
    # send_text_gateway_unknown('18455198309', msg)
    senf_text('7185703910', 'i like to eat eat eat, apples and banannas',4)
