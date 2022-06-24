import os

#get the relevant email set from the file 'emailset.txt'
emailset=[]
fileobj=open("emailset.txt")
emailset=fileobj.read().split(',')
#print(lines)
for i in range(0,len(emailset)):
    emailset[i]=(emailset[i].replace("'","")).strip()

#specify the range say if you are downloading files from 50,000.eml to 50,000.eml
for i in range(30000,50000):
    #below if loop checks if this file is a file from the emailset document
    if ("{0}.eml".format(i)) in emailset:
        os.system("curl -O https://file.wikileaks.org/file/podesta-emails/Maildir/cur/%s.eml"%i)
