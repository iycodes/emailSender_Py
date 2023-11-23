import smtplib
import os
import sys
from time import sleep
import asyncio
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

sys.path.append("config")
import config

#


def yes_or_no_input(text):
    res = input(
        f"""/
{text}
1) yes
2) no 
: """
    )
    while True:
        match res:
            case "yes" | "1" | "y":
                # recall = False
                res = True
                break
            case "no" | "2" | "n":
                # recall = False
                res = False
                break

            case _:
                yes_or_no_input(text)
    return res


login_details = config.auth_details

title = "test mail"
message = "body of test mail"

text = f"Subject:{title}\n\n{message}"

#
smpt_server = {
    "gmail": "smtp.gmail.com",
    "outlook": "smtp-mail.outlook.com",
    "mailru": "smtp.mail.ru",
}

smpt_port = {"outlook": 587, "mailru": 465}

smpt_passwords = {}

smpt_port = 587
app_password = {
    "gmail": "bqvynvgajziackqg ",
    "outlook": ".Iyanu0luwafan0r0",
}
print("Welcome..")

res = yes_or_no_input("Use Default Email?")
if res == False:
    login_details["email"] = input("Type in Outlook Email : ")
    login_details["password"] = input("Type in password : ")
    print(login_details)


message = MIMEMultipart()

# add in header
message["From"] = Header(config.email_header_from)
message["To"] = Header(config.email_header_to)
message["Subject"] = Header(config.email_subject)

# attach message body as MIMEText
message.attach(
    MIMEText(
        config.email_body,
        "plain",
        "utf-8",
    )
)


def add_attachment():
    # locate and attach desired attachments
    att_name = os.path.basename("data.txt")
    _f = open("data.txt", "rb")
    att = MIMEApplication(_f.read(), _subtype="txt")
    _f.close()
    att.add_header("Content-Disposition", "attachment", filename=att_name)
    message.attach(att)


server = smtplib.SMTP("smtp-mail.outlook.com", 587)
server.starttls()
server.login(login_details["email"], login_details["password"])


async def sendMail():
    print("Starting.....")
    for email in config.emails_to_spam:
        # try:
        server.sendmail(login_details["email"], email, message.as_string())
        # except Exception as e:
        #     # print(e)
        #     print("error Sending..")
        #     return

        print(f"SENT SUCCESFULLY TO {email} ")
        print(f"waiting {config.delay} seconds")
        await asyncio.sleep(config.delay)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(sendMail())
    finally:
        loop.close()
