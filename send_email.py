import smtplib
import config
encode= encode.encode('utf-8')
def send_email(sub, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message="Subject:".format(subject, msg)
        encode= messenge.encode('utf-8')
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL,message)
        server.quit()
        print("Your email has been sent.")
    except:
        print("Error Your email hasn't been sent.")

subject = "Hello"
msg = "Hello from python auto mail bot!"

send_email(subject, msg)

