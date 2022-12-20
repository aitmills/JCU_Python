# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:58:27 2020
for JCU 20-A-CP5805-ONL-EXT-SP81 Programming and Data Analytics using Python
Assessment task 4: Data analysis - implement 

@author: amills
"""

def load_file():
    from csv import reader
    opened_file = open('a4_data.csv')
    read_file = reader(opened_file)
    all_data = list(read_file)
    print("----------")
    print("Set data loaded successfully")
    print("----------")
    
    return all_data

def display_sets(all_data):
    print("----------")
    print("DATA CURRENTLY LOADED: \n")
    # Convert list number elements from str to int before displaying/sorting
    j = 0
    for array in all_data:
        i = 0
        for element in all_data[j]:
            if str(all_data[j][i]).isdigit() == True:
                all_data[j][i] = int(all_data[j][i])   
            i+= 1
        j+= 1
    i = 0
    for set in all_data:
        print(all_data[i][0])
        print("")
        
        print("SET VALUES:")
        print(all_data[i][1:])
        print("")
        i = i + 1
    print("----------")
    return all_data

def rename_set(set_choice, set_choice_name, all_data):
    print(set_choice)
    print(set_choice_name)
    old_set_name = all_data[set_choice][0]
    all_data[set_choice][0] = set_choice_name
    print("----------")
    print("OLD NAME: ",old_set_name,"CHANGED TO NEW NAME: ",all_data[set_choice][0])
    print("----------")
    return

def sort_set(set_choice, all_data):
    print("----------")    
    print("BEFORE:")
    print(all_data[set_choice][1:])
     # Convert list number elements from str to int before sorting/displaying
    j = 0
    for array in all_data:
        i = 0
        for element in all_data[j]:
            if str(all_data[j][i]).isdigit() == True:
                all_data[j][i] = int(all_data[j][i])   
            i+= 1
        j+= 1
    print("AFTER:")
    all_data[set_choice][1:] = sorted(all_data[set_choice][1:])
    print(all_data[set_choice][1:])
    print("----------")    
    return all_data

def displaystats_set(set_choice, all_data):
    from statistics import mode

    set_count = len(all_data[set_choice][1:])
    set_min = min(all_data[set_choice][1:])
    set_max = max(all_data[set_choice][1:])
    all_data[set_choice][1:].sort()
    try:
        
        if set_count % 2 == 0:
            median1 = int(all_data[set_choice][1:][set_count//2])
            median2 = int(all_data[set_choice][1:][set_count//2 - 1])
            median = (median1 + median2) / 2
        else: 
            median = all_data[set_choice][1:][set_count//2] 
        
        set_medi = median
        set_mode = mode(all_data[set_choice][1:])
    except:
        set_mode = "N/A"

    print("----------")
    print("            Set Name: ", all_data[set_choice][0])
    print("Number of Values (n): ", set_count)
    print("                 Min: ", set_min)
    print("                 Max: ", set_max)
    print("              Median: ", set_medi)
    print("                Mode: ", set_mode)
    print("----------")
    return

def disply_main_menu():
    print('''
    1 – Load data from a file
    2 – Display the data to the screen
    3 – Rename a set
    4 – Sort a set
    5 – Analyse a set
    6 - Quit
    ''')
    menu_choice = validate_maininput("Please enter an item number from the menu: ")
    return menu_choice

# Validate main menu choice
def validate_maininput(message):
    valid_input = False
    menu_choice = 0
    while valid_input == False:       
        try:
            menu_choice = int(input(message))
            if 1 <= menu_choice < 7:
                valid_input = True
                return menu_choice
            else:
                valid_input = False
        except ValueError:
            print("----------")
            print("ERROR: Not an acceptable number")
            print("----------")
    return menu_choice

def validate_setchoice(all_data):
    valid_input = False
    while valid_input == False:
        try:
            set_choice = int(input("Please enter an SET NUMBER from the menu list: "))
            if 0 <= set_choice < len(all_data):
                valid_input = True
                return set_choice
            else:
                valid_input = False
        except ValueError:
            print("----------")
            print("ERROR: Not an acceptable number")
            print("----------")
    return set_choice

def check_loaded(all_data):
    if len(all_data) == 0:
        data_loaded = False
        print("----------")
        print("ERROR: No data loaded yet, use main menu option 1 to load data")
        print("----------")
    else:
        data_loaded = True
    return data_loaded

def list_set_names(all_data):
    i = 0
    print("----------")
    print("SET NAME:")
    for set in all_data:
        print(i, "-" ,all_data[i][0])
        print("")
        i = i + 1
    return

def main():
    all_data = []
    print('''
Welcome to The Smart Statistician!
NOTES:
- Data is expected in csv format with each set on its own row and set name first followed by numerical values.
- File name should be a4_data.csv

Please choose from the following options:''')
    menu_choice = disply_main_menu()
    while menu_choice > 0 and menu_choice < 6:
        
         # Load from csv file
        if menu_choice == 1:
            all_data = load_file()
            menu_choice = disply_main_menu()
            
         # Display all
        elif menu_choice == 2:
            if check_loaded(all_data) == True:
                display_sets(all_data)
                menu_choice = disply_main_menu()
            else:
                menu_choice = disply_main_menu()

         # Rename
        elif menu_choice == 3:
            if check_loaded(all_data) == True:
                list_set_names(all_data)
                set_choice = validate_setchoice(all_data)
                set_choice_name = input('{} for the {} set = '.format("Please enter a new name", all_data[set_choice][0]))
                rename_set(set_choice, set_choice_name, all_data)
                menu_choice = disply_main_menu()
                print("----------")
            else:
                menu_choice = disply_main_menu()

        # Sort
        elif menu_choice == 4:
            if check_loaded(all_data) == True:
                list_set_names(all_data)
                set_choice = validate_setchoice(all_data)
                sort_set(set_choice, all_data)
                menu_choice = disply_main_menu()
            else:
                menu_choice = disply_main_menu()

        # Analyse / display stats
        elif menu_choice == 5:
            if check_loaded(all_data) == True:
                list_set_names(all_data)
                set_choice = validate_setchoice(all_data)
                displaystats_set(set_choice, all_data)
                menu_choice = disply_main_menu()
            else:
                menu_choice = disply_main_menu()
                print("----------")
main()
