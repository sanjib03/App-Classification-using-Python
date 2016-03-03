#!/usr/bin/env python
# -*- coding: utf-8 -*- 

python desc_extract.py $1

f_name=$1".txt"

echo "App description successfully extracted and stored in " f_name

echo "Processing the raw description file"

python dict_build.py $f_name

cd dict

dict_name="p_"$f_name

echo "Comparing the app description file against pre-built dictionaries"
python SimilarityCal.py $dict_name

