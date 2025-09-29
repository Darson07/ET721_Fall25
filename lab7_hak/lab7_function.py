'''
Darson Hak
Function File
09/29/2025
Lab #7: 
'''
def testing():
    print("Darson Hak")

# EXAMPLE #1: Read File
def read_data(filename):
    # pipe a text line in a file with a Python code
    fileuser = open(filename, 'r')

    # use a loop to go over each line in fileuser
    for each in fileuser:
        print(each)