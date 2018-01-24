from string import index
def xor(a,b):
    if a==b:    return '0'
    else:    return '1'
def crc(msg,poly):
    # i is the eval value,where position is the current position of that value
    i=eval(msg[0])
    position=0
    last=11

        #This code will check if the current bit position is 0 or 1 and executes the code if its 1
    while i and position+3<last:
        for x in xrange(4):
                #xor will return a string value
            msg[position]=xor(msg[position],poly[x])
            position+=1
        for x in msg:
            if eval(x):
                i=eval(x)
                position=msg.index(x)
                break

    temp=msg[8:]
    return temp

msg=list(raw_input("Enter the msg you want to send:"))
poly=list('1011')
msg=msg+list('000')
code=crc(msg,poly)
print "the crc code is ",code
new_msg=list(raw_input("enter the reciever side msg:"))
newcode=crc(new_msg,poly)
print "newcode:",newcode
if list('000')== newcode:
    print "The message was not corrupted"
else: print "The message is corrupted"
