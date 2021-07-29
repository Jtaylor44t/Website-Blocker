import time
from datetime import datetime as dt    #sets datetime as dt so you can just type dt

hosts_temp=r"C:\Users\Jtaylor\Desktop\Blank\Python\App3WebsiteBlocker\hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"    #get this from the hosts file. hosts file can only be changed by the administrator
website_list=["www.facebook.com", "facebook.com", "www.gmail.com", "https://mail.google.com/mail/u/0/#inbox"] #add a loop that iterates through list

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
##imports multiple datetime objects and compares them ^^^
        print("Working hours...")
        with open(hosts_path,'r+') as file:    #import the file and read it. then put the file.read() in a variable
            content = file.read()
            for website in website_list:
                if website in content:
                    pass  #pass is if you don't want to do anything. it will pass to next line since its in working hours
                else:
                    file.write(redirect+" "+ website+"\n") #this appends the websites to the hosts file.
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()  #produces a list with all lines in hosts file. turns content into a list
            file.seek(0) #place the pointer just before first character of file content. Gets all the lines and puts it at top
            for line in content:      #loop through content list and check these lines against content
                if not any(website in line for website in website_list): #checks items of website list against hosts file until list ends
                    file.write(line)  #append the line and remove the websites during "fun hours"
            file.truncate()

#need to delete the website lines if they are there. need to use append method to add and remove depending on time of day        
        print("Fun hours")
    time.sleep(300)

#this program will append the website lines under the original content of the hosts file.
#first iteration adds first block after existing block of original content
#the truncate() method deletes the content of the file from the current point and downwards. need to move pointer to top.
#the seek method moves the original content to the top and then the truncate method will delete everything after the
#original content so the file is back to normal

#change file extension to pyw to run in background. then double click file to run it. must execute as admin
# change variables to hosts_temp without admin rights to test.

#use Task Scheduler to run script when computer starts.
#     scheduling:    Create Task>Name it>configure for(OS)>check run with highest priveleges box>triggers>new>
# begin the task>at startup> actions>start a program> point to program script>click ok>conditions>uncheck AC power only








