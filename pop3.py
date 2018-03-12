import poplib
email = raw_input('Email:')
passsword = raw_input('Password')
pop3_server = raw_input('POP3 server')

server = poplib.POP3(pop3_server)
server.set_debuglevel(1)
prinf(server.getwelcome().decode('utf-8'))
server.user(email)
server.pass_(password)

print('messages %s. size %s'%server.stat())
resp,mails,octets = server.list()
index = len(mails)
resp,mails,octets = server.retr(index)

msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)
server.quit()
