def find_number(s):
    l = ''
    for t in s.split():
        try:
            l = float(t)
        except ValueError:
            pass
    return l
#Import modules
import csv

#Arrays needing to be pre-defined
temp = []
htemp = []
raop_data = []
header = False

#Open up the train csv
temp2 = open('train.csv','rb')
train = csv.reader(temp2)

for row in train:
    #Make a header
    if header == False:
        if 'subreddits' in row[1] or 'requests' in row[1]:
            continue
        elif 'request_' in row[1] or\
        '_request' in row[1] or\
        'requester' in row[1]: 
            t = row[1].split()
            htemp.append((t[0].replace(':', '')))
        elif 'edited' in row[1]: 
            t = row[1].replace(':', '')       
            t = t.split()
            htemp.append(t[0])
        
        elif '},' in row[1]:
            raop_data.append(htemp)
            htemp = []
            header = True
        else:
            pass
   #Read in and sort all of the data. Remove some info that may not be needed.
    if 'request_id' in row[1] or\
    'request_title' in row[1] or\
    'request_text' in row[1] or\
    'received' in row[1] or\
    'flair' in row[1] or\
    'edited' in row[1]:
        t = row[1].replace(',', '')       
        t = t.split(':',2)
        temp.append(t[1])
    elif 'subreddits' in row[1] or 'requests' in row[1]:
        continue
    elif 'request_' in row[1] or\
    '_request' in row[1] or\
    'requester' in row[1]: 
        temp.append(find_number(row[1].replace(',', '')))
    elif '},' in row[1]:
        if len(temp) < 29:
            temp.insert(5,'')
        raop_data.append(temp)
        temp = []
    else:
        pass
        
with open('RAOP_Cleaned_Data.csv', 'wb') as ofile:    
    writer = csv.writer(ofile, delimiter=',', quotechar='"',quoting=csv.QUOTE_ALL)
    for r in raop_data:
        writer.writerow(r)        
        