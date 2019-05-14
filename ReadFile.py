import os
from GlobalName import *
import re


class ReadFile:
    #read data format MSR
    def read_data(self,filename):
        global kalimatAlign
        bukaFile = open(os.path.join(filename), "r")
        for line in bukaFile.readlines():
            if line.split(None,1)[0] != '#' and line.split(None,1)[0] != "NULL" :
                x = line.rstrip('\n')

            if line.split(None,1)[0] == "NULL" :
                #dipisahkan menggunakan regular expression
                y = [x, re.sub('\s*(?:\(\{[^/]*/\s*/\s*}\)|NULL)\s*',' ', line)]
                kalimatAlign.append(y)

                #untuk mencari kata yang ada gold anotation/ gold standard
                goldAnno = re.findall('\s*(\(\{[^/]*/\s*/\s*}\))\s*',line)
                goldAnnotation.append(goldAnno)

