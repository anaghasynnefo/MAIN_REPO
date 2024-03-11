from flask import Flask, render_template, request, url_for, redirect 
from email.mime.text import MIMEText 
import smtplib 
from email.message import EmailMessage 
app = Flask(__name__) 

@app.route("/") 
def index(): 
	return render_template("index.html") 

@app.route("/sendemail/", methods=['POST']) 
def sendemail(): 
	if request.method == "POST": 
		name = request.form['name'] 
		subject = request.form['Subject'] 
		email = request.form['_replyto'] 
		message = request.form['message'] 

		
		yourEmail = "anagharemesan@gmail.com"
		yourPassword = "123"

		server = smtplib.SMTP('anagharemesan@gmail.com', 587) 
		server.ehlo() 
		server.starttls() 
		server.login(yourEmail, yourPassword) 
		msg = EmailMessage() 
		msg.set_content("First Name : "+str(name) 
						+"\nEmail : "+str(email) 
						+"\nSubject : "+str(subject) 
						+"\nMessage : "+str(message)) 
		msg['To'] = email 
		msg['From'] = yourEmail 
		msg['Subject'] = subject 

		 
		try: 

			server.send_message(msg) 
			print("Send") 
		except: 
			print("Fail to Send") 
			pass
			
	return redirect('/') 

if __name__ == "__main__": 
	app.run(debug=True,port=3000)
