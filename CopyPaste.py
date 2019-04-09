import os
import zipfile

#Check root user
if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.\nExample : sudo python <filename>.py")

#Store all file name in array
Mylist = os.listdir('.')
#Get the number size of array
tfile = int(len(Mylist))
#Print all the data from array
print "List of files contain in current directory: \n"
x = 1
while x < tfile+1:
	print x,". ",Mylist[x-1]
	x+=1
#Reveice input xml and attach from user
xml = int(input("\nChoose XML backup file: "))
attach = int(input("Choose Attachments backup file: "))
print Mylist[xml-1]
print Mylist[attach-1]
#Copy & paste file to others location
cdir = os.getcwd()
cpxml = 'cp {}/{} var/'.format(cdir,Mylist[xml-1])
cpattach = 'cp {}/{} var/'.format(cdir,Mylist[attach-1])
os.system(cpxml)
os.system(cpattach)
#Unzip Attachments backup file
loczip = '/home/user/Desktop/var/{}'.format(Mylist[attach-1])
unpack_attach = zipfile.ZipFile(loczip)
unpack_attach.extractall('/home/user/Desktop/var')
unpack_attach.close()
#Change ownership of file from ROOT to user
own = 'chown -R user:user var/'
os.system(own)
