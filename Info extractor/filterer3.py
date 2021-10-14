import urllib.request
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen    
import nltk
from nltk import *
from textblob import TextBlob 
from nltk.corpus import wordnet
import nltk 
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag
from textblob import TextBlob 
from nltk.corpus import wordnet 
from nltk.corpus import wordnet as wn
import os
#import similarity3
#from similarity3 import*

def getallnounphrases(text):
    blob=TextBlob(text)
    d=blob.noun_phrases
    d2=[]
    for i in d:
        i=i.replace('‘','')
        i=i.replace('’','') 
        d2.append(i)
            
    return(d2)

def filteraccordingtodomain(ingredient_name,keylist,domain_area,ingredient_name_rel):

    #to ensure folder path
    cdir1="ingredients"
    baap=os.path.dirname(os.path.abspath(__file__))+'/'
    fpathd1=os.path.join(baap, cdir1)
    main_info_folder=fpathd1+'/'

    try:  
        os.mkdir(fpathd1)

    except OSError as error:  
        pass   
    #to ensure folderpath

    pathd1=main_info_folder+ingredient_name+'/'

    file_path1ofinfo=pathd1+'/'+ingredient_name+'_info.txt'
    
    directory2=domain_area

    parent_dir2=pathd1

    pathd2=os.path.join(parent_dir2, directory2)  
    try:  
        os.mkdir(pathd2)  
    except OSError as error:  
        pass

    file_path2=pathd2+'/'+domain_area+'_filteredinfo.txt'
    file_path3=pathd2+'/'+domain_area+'_filteredinfo_namespecific.txt'
    f=open(file_path2,'a',encoding="utf-8", errors='ignore')
    f.write('******'+domain_area+'*******')
    f.write('\n')
    f.close()
    f=open(file_path1ofinfo, "r", encoding="utf-8", errors='ignore')
    text=f.read()
    f.close()
    textlist=text.split('---endofparagraph@rohit1234---')

    for i in keylist:
        for r in textlist:
            if i in r:
                f=open(file_path2,'r',encoding="utf-8", errors='ignore')
                filterfiletext=f.read()
                f.close()
                if r not in filterfiletext:
                    f=open(file_path2,'a',encoding="utf-8", errors='ignore')
                    f.write(r)
                    f.write('---endofparagraph@rohit1234---')
                    f.write('\n')
                    f.close()
    f=open(file_path3,'a',encoding="utf-8", errors='ignore')
    f.write('*********name specific*********')
    f=open(file_path2,'r',encoding="utf-8", errors='ignore')
    h=f.read()
    f.close()
    hlist=h.split('---endofparagraph@rohit1234---')
    for i in hlist:
        for t in ingredient_name_rel:
            if t in i:
                f=f=open(file_path3,'r',encoding="utf-8", errors='ignore')
                k=f.read()
                f.close()
                if i not in k:
                    f=open(file_path3,'a',encoding="utf-8", errors='ignore')
                    f.write(i)
                    f.write('---endofparagraph@rohit1234---')
                    f.write('\n')
                    f.close()
    
    

def filtertorelevantnounphrases(ingredient_name,domain_area,keylist):

    #to ensure folder path
    cdir1="ingredients"
    baap=os.path.dirname(os.path.abspath(__file__))+'/'
    fpathd1=os.path.join(baap, cdir1)
    main_info_folder=fpathd1+'/'
    
    try:  
        os.mkdir(fpathd1)
        
    except OSError as error:  
        pass   
    #to ensure folderpath


    parent_dir1=main_info_folder+ingredient_name+"/"+domain_area+"/"
    file_path1=parent_dir1+domain_area+"_filteredinfo_namespecific.txt"
    file_path2=parent_dir1+domain_area+"_filteredinfo_namespecific_removed ambiguity.txt"
    file_path3=parent_dir1+domain_area+"relevant_phrases and result.txt"
    f=open(file_path3, "w", encoding="utf-8", errors='ignore')
    #f.write('***the relevant file***')
    f.close()

    f=open(file_path1, "r", encoding="utf-8", errors='ignore')
    text=f.read()
    f.close()
    ambiguouswordslist=['myt','mys','belie','ambigu','fake','pseudo','may','migh','possi','no','not','nt',"n't",'possi']

    textlist=text.split('---endofparagraph@rohit1234---')
    f=open(file_path2, "a", encoding="utf-8", errors='ignore')
    f.write('****abiguity stripped****')
    f.close()
    for i in textlist:
        if '***' not in i:    
            ilist=nltk.sent_tokenize(i)
            ilistnew=[]
        #print(ilist)
            for r in ilist:
                for w in ambiguouswordslist:
                    if w not in r and r not in ilistnew:
                        ilistnew.append(r)

            inew=' '.join(ilistnew) 
    
            f=open(file_path2, "r", encoding="utf-8", errors='ignore')
            text2=f.read()
            f.close()
            if inew not in text2:
                f=open(file_path2, "a", encoding="utf-8", errors='ignore')
                f.write(inew)
                f.write('\n')
                f.write('---endofparagraph@rohit1234---')
                f.close()
    
    f=open(file_path2, "r", encoding="utf-8", errors='ignore')
    text3=f.read()
    text3list=text3.split('---endofparagraph@rohit1234---')
    text3text=' '.join(text3list)
    #cancerkwlist=['cancer','carcino','tumo','toxi','onco','poison']
    
    q=[]


    aq=getallnounphrases(text3text)
    for r in aq:
        for w in keylist:
            if w in r and r not in q: 
                f=open(file_path3, "r", encoding="utf-8", errors='ignore')
                textrelevant=f.read()
                f.close()
                q.append(r)
                if '***the relevant file***' not in textrelevant:
                    f=open(file_path3, "a", encoding="utf-8", errors='ignore')
                    f.write('***the relevant file***\n')
                    f.close()
                if r not in textrelevant:
                    
                    f=open(file_path3, "a", encoding="utf-8", errors='ignore')
                    f.write(r)
                    f.write(',\n')
                    f.close()
    

#to ensure folder path
cdir1="ingredients"
baap=os.path.dirname(os.path.abspath(__file__))+'/'
fpathd1=os.path.join(baap, cdir1)
main_info_folder=fpathd1+'/'

try:  
    os.mkdir(fpathd1)
    
except OSError as error:  
    pass   
#to ensure folderpath
            
########################################################################################################
# user relevant starts here    

cancerkwlist=['cancer','carcino','tumo','toxi','onco','poison']
keylist=cancerkwlist[:]
domain_area='cancer'
ingredient_name='maltodextrin'
ingredient_name_rel=['sugar','malt','dextri']
#ingredient_name_rel=['tartrazine','yellow']
filteraccordingtodomain(ingredient_name,keylist,domain_area,ingredient_name_rel)
pathd1=main_info_folder+ingredient_name+'/'
file_path1=pathd1+'/'+ingredient_name+'_info.txt'
filtertorelevantnounphrases(ingredient_name,domain_area,keylist)

print("done!!")