import tkinter as tk

import csv

import sys

from PIL import ImageTk, Image



#Checking Login Details:
def logincheck():
    global normaluser
    normaluser=userbut.get()
    global normalpass
    normalpass=passbut.get()
    
    
    if normaluser=='AbhirajGhose' and normalpass=='8851679131':
        adminwindow=tk.Tk()
        adminwindow.geometry("1920x1080")
        adminwindow.title("Swasth Bharat App by Abhiraj Ghose")
        Applogolabel=tk.Label(adminwindow, text='Welcome Admin', font=('Arial', 30))
        Applogolabel.pack(pady=20)


#Login Screen
def loginbutpress():
    loginwindow=tk.Tk()
    loginwindow.geometry("1920x1080")
    loginwindow.title("Swasth Bharat App by Abhiraj Ghose")
    label=tk.Label(loginwindow, text='Please Enter your Username and Password', font=('Arial', 30))
    label.pack(pady=20)
    root.destroy()
    userlabel=tk.Label(loginwindow, text='Username', font=('Arial', 20))
    userlabel.pack()
    userbut=tk.Entry(loginwindow, font=('Arial', 20))
    userbut.pack()
    passlabel=tk.Label(loginwindow, text='Password', font=('Arial', 20))
    passlabel.pack()
    passbut=tk.Entry(loginwindow, font=('Arial', 20))
    passbut.pack()
    Loginbut=tk.Button(loginwindow, text="Log In", font=('Arial', 20),padx=50, pady=10, command=logincheck)
    Loginbut.pack()

    


#Choosing Login or Signup Main Screen

root=tk.Tk()
root.geometry("1920x1080")

Applogo=ImageTk.PhotoImage(Image.open("Swasth Bharat App Logo.png"))
Applogolabel=tk.Label(image=Applogo)
Applogolabel.pack()
root.title("Swasth Bharat App by Abhiraj Ghose")
label=tk.Label(root, text='Welcome to Swasth Bharat App by Abhiraj Ghose!\nWould You like to Log in or Sign Up?', font=('Arial', 30))
label.pack(pady=20)
Loginbut=tk.Button(root, text="Log In", font=('Arial', 15),padx=50, pady=25,command=loginbutpress)

Signupbut=tk.Button(root, text="Sign Up",font=('Arial', 15),padx=40, pady=25)


Loginbut.pack()
Signupbut.pack()

root.mainloop()






'''

# THANKYOU
def thankyou():
    print("\n\nThankyou for using Swastha Bharat App-Py, Created by Abhiraj Ghose\n\n\n\n\n\n\n\n\n")
    sys.exit()

# CHOOSING LOGIN OR SIGNUP
def loginorsignup():
    print("\n\n\n\n")
   
    print("Welcome User! \n")

    print('Would you like to Log In, or Sign Up? ')
 
    loginsignup=int(input('Press 1 to Log In, Press 2 to Sign Up \n\n'))

    if loginsignup==1:
        normallogin()
    elif loginsignup==2:
        normalsignup()



# NORMAL LOGIN
def normallogin():
    normaluser=input("Enter Username: ")
  
    normalpass=input("Enter Password: ")
  
    if normaluser=='AbhirajGhose' and normalpass=='8851679131':
        print("\nWelcome Adminstrator!\n")
        admincontrols()
    elif 1==1:
        with open('databaseaccess.csv', 'r') as accessdatabase:
            csv_reader= csv.reader(accessdatabase)

            for lines in csv_reader:

                if lines[0]==normaluser and lines[1]==normalpass:
                    print("\nWelcome", normaluser)
                    print("\n What would you like to do?")
                    global normalaadhaar
                    normalaadhaar=lines[2]
                    loginput=int(input("Press 1 to check your record, Press 2 to sign out:  "))
                    if loginput==1:
                        with open('patientdiseaselist.csv', 'r') as patientdiseaselists:
                            csv_reader= csv.reader(patientdiseaselists)
                            for line in csv_reader:
                                if int(float(line[0]))==int(normalaadhaar):
                                    print("Here is the record:")
                                    for i in line:
                                        if type(i)==float():
                                            print(int(i))
                                        else:
                                            print(i,'\n')
                                    thankyou()
                                    break
                                else:
                                    continue
                                
                 
        print("Wrong Data Entered.")
        thankyou()
                        


      


# NORMAL SIGNUP
def normalsignup():
    normaluser=input("Enter Username: ")

    normalpass=input("Enter Password: ")
    
    aadhaarnumber=int(input("Enter Aadhaar ID: "))
    with open('signuprequest.csv', 'w') as signupfile:
        signuplist=[normaluser, normalpass, aadhaarnumber]
        csv_writer= csv.writer(signupfile)
        csv_writer.writerow(signuplist)

        print("\n\nYour Signup Request has been forwarded to the Adminstrator. Please wait while he/she approves it. Thankyou.")

        print("\n\n Thankyou for using Swastha Bharat App-Py, Created by Abhiraj Ghose")


# ADMIN CONTROLS
def admincontrols():

    print("Select an option: \n ")

    print("1. Check for pending SignUp requests")

    print("2. View Patient Records")

    print("3. Add Patient Records")
    
    print("4. Sign Out")
    adminoption=int(input("\n"))
    if adminoption==4:
        thankyou()
        
    elif adminoption==1:
        adminpendingsignup()   
    elif adminoption==2:
        
        viewdisease()
    
    elif adminoption==3:
        adddisease()
   
            



# NORMAL USER CONTROLS



# ACCEPTING OR DENYING PENDING SIGUP REQUESTS
def adminpendingsignup():
    with open('signuprequest.csv', 'r') as signupfile:
        csv_reader= csv.reader(signupfile)
        for line in csv_reader:
            
            print("\nSomeone with the username '"+ line[0]+ "' wants viewing access to the Swastha Bharat App Database.")

            signuprequestacceptdeny=input("Will you Accept or Deny this Request?\n")
            if signuprequestacceptdeny=='Accept':
                with open('databaseaccess.csv', 'a', newline='') as accessdatabase:
                    csv_writer= csv.writer(accessdatabase)
                    csv_writer.writerow(line)
                    with open('databaseaccess.csv', 'w') as accessdatabase:
                        print(" ")

                print("Viewing Access Request has been Accepted. ")    
                admincontrols()
                continue
            else:
                with open('databaseaccess.csv', 'w') as accessdatabase:
                    print(" ")

                print("Viewing Access Request has been Denied.")
                admincontrols()
                continue
 




def viewdisease():
        
    patientname=input("Enter the Patient Aadhaar ID who's record you would like to View: \n")
    
    with open('patientdiseaselist.csv', 'r') as patientdiseaselists:
        csv_reader= csv.reader(patientdiseaselists)
        for line in csv_reader:
            if int(float(line[0]))==int(patientname):
                print("Here is the record:")
                for i in line:
                    if type(i)==float():
                        print(int(i))
                    else:
                        print(i,'\n')
            else:
                continue

def adddisease():
    addmore=True
    
    patientname=input("Add the Patient's name: \n\n")
    aadhaar=int(input("Add the Patient's Aadhaar ID Number: \n\n"))
    diseaselist=[aadhaar, patientname]
    while addmore==True:
        diseasename=input("Add the Disease befallen or Vaccinations taken by the Patient and Date of Checkup:\n\n ")
        diseaselist.append(diseasename)
        askmore=input("Would you like to add more?\n")
        if askmore=='No':
            addmore=False
            with open('patientdiseaselist.csv', 'a', newline='') as patientdiseaselists:
                csv_writer= csv.writer(patientdiseaselists)
                csv_writer.writerow(diseaselist)
                print("Record has been added")

        elif askmore=='Yes':
            continue







    
def viewdiseasenormal():
         
    with open('patientdiseaselist.csv', 'r') as patientdiseaselists:
        csv_reader= csv.reader(patientdiseaselists)
        for line in csv_reader:
            if line[0]==normalaadhaar:
                print("Here is your record based on the Aadhaar ID you have uploaded during Signup:")
                for i in line:
                    print(i,'\n')
            else:
                continue

    







loginorsignup()










"""

Created on Tue Sep  5 19:27:11 2023
Days Worked:
Sep 5 2023
Sep 6 2023
Sep 7 2023
Sep 28 2023
Sep 29 2023
Nov 11 2023

Creator= Abhiraj Ghose
"""
'''