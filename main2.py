import usr_input
import parse_file
import os

#def error_handle(check_return):
'''
key Notes: 
1)Need to check if the given file path exists, and if not display the message 
"<file path> does not exist." and return an int of 1.
2)If the given file path exists and is a folder, check_path needs to 
check the content of the folder for any valid files. This should work even if there are nested folders.
3)If the given file path exists and is a file but is already formatted JSON file, 
it needs to be skipped and an int of 2 returned. The names of already 
formatted JSON files end with '_formatted.json'.
'''


def main():
    
    
    
    
    
    
    
    def check_path(file_path, list=[]):
        print(os.getcwd())
        current_directory = os.getcwd()
        fiesToBeProcessed = []
        #Check to make sure the file path exits
        if os.path.exists(file_path):
            print("File exits")
            list = os.listdir(file_path)
            print(list)
        # now we need to check if the files are directories or valid to be processed
            for file in list:
                if os.path.isdir(file):
                    print("Here are the folders", file)
                    #if its a folder we want to loop over it and list all the files that can be proccesed
                    print(os.listdir(file))
                    folderFiles = os.listdir(file)
                    for file in folderFiles:
                        if file.endswith(".json") and not file.endswith("_formatted.json"):
                             # print(f"File that ends with .json {file}")
                               fiesToBeProcessed.append(f"({current_directory}/{file}, {file})")
                else:
                    if os.path.isfile(file):
                      #  print(f"Here are the files {file}")
                        if file.endswith(".json") and not file.endswith("_formatted.json"):
                        #    print(f"File that ends with .json {file}")
                            fiesToBeProcessed.append(f"({current_directory}/{file}, {file})")
        #if the path does not exit return path does not exit
        else:
            print("File path does not exits")
            return 1
        
        print(fiesToBeProcessed)
    check_path(".")

if __name__ == "__main__":
    main()