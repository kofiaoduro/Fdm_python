import os.path


def check_path(file_path, data_files):
    if not os.path.exists(file_path):
        print(file_path + " does not exist.")
        return "doesn't exist"
    elif os.path.isdir(file_path):
        for file in os.listdir(file_path):
            # The line below features calling the function within itself, which is refereed to
            # as 'recursion'. Recursion is needed here to meet the requirement : "to check the
            # contents of any nested folders".            
            check_path(os.path.join(file_path, file), data_files)
    elif file_path.endswith("_formatted.json"):
        data_files.append(file_path)
    return tuple(data_files)



#def get_usr_input(msg) :
    
