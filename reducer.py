#!/bin/python3

"""
About this Script

* Run at the command line with the following arguments (in order):
    ** Desired key
    ** Relative path to JSON file (or files - not hard limit)

Ian Richard Ferguson | Stanford University
"""

# ---------- Imports
import os
import json
import sys


# ---------- Setup

def checkCommandLine():
    """
    Confirms End User has entered valid arguments
    """

    ux = sys.argv

    # User didn't include key and JSON
    if len(ux) < 2:
        print("\nHeck! Invalid user input\n\nYour input:\t{}\n".format(ux))
        sys.exit(1)

    # Incorrect order of arguments (JSON files come last)
    for userEntry in ux[2:]:
        if ".json" not in userEntry:
            print("\nInvalid user entry - run python3 main.py [ KEY VALUE ] [ JSON FILE ]\n")
            sys.exit(1)


def parseUserInput():
    """
    Assumes command line input has already been checked

    Returns string object (desired key) and list object (list of JSONs, may only be one)
    """

    ux = sys.argv                                                       # List of command line args
    keyName = ux[1]                                                     # Key val must come before JSON files
    JSON_files = ux[2:]                                                 # May be 1 or more JSON files

    return keyName, JSON_files


def directoryTree(KEY):
    """
    Standardized output flow for reduced JSON files
    Makes output directory AND returns string value of relative path
    """

    path = ("./OUTPUT/{}/".format(KEY))                                 # Relative output path

    # If Output parent dir doesn't exist at all..
    if not os.path.isdir("./OUTPUT/"):
        os.mkdir("./OUTPUT/")

    # Make subdir within Output dir
    if not os.path.isdir(path):
        os.mkdir(path)

    return path


def outputName(KEYVALUE, JSON):
    """
    Returns name of output JSON file
    """

    temp = str(JSON)[:-5]                                               # Isolate filename without extension
    temp = temp.split('/')[-1]                                          # Strip leading directory path
    temp += "_{}-only.json".format(KEYVALUE)                            # Append to filename

    return temp


def isoUSER(KEYVALUE, JSON, PATH):
    """
    Reduces JSON file down to desired key tree
    """

    newName = outputName(KEYVALUE, JSON)                                # Generate output filename

    with open(JSON) as incoming:
        temp = json.load(incoming)                                      # Read JSON as dictionary
        temp = temp[KEYVALUE]                                           # Reduce JSON to desired key

    with open(os.path.join(PATH, newName), "w") as outgoing:
        json.dump(temp, outgoing, indent=4)                             # Write JSON to Output dir


def main():
    """
    Let's get it
    """

    checkCommandLine()                                                  # Confirm arguments supplied
    user_value, json_list = parseUserInput()                            # Isolate arguments
    path = directoryTree(user_value)                                    # Save output path to memory
    
    # In case multiple JSONs are provided...
    for k in json_list:
        print("Subsetting {}....".format(k))
        isoUSER(user_value, k, path)

    print("All JSON values parsed - see {} for output".format(path))


if __name__ == "__main__":
    main()