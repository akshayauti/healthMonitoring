from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)
f = open("check.txt", "r")
str = f.read()
f.close()

emailCre = open("email.txt", "r")
emailCred = emailCre.read()
emailCre.close()

passCre = open("password.txt", "r")
passCred = passCre.read()
passCre.close()

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = emailCred
app.config['MAIL_PASSWORD'] = passCred
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   if str =="Defaulted on the mask":
     msg = Message('warning mask removed', sender = 'gratitudesystems@gmail.com', recipients = ['suhilkoul@gmail.com'])
     msg.body = "Hello this is a mail from system, you should wear your mask properly to not get flagged"
     mail.send(msg)
     return "Sent cause mask was defaulted"
   else:
     return "did not send cause was wearing the mask properly"
  # return "<h2>Welcome to Gratitude the ultimate health safety and health monitoring system.</h2>"

if __name__ == '__main__':
  app.run(debug = True)