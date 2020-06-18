import csv, smtplib, ssl

message = """Subject: Final Grades

Hi {name},

I hope you are doing well. Your final grade for this school year is a {grade}"""

sender_email = "sender@gmail.com"
password = input("Enter the password for the sender's email: ")

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
	server.login(sender_email, password)
	with open("contacts_for_python_emails_project.csv") as csvfile:
		file = csv.reader(csvfile)
		next(file)
		for name, email, grade in reader:
			server.sendmail(
					sender_email,
					email,
					message.format(name=name, grade=grade),
				)

