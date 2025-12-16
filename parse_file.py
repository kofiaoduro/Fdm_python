import json
import os

#def get_json_content(file):
   
def get_json_content(files):
    list = []
    for file in files:
        print(file, "\n")
        with open(file[0], "r") as f:
            text = f.read()
            userInfo = json.loads(text)
            for user in userInfo:
                (validate_phone_number(user["Phone Number"], list))
    print(list)

#def validate_phone_number(phone_number):

def validate_phone_number(phone_number, list):
    
    phone_number = phone_number.strip()
    if len(phone_number) == 10 and phone_number.isdigit():
        list.append(phone_number)
    # return list

#def validate_zip(zip_code):




#def generate_email(first_name, last_name):
    



#def generate_salary(job_id, state):
    



#def process_each_emp(emp_list):
    




#def generate_formatted_file(emp_list, orig_path):
    

