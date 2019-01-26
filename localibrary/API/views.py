
from django.http import HttpResponse

import smtplib
from django.shortcuts import render


def hook_get(request):
    if request.method == "GET":
     from_mail = request.GET.get('token')
     text = request.GET.get("text")
     foo = sendmail(text=text,from_mail=from_mail)
     foo.sendfrom()
     return HttpResponse('ok')
    else:
        return HttpResponse('api no')



class sendmail:
   def __init__(self,text,from_mail):
       try:
           self.mail = smtplib.SMTP('smtp.gmail.com', 587)
       except:
           pass
       self.send_mail ="mail name"
       self.password = "password mail"
       self.from_mail = from_mail
       self.text = text
   def sendfrom(self):
        self.mail.ehlo()
        self.mail.starttls()
        self.mail.login(self.send_mail,self.password )
        self.mail.sendmail(self.send_mail, self.from_mail, self.text)
        self.mail.quit()

def post_fon(request):
    return render(request,'api/index.html',{})

