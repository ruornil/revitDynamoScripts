"""MIT License

Copyright (c) 2019 M. Cenk Tuanboylu

A script for appending revision numbers to .dwg file names, and appending sorting prefix to .pdf files
from a csv list. CSV file must have headers on 1 st row named dwgName, pdfName, pdfSort. Script will search
for the specified folder, if the file extensiond is .dwg and it is on the csv list, it will replace the .dwg
filename with the pdf name, if the file extension is .pdf and it is on the csv list, it will replace the .pdf
filename with the pdfSort name.
""" 


import os
import pandas as pd

p = (r"C:\Users\ctunaboylu.GHAFARITR\Desktop\ARC")
df = pd.read_csv(r"C:\Users\ctunaboylu.GHAFARITR\Desktop\ARC\sheetListForSort.csv", engine='python')


for filename in os.listdir(p):
    filename_without_ext = os.path.splitext(filename)[0]
    extension = os.path.splitext(filename)[1]
    if extension == r'.pdf':
        try:
            new_file_name = df.loc[df[r'pdfName'] == str(filename_without_ext)][r'pdfSort'].values[0]
            new_file_name_with_ext = new_file_name + extension
            os.rename(os.path.join(p,filename),os.path.join(p,new_file_name_with_ext))
        except:
            print(filename + r' pdf not found')
    if extension == r'.dwg':
        try:
            new_file_name = df.loc[df[r'dwgName'] == str(filename_without_ext)][r'pdfName'].values[0]
            new_file_name_with_ext = new_file_name + extension
            os.rename(os.path.join(p,filename),os.path.join(p,new_file_name_with_ext))
        except:
            print(filename + r' dwg not found')
