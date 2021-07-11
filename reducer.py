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

    if len(ux) < 2:
        print("\nHeck! Invalid user input\n\nYour input:\t{}\n".format(ux))
        sys.exit(1)

    for userEntry in ux[2:]:
        if ".json" not in userEntry:
            print("\nInvalid user entry - run python3 main.py [ KEY VALUE ] [ JSON FILE ]\n")
            sys.exit(1)


def parseUserInput():
    """
    Assumes command line input has already been checked

    Returns string object (desired key) and list object (list of JSONs, may only be one)
    """

    ux = sys.argv
    keyName = ux[1]
    JSON_files = ux[2:]

    return keyName, JSON_files


def directoryTree(KEY):
    """
    Standardized output flow for reduced JSON files
    Makes output directory AND returns string value of relative path
    """

    path = ("./OUTPUT/{}/".format(KEY))

    if not os.path.isdir("./OUTPUT/"):
        os.mkdir("./OUTPUT/")

    if not os.path.isdir(path):
        os.mkdir(path)

    return path


def checkForCopies(FULLPATH):
    """
    Prevents file overwriting over multiple runs
    """

    if os.path.isfile(FULLPATH):
        return True
    else:
        return False


def outputName(KEYVALUE, JSON):
    """
    Returns name of output JSON file
    """

    temp = str(JSON)[:-5]
    temp = temp.split('/')[-1]
    temp += "_{}-only.json".format(KEYVALUE)
    return temp


def isoUSER(KEYVALUE, JSON, PATH):
    """
    Reduces JSON file down to desired key tree
    """

    newName = outputName(KEYVALUE, JSON)

    with open(JSON) as incoming:
        temp = json.load(incoming)
        temp = temp[KEYVALUE]

    with open(os.path.join(PATH, newName), "w") as outgoing:
        json.dump(temp, outgoing, indent=4)


def main():
    """
    Let's get it
    """

    checkCommandLine()
    user_value, json_list = parseUserInput()
    path = directoryTree(user_value)
    
    for k in json_list:
        print("Subsetting {}....".format(k))
        isoUSER(user_value, k, path)

    print("All JSON values parsed - see {} for output".format(path))


if __name__ == "__main__":
    main()