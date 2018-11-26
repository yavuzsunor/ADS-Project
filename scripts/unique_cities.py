import csv



with open('MPVDatasetDownload.xlsx', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')