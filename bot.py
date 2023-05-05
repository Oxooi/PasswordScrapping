#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Import the required modules
import os
import sys
from tqdm import tqdm

# Define a class to scrape password from combolist
class ScrapPasswords:

    # Initialize the class
    def __init__(self, combolist, result):
        self.combolist = combolist
        self.result = result

    # Get the combolist file content
    def get_content(self):
        with open(self.combolist, "r") as file:
            content = file.readlines()
        return content
 
    # Write the password to the result file
    def write_password(self):
        content = self.get_content()
        for lines in tqdm(content, desc="Processing passwords"):
            passwd = lines.split(":")[1]
            passwd = passwd.replace("\n", "")
            
            # Write the password to the result file
            with open(self.result, "a") as file:
                file.write(passwd + "\n")    
        print("[+] File saved as: " + self.result + "\n")

# Define the main function
def main():

    # Check if the arguments are passed
    if len(sys.argv) < 2:
        print("Usage: python3 bot.py combolist.txt")
        sys.exit()


    # Define the combolist and result file
    combolist = sys.argv[1]
    result = "results/final.txt"
    
    # Check if the combolist file exists
    if not os.path.exists(combolist):
        print("[-] The combolist file does not exist!")
        sys.exit()

    # Define the scraper object
    scraper = ScrapPasswords(combolist, result)

    # Get the content and write the password
    scraper.get_content()
    scraper.write_password()

# Execute the main function
if __name__ == "__main__":
    main()