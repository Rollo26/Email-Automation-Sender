import smtplib

email = input("Enter your email: ")
reciever_email = input("RECEIVER EMAIL: ")

subject = input("SUBJECT: ")
message = input("MESSAGE: ")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login(email, "dpow oerg bsbx ardk")

server.sendmail(email, reciever_email, text)

print("Email was sent to " + reciever_email)
