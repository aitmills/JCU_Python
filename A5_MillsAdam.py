# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:50:31 2020

@author: amills
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def disply_main_menu():
    print("""Welcome to The Basic Statistician!
      Please choose from the following options:

     1 – Load from a CSV file

     2 – Analyse

     3 – Visualise

     4 - Quit""")
    menu_choice = validate_maininput("Please enter an item number from the menu: ")
    return menu_choice

# Validate main menu choice
def validate_maininput(message):
    valid_input = False
    menu_choice = 0
    while valid_input == False:       
        try:
            menu_choice = int(input(message))
            if 1 <= menu_choice < 5:
                valid_input = True
                return menu_choice
            else:
                valid_input = False
        except ValueError:
            print("----------")
            print("ERROR: Not an acceptable number")
            print("----------")
    return menu_choice

def load_file(): 
    print("List of CSV files: \n")
    for f_name in os.listdir():
        if f_name.endswith('.csv'):
            print(f_name)
    try:
        filename = input("Enter a filename: ")
        all_data = pd.read_csv(filename, index_col = 0)
        print("----------")
        print("Set data loaded successfully")
        print("----------")
        print(all_data)
        return all_data
    except Exception:
        print("----------")
        print("ERROR: Not an acceptable filename")
        print("----------")
        load_file()
    
def check_loaded(all_data):
    if len(all_data) == 0:
        data_loaded = False
        print("----------")
        print("ERROR: No data loaded yet, use main menu option 1 to load data")
        print("----------")
    else:
        data_loaded = True
    return data_loaded

def analyse_sets(all_data):
    for col in all_data:
        print("----------")
        print("         Variable Name:", str.upper(col))
        print("  Number of values (n):", all_data[col].count())
        print("                  Mean:", round(all_data[col].mean(),2))
        print("    Standard Deviation:", round(all_data[col].std(),2))
        print("Standard Error of Mean:", round(stats.sem(all_data[col]),2))

def get_plot_choice():
    valid_choice = False
    while valid_choice == False:
        try:
            plot_choice = int(input("Please select a plot type: "))
            if 1 <= plot_choice < 4:
                valid_choice = True
                return plot_choice
            else:
                valid_choice = False

        except ValueError:
            print("----------")
            print("ERROR: Not an acceptable number")
            print("----------")

def get_subplot_choice():
    valid_choice = False
    while valid_choice == False:
        try:
            sub_plots = str.lower((input("Display as subplots? Yes(y) or No(n): ")))
            
            if sub_plots == "y" or sub_plots == "yes":
                valid_choice = True
                sub_plots = True
                return sub_plots
            elif sub_plots == "n" or sub_plots == "no":
                sub_plots = False
                valid_choice = True
                return sub_plots
            else:
                valid_choice = False
        except ValueError:
            print("----------")
            print("ERROR: Not an acceptable number")
            print("----------")

    return sub_plots

def main():
    all_data = []
    menu_choice = disply_main_menu()
    while menu_choice > 0 and menu_choice < 4:
        
         # Load from csv file
        if menu_choice == 1:
            print("Option 2 - load from CSV file \n")
            all_data = load_file()
            menu_choice = disply_main_menu()
            
         # Analyse
        elif menu_choice == 2:
            if check_loaded(all_data) == True:
                print("Option 2 - analyse \n")
                analyse_sets(all_data)
                menu_choice = disply_main_menu()
            else:
                menu_choice = disply_main_menu()

        # Visualise / display stats
        elif menu_choice == 3:
            if check_loaded(all_data) == True:
                print("Option 3 – visualise \n")
                print("""Please select a plot type: 
        1 - Line 
        2 - Bar
        3 - Box
        """)
                plot_choice = get_plot_choice()
                sub_plots = get_subplot_choice()
                
                if plot_choice == 1 and sub_plots == True:
                    all_data.plot.line(subplots=True, figsize=(10, 10))
                    plt.show()
                elif plot_choice == 1 and sub_plots == False:
                    all_data.plot(figsize=(10, 5))
                    plt.show()
                elif plot_choice == 2 and sub_plots == True:
                    all_data.hist(bins=50, figsize=(10, 5))
                    plt.show()
                elif plot_choice == 2 and sub_plots == False:
                    all_data.plot.hist(stacked=True, bins=50, alpha=0.5)
                    plt.show()
                elif plot_choice == 3 and sub_plots == True:
                    all_data.plot.box(subplots=True, figsize=(10, 5))
                    plt.show()
                elif plot_choice == 3 and sub_plots == False:
                    all_data.plot.box(figsize=(10, 5))
                    plt.show()

            menu_choice = disply_main_menu()
            
        else:
            menu_choice = disply_main_menu()
            print("----------")
main()