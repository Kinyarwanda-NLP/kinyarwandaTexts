 # coding=utf-8
import os
import json
import nltk
from nltk.tokenize import word_tokenize
import re
#stopwods : useless words ( uhmm, amm)
#from nltk.corpus import stopwords
#nltk.download('stopwords')
rootdir = 'C:/Users/Sababu/Desktop/Kinyarwanda/Digital_Umuganda_data/words'
db =[]

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".txt"):
            rd = open(filepath, encoding="ISO-8859-1").read().lower()
            wrd = word_tokenize(rd)
            words = [word for word in wrd if word.isalpha()]   
                    
            neww = words
            db.extend(neww)
 
  
def remove(list): 
    pattern = '[0-9]'
    list = [re.sub(pattern, '', i) for i in list] 
    return list  

new_file=remove(db) 
count = list(set(db)) 

print(len(db)) #all words in all .txt files including common
#remove special characters & numbers
new_file=remove(db) 
new_filee = ''.join(e for e in new_file if e.isalnum()) 
print(len(new_filee))
print(len(count))# unique words



#putting them into one file

with open("C:/Users/Sababu/Desktop/Kinyarwanda/Digital_Umuganda_data/words.txt", "w+") as filehandle:
    json.dump(count, filehandle,indent=2)

