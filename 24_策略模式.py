class customer:
    customer_name=""
    snd_way=""
    info=""
    phone=""
    email=""
    def setPhone(self,phone):
        self.phone=phone
    def setEmail(self,mail):
        self.email=mail
    def getPhone(self):
        return self.phone
    def getEmail(self):
        return self.email
    def setInfo(self,info):
        self.info=info
    def setName(self,name):
        self.customer_name=name
    def setBrdWay(self,snd_way):
        self.snd_way=snd_way
    def sndMsg(self):
        self.snd_way.send(self.info)

#snd_way向客户发送信息的方式，该方式置为可设，即可根据业务来进行策略的选择。
#发送方式构建如下：
class msgSender:
    dst_code=""
    def setCode(self,code):
        self.dst_code=code
    def send(self,info):
        pass

class emailSender(msgSender):
    def send(self,info):
        print("EMAIL_ADDRESS:%s EMAIL:%s"%(self.dst_code,info))

class textSender(msgSender):
    def send(self,info):
        print("TEXT_CODE:%s EMAIL:%s"%(self.dst_code,info))

#业务场景中将发送方式作为策略
if  __name__=="__main__":
    customer_x=customer()
    customer_x.setName("CUSTOMER_X")
    customer_x.setPhone("10023456789")
    customer_x.setEmail("customer_x@xmail.com")
    customer_x.setInfo("Welcome to our new party!")
    text_sender=textSender()
    text_sender.setCode(customer_x.getPhone())
    customer_x.setBrdWay(text_sender)
    customer_x.sndMsg()
    mail_sender=emailSender()
    mail_sender.setCode(customer_x.getEmail())
    customer_x.setBrdWay(mail_sender)
    customer_x.sndMsg()