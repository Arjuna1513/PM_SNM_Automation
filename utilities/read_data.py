import csv

def readCSVData(fileName):
    rows = [] #created rows list to store rows of data.
    with open(fileName, 'r') as fileData: # opened a file to read data from
        reader = csv.reader(fileData) # create a reader using the file
        next(reader) #reader by-default will point to first row but we need to start from 2nd row.
        for row in reader:
            rows.append(row)
    return rows