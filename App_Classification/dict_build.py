#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import unicodedata
import string
import sys
import os
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import *


#Creating the filename from arguments
file_name = sys.argv[1]

#Reading the file contents and converting into lower case
f = open(file_name,"r").read().lower()

#Removing non ascii characters
#f = f.decode('utf-8)
stripped = lambda s: "".join(i for i in f if 31 < ord(i) < 127)
f = stripped("\ba\x00b\n\rc\fd\xc3")

#Tokenizing
tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
f_tokens = tokenizer.tokenize(f)

#Stop words Removal
sw = stopwords.words("english")
f_tok_sw = [i for i in f_tokens if i not in sw]

#Remove punctuation marks and junk characters
f_nopun = str(f_tok_sw).translate(None, string.punctuation)

#Removing all numerical, special characters. Retaining only letters in english alphabet
f_all_char = re.sub("[^a-zA-Z]"," ",f_nopun)

#Removing extra blank spaces
f_final = ' '.join(f_all_char.split())
f_final_tok = tokenizer.tokenize(f_final)
f_final_tok = sorted(set(f_final_tok))

#USE stemming if you feel NECESSARY
stemmer_p = PorterStemmer()
f_stem_p= [stemmer_p.stem(i) for i in f_final_tok]

#Removing words of length less than 3
shortword = re.compile(r'\W*\b\w{1,3}\b')
f_final_list_p = shortword.sub('', str(f_stem_p))


#Writing the contents to a file
output_file_p = open("../Documents/App_Classification/dict/p_"+sys.argv[1],"w")
output_file_p.write(str(f_final_list_p))
output_file_p.close()

