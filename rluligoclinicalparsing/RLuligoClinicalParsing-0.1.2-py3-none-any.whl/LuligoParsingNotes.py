
#import RLuligoClinicalParsing.constants as constants

import pandas as pd
import re
def LuligoParsingNotes(csvfile, fsep, tdelimiter, fencode='utf8'):
    sep = '\u0000'
    df = pd.read_csv(csvfile,  sep=sep , encoding=fencode, dtype=str, escapechar='\\', header=None, names=['text'], quoting=3 )
    
    #remove empty fields wihtout a quote("name",,"lastname")
    df = df.text.replace(to_replace=f'{tdelimiter}{fsep}{fsep}{tdelimiter}', regex=True, value=f'{sep}{sep}') 
    df = df.to_frame()
    #second pass for pattern like ",,,"" remove empty fields wihtout a quote("name",,"lastname")
    df = df.text.replace(to_replace=f'{tdelimiter}{fsep}{fsep}{fsep}{tdelimiter}', regex=True, value=f'{sep}{sep}{sep}') 
    df = df.to_frame()
    
    #third pass for pattern like ",,,"" remove empty fields wihtout a quote("name",,"lastname")
    df = df.text.replace(to_replace=f'{tdelimiter}{fsep}{fsep}{fsep}{fsep}{tdelimiter}', regex=True, value=f'{sep}{sep}{sep}{sep}') 
    df = df.to_frame()

    #special case for nested pipes
    if(fsep == '|'):
        df = df.text.replace(to_replace=f'{tdelimiter}\|{tdelimiter}', regex=True, value=sep)
    else:
        df = df.text.replace(to_replace=f'{tdelimiter}{fsep}{tdelimiter}', regex=True, value=sep) 
    df = df.to_frame()
    
    
    #removes first and last text identifiers
    pattern = f'^{ tdelimiter}|{tdelimiter}$',
    df = df.text.replace(to_replace=pattern, regex=True, value='')
    df = df.to_frame()
    
    if(fsep == '|'):
        #adding more pattern cases (replace nested pipes in Text CHN)
        #patern = '((?<![\\])[|])'
        df = df.text.replace(to_replace=r'((?<![\\])['+fsep+'])', regex=True, value='\|')
        df = df.to_frame()
    else:
        #adding patterner to eascape nested text delimitters (``) #SSM Health
        df = df.text.replace(to_replace=r'((?<![\\])['+tdelimiter+'])', regex=True, value=f'\\{tdelimiter}')
        df = df.to_frame()
    
    #removes last escape character in the line (#Avera)
    pattern = f'\"$',
    df = df.text.replace(to_replace=pattern, regex=True, value='')
    df = df.to_frame()
    
   #################################SET HEADERS AND FIELDS
    
    df = df.text.str.split(pat=sep,expand=True)
    new_header = df.iloc[0] #grab the first row for the header
    df = df[1:] #take the data less the header row
    df.columns = new_header #set the header row as the df header
    df.drop(df[df[df.columns[0]] == f'{df.columns[0]}'].index, inplace=True)

    return df