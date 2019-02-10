
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


def save_exel(request):
 if request.method == "GET":
   temp= request.GET.get("val")
   lux= request.GET.get("lux")
   df = pd.DataFrame({'LUX': [lux]},{"temp":[temp]})
   writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
   df.to_excel(writer, sheet_name='Sheet1')
   writer.save()
   logging.info("Informational message")
   return HttpResponse('complite')

def list_push(request):
    if request.method == "GET":
        temp = request.GET.get("val")
        lux = request.GET.get("lux")
        temp_list.append(temp)
        lux_list.append(lux)
        return HttpResponse('save')
def deleted_list(request):
    key = request.GET.get("key")
    if key == "ghostnetwork":
        temp_list,lux_list=[],[]
        return HttpResponse('deletade')

def push(request):
    mail = request.GET.get("mail")
    key = request.GET.get("key")
    if key == "String":
     send = sendmail(from_mail=mail,text=f"{temp_list} && {lux_list}")
     send.sendfrom()
     logging.error("error")
     return HttpResponse("push")
    else:
        return HttpResponse("500")
    
    def log(request):
    with open("log.log","r") as file:
        return HttpResponse(file.read())

