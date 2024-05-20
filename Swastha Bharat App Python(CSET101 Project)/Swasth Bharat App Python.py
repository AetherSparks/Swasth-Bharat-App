
import csv

import sys



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
                                    
                                    viewdiseasenormal()
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

        thankyou()


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
    f=open('signuprequest.csv', 'r')
    csv_reader= csv.reader(f)
    for line in csv_reader:
        if line:
            
        
            print("\nSomeone with the username '"+ line[0]+ "' wants viewing access to the Swastha Bharat App Database.")

            signuprequestacceptdeny=input("Will you Accept or Deny this Request?\n")
            if signuprequestacceptdeny=='Accept':
                with open('databaseaccess.csv', 'a', newline='') as accessdatabase:
                    csv_writer= csv.writer(accessdatabase)
                    csv_writer.writerow(line)

                    
                        

                print("Viewing Access Request has been Accepted. ")    
         

            else:

                print("Viewing Access Request has been Denied.")
        else:
            print("No Signup Requests have been raised.")
    f.close()            
    f=open('signuprequest.csv', 'w')
    f.close()
    admincontrols()




def viewdisease():
        
    patientname=input("Enter the Patient Aadhaar ID who's record you would like to View: \n")
    
    with open('patientdiseaselist.csv', 'r') as patientdiseaselists:
        csv_reader= csv.reader(patientdiseaselists)
        for line in csv_reader:
            if int(float(line[0]))==int(patientname):
                print("Here is the record:\n")
                print('Name:', line[1],'\n')
                print('Aadhaar Number:', line[0],'\n')
                for i in line:
                    if i!=line[0] and i!=line[1]:
                    
                        print(i,'\n')
                        thankyou()
                else:
                    continue

                print('Wrong Data Entered.\n')
                thankyou()

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
                thankyou()

        elif askmore=='Yes':
            continue







    
def viewdiseasenormal():
         
    with open('patientdiseaselist.csv', 'r') as patientdiseaselists:
        csv_reader= csv.reader(patientdiseaselists)
        for line in csv_reader:
            if line[0]==normalaadhaar:
                print("Here is your record based on the Aadhaar ID you have uploaded during Signup:\n")
                print('Name:', line[1],'\n')
                print('Aadhaar Number:', line[0],'\n')
                for i in line:
                    if i!=line[0] and i!=line[1]:
                    
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
Nov 14 2023

Creator= Abhiraj Ghose
"""
