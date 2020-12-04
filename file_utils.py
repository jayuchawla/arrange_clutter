import os, time
import re

PATH = "E:\\temp\\"

FILES = os.listdir(PATH)

MONTHS = {"Dec":12, "Nov":11, "Oct":10, "Sep":9, "Aug":8, "Jul":7, "Jun":6, "May":5, "Apr":4, "Mar":3, "Feb":2, "Jan":1}

CONCERNED_PATTERN = re.compile(r'\d\d*-\d\d')

def get_concerned_folders():
    subdirs = [folder for folder in FILES if os.path.isdir(os.path.join(PATH + folder))]
    concerned_folders = []
    for s in subdirs:
        if CONCERNED_PATTERN.search(s):
            concerned_folders.append(s)

    return(concerned_folders)

def get_folder_name(filename):
    file_path = PATH + filename
    
    time_ = str(time.ctime(os.path.getctime(file_path))).split(" ")
    time_[1] = MONTHS[time_[1]]

    month_ = time_[1]

    if time_[2] == '':
        day_ = time_[3]
    else:
        day_ = time_[2]

    appropriate_folder_name = str(day_).lstrip("0") + "-" + str(month_)
    return appropriate_folder_name

if __name__ == "__main__":
    concerned_folders = get_concerned_folders()

    for file_name in FILES:

        # skip appropriate folders
        if file_name in concerned_folders:
            continue

        # get name of folder where to move this file        
        appropriate_folder_name = get_folder_name(file_name)

        # if appropriate folder not present make one
        if not appropriate_folder_name in concerned_folders:
            os.mkdir(os.path.join(PATH, appropriate_folder_name))
            concerned_folders.append(appropriate_folder_name)

        # move file to appropriate directory
        try:
            os.replace(os.path.join(PATH, file_name), os.path.join(PATH + appropriate_folder_name, file_name))
        except:
            print("File already open somewhere")