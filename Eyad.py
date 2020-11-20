print ("make by EYAD")

aminoid = input ("Enter the amino id: ")

userid = input ("Enter id of host: ")

chatid = input ("Enter id of chat: ")

email = input ("Enter your account Email: ")

password = input ("Enter your account Password: ")

import amino

client = amino.Client()

client.login(email=email, password=password)

subclient = amino.SubClient(comId=aminoid, profile=client.profile)

subclient.kick(userId=userid, chatId=chatid, allowRejoin=True) #
