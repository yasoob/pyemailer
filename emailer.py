import smtplib
import sys

class Email(object):
    def __init__(self):
        self.header()
        self.usage()
        self.get_userlist()
        self.get_info()
        self.get_credentials()
        self.prepare_message()
        self.set_config()
        self.send_email()
    
    def header(self):
        print "-----------------++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-----------------"
        print "-----------------++++++++++++++++++++++++++++++++++++++--Yasoob's bulk email sender--++++++++++++++++++++++++++++++++++++++++++-----------------"
        print "-----------------++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-----------------"

    def usage(self):
        print " get the txt file containing the email addresses of recepients. Each email is written on a separate line"
        print " for example"
        print " someone@some.com"
        print " otherperson@other.com"
        print " and so on"
        
    def get_userlist(self):
        global recepients
        users = raw_input("\n[email sender]  recepients file name:  ")
        if ".txt" in users:
            pass
        else:
            print "[email sender]  this is not a valid txt file"
            sys.exit()
        recepients = []
        try:
            with open(users) as i:
                user_list = i.readlines()
            for i in user_list:
                recepients.append(i.strip("\n"))
        except IOError :
            print "[email sender]  invalid recepients file"
            sys.exit()
        
    def get_info(self):
        global FROM,TO,SUBJECT,TEXT    
        FROM = raw_input("[email sender]  from:  ")
        TO = recepients 
        SUBJECT = raw_input("[email sender]  subject:  ")
        TEXT = raw_input("[email sender]  message:  ")
        
    def get_credentials(self):
        global username,password
        username = raw_input("[email sender]  your username:  ")
        password = raw_input("[email sender]  your password:  ")    
    
    def prepare_message(self):
        global headers,body
        headers = ["From: " + FROM,
            "Subject: " + SUBJECT,
            "To: " + ", ".join(TO),
            "MIME-Version: 1.0",
            "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        body = "" + TEXT + ""
        
    def set_config(self):
        global host
        if "gmail.com" in username:
            host = "smtp.gmail.com:587"
        elif "ymail.com" in username:
            host = "smtp.ymail.com:587"
        elif "live.com" in username:
            host = "smtp.live.com:587"
        else:
            print "[email sender]  there was something wrong"
            sys.exit()
    
    def send_email(self):  
        server = smtplib.SMTP(host)
        server.starttls()
        server.login(username,password)
        server.sendmail(FROM, TO, headers + "\r\n\r\n" + TEXT)
        server.quit()

if __name__ == "__main__":
    try:
        a = Email()
    except KeyboardInterrupt:
        print "\n[email sender]  The program was closed by the user.\n"
