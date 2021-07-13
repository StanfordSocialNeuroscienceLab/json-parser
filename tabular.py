#!/bin/python3

"""
About this Script

* Point this script to a reduced JSON file (after reducer.py has been run)
* Loops through keys and sub-keys and produces CSVs for each nested dictionary

Ian Richard Ferguson | Stanford University
"""

# ---------- Imports
import json
import sys
from tqdm import tqdm
import pandas as pd


# ---------- Setup
def checkCommandLine():
    """
    Confirms that JSON was included as standard input
    """

    try:
        ux = sys.argv[1]                                                # Isolate command line argument
    except:
        print("\nAck! No user input provided")                          # Error + Exit
        sys.exit(1)

    if ".json" not in ux:
        print("\nInvalid JSON provided...\nYour input:\t\t{}".format(ux))
        sys.exit(1)


def isoSubjID():
    """
    Isolates Subject ID to use for output name / relative file paths
    """

    ux = sys.argv[1]                                                    # Isolate command line argument
    ux = ux.split('/')[2]                                               # Remove leading and trailing dirs 
    return ux


def parseJSON(INCOMING):
    """
    
    """

    subjID = isoSubjID()                                                # Isolate subject ID
    outer_keys = list(INCOMING.keys())                                  # Install IDs to loop through

    for nest in tqdm(outer_keys):
        temp = INCOMING[nest]                                           # Values / install ID

        for key in list(temp.keys()):
            output_name = "{}-{}-{}.csv".format(subjID, nest, key)      # Formatted output name for CSV
            iso = temp[key]                                             # Unnest JSON key
            frame = pd.DataFrame(iso)                                   # Save as DataFrame locally
            frame.to_csv("./OUTPUT/{}/{}".format(subjID, output_name), index=False)



def main():
    checkCommandLine()

    with open(sys.argv[1]) as incoming:
        data = json.load(incoming)
        parseJSON(data)

    print("All CSVs saved locally\n")


if __name__ == "__main__":
    main()