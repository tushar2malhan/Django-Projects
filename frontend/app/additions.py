# create records data using csv file storeed in articles.csv
import csv
import os

from models import Articles
from time import strptime   

# with open(r'app\articles.csv',encoding="utf8") as f:
#     reader = csv.reader(f)
    # next(reader)            # Column names
    # for row in reader:

        # print(row[1]) # title
        # print(row[2]) # body
        # print(row[3]) # affiliations
        # print(row[4]) # authors
        # print(row[5]) # journal

        # print(row[6].split(' ')[0], strptime(row[6].split(' ')[1],'%b').tm_mon if len(row[6].split(' ')[1]) == 3 else strptime(row[6].split(' ')[1].split('-')[0],'%b' ).tm_mon) 
        # print(row[7] ) # keywords == category
        # print(row[7].split('/')[0].split(',')[:2]  ) #  category
        # print(row[8]) # url
        # print('******************************\n\n')

        # Articles.objects.create(
            # title = row[1],
            # body = row[2],
            # affiliations = row[3],
            # authors = row[4],
            # journal = row[5],
            # created_at = (row[6].split(' ')[0],
            # strptime(row[6].split(' ')[1],'%b').
            # tm_mon if len(row[6].split(' ')[1]) == 3 
            # else strptime(row[6].split(' ')[1].split('-')[0],'%b' ).tm_mon,
            # row[6].split(' ')[2] if row[6].split(' ')[2] else 1
            # ),
            # updated_at = created_at,
            # keywords = row[7],
            # url = row[8],
            # category = ' '.join(row[7].split('/')[0].split(',')[:2]),
            # )
            
    # print('Done')