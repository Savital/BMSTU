import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import COMMASPACE, formatdate
from email import encoders
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

WRONG_FILE = 1
PASS = 0
FILE_ERROR = -1
ACCESS_ERROR = -2

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.UI = uic.loadUi("mainForm.ui", self)
        self.construct()

    def construct(self):
        print("construct")
        self.btnSend.clicked.connect(lambda: onBtnSend(self))

def checkUser(user):
    if user.strip() == '':
        return False
    return True
def checkPassword(password):
    if password.strip() == '':
        return False
    return True
def checkSendTo(sendTo):
    if sendTo.strip() == '':
        return False
    return True
def checkFilename(filename):
    if filename.strip() == '':
        return False
    return True
def checkKeyword(keyword):
    if keyword.strip() == '':
        return False
    return True

def processFile(user, password, sendTo, filename, keyword, textOutput):
    try:
        with open(filename, 'r') as f:
            text = f.read()
            f.close()
            if keyword in text:
                textOutput = f'Find keyword "{keyword}" in {filename}...\n'
            else:
                return WRONG_FILE
    except Exception:
        return FILE_ERROR

    # Multipurpose Internet Mail Extensions
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(filename, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(filename))

    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = COMMASPACE.join(sendTo)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = 'Message'
    msg.attach(part)

    try:
        # Secure Sockets Layer
        server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server_ssl.ehlo()
        server_ssl.login(user, password)
        server_ssl.sendmail(user, sendTo, msg.as_string())
        server_ssl.close()

        textOutput = textOutput + 'Email sent!\n'
    except Exception: # GMail reports if wrong access policy
        return ACCESS_ERROR
    return PASS

def onBtnSend(window):
    user = window.lineEditUser.text()
    password = window.lineEditPassword.text()
    sendTo = window.lineEditSendTo.text()
    filename = window.lineEditFolder.text()
    keyword = window.lineEditKeyword.text()

    textOutput = ""
    if (checkUser(user) and checkPassword(password) and checkSendTo(sendTo) and checkFilename(filename) and checkKeyword(keyword)):
        ret = processFile(user, password, sendTo, filename, keyword, textOutput)
        if (ret == WRONG_FILE):
            textOutput = "File doesn't content keyword!\n"
        if (ret == PASS):
            textOutput = "Email sent\n"
        if (ret == FILE_ERROR):
            textOutput = "Can't open file!\n"
        if (ret == ACCESS_ERROR):
            textOutput = "Can't access to email!\n"
    else:
        textOutput = "Invalid input fields data!\n"

    window.textOutput.setText(textOutput)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()