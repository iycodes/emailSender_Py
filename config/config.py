class Config:
    def __init__(self):
        self.body = email_body


email_header_from = "someone"
email_header_to = "you!"
email_subject = "SUBJECT.PDF"
email_body = """\

Hi, AND HI AGAIN
Check out the new post on the Mailtrap blog:
SMTP Server for Testing: Cloud-based or Local?
https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server/
Feel free to let us know what content would be useful for you!

"""
_a = "2E3179616E75306C757741"

# email_address = "pyrxcodes@gmail.com"
# email_password = _b = bytes.fromhex(_a).decode()

auth_details = {
    "email": "pyrxcodes@outlook.com",
    "password": bytes.fromhex(_a).decode(),
}


emails_to_spam = [
    # "shedibalabala123@gmail.com",
    "francbubs@gmail.com",
    # "maguiretoaspiretoperspire@gmail.com",
]
