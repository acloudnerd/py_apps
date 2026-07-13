import smtplib

my_email = "mudaud459@gmail.com"
password = "TondyMudau11"

connection = smtplib.SMTP("smtp.gmail.com", 587)  # my postman
connection.starttls()  # for security
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="matshisevhe.tshepo@gmail.com",  msg = "Subject: Hello\n\nHello Tee")
connection.close()
