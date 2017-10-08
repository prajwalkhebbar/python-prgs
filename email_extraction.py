import re
from operator import itemgetter
from audioop import reverse
f=open("mbox.txt")
email={}
#--------------for the most popular email_id------------------------
# for line in f:
#     matchobj=re.match(r"From (.*?) (.*) (.*)",line)
#     if matchobj:
#         id=matchobj.group(1)
#         if(id not in email ):
#             email[id]=1
#         else:
#             email[id]+=1 
# li=sorted(email.items(),key=lambda x:x[1],reverse=True)
# print"the most popular email is ",li[0][0],"which is repeated",li[0][1],"times"
# print"the 2nd most popular email is ",li[1][0],"which is repeated",li[1][1],"times"
#-------------------------for time of email----------------------------------
for line in f:
    matchobj=re.match(r"From (.*?) (.*)",line)
    if matchobj:
        id=matchobj.group(1)
        if(id not in email ):
             email[id]=matchobj.group(2)
for i in email:
    print"the email is",i,"and the time it is recieved is",email[i]