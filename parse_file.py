import json
import os

#def get_json_content(file):
   
def get_json_content(files):
    list = []
    zip = []
    usersEmail = []
    userPay = []
    for file in files:
        print(file, "\n")
        with open(file[0], "r") as f:
            text = f.read()
            userInfo = json.loads(text)
            for user in userInfo:
                validate_phone_number(user["Phone Number"], list)
                validate_zip_code(user["Zip Code"], zip)
                generate_email(user["First Name"], user["Last Name"], usersEmail)
                generate_salary(user["Job ID"], user["State"], user["First Name"])
    print(list)
    print("Valid Zip codes: ", zip)
    print("Generated Emails: ", usersEmail)

#def validate_phone_number(phone_number):

def validate_phone_number(phone_number, list):
    
    phone_number = phone_number.strip()
    if len(phone_number) == 10 and phone_number.isdigit():
        list.append(phone_number)
    # return list

#def validate_zip(zip_code):

def validate_zip_code(zip_code, zip):
    zip_code = zip_code.strip()
    if len(zip_code) == 5:
        zip.append(zip_code)

#def generate_email(first_name, last_name):
    
def generate_email(first_name, lastname, usersEmail):
    first_name.strip()
    lastname.strip()
    if first_name and lastname:
        usersEmail.append(f"{first_name}{lastname}@comp.com")


#def generate_salary(job_id, state):
    
def generate_salary(job_id, state, name):
    states = ["NY", "CA",  "OR", "WA", "VT"]
    if job_id.startswith("SA"):
        baseSalary = 60000
        if state in states:
            if state in states:
                stateExtra = baseSalary * 0.015
                baseSalary = 60000 + stateExtra
        if job_id.endswith("_MNG"):
            extra = baseSalary * 0.05
            baseSalary = baseSalary + extra
        print(f"{name}: ${baseSalary}")
    elif job_id.startswith("HR"):
        baseSalary = 70000
        if state in states:
            stateExtra = baseSalary * 0.015
            baseSalary = 7000 + stateExtra
        print(f"{name}: ${baseSalary}")
    elif job_id.startswith("IT"):
        baseSalary = 80000
        if state in states:
            stateExtra = baseSalary * 0.015
            baseSalary = 60000 + stateExtra
        print(f"{name}: ${baseSalary}")
#def process_each_emp(emp_list):
    




#def generate_formatted_file(emp_list, orig_path):
    

