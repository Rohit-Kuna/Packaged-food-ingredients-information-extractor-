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

def sorter(ylink, ingredient_name, query, pathd1):
    url=ylink
    file_path1=pathd1+'/'+ingredient_name+'_info.txt'
    file_path2=pathd1+'/websitesvisited.txt'
    file_path3=pathd1+'/websitesthatdeniedextraction.txt'
    try:
        req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = bs(webpage, "html.parser") 
        paragraph=soup.find_all('p')
        f=open(file_path1, "a", encoding="utf-8", errors='ignore')
        f.write('******'+query+'*******')
        f.write(':\t')
        f.write('******'+url+'******')
        f.write('\n')    
        f.write('\n')
        f.close()
        for i in paragraph:
            f=open(file_path1, "r", encoding="utf-8", errors='ignore')
            text=f.read()
            f.close() 
            if i.get_text() not in text:
                f = open(file_path1, "a", encoding="utf-8", errors='ignore')
                f.write(i.get_text())
                f.write('\n')
                f.write('---endofparagraph@rohit1234---')
                f.close()

        f=open(file_path2, "a", encoding="utf-8", errors='ignore')
        f.write(url)
        
        f.write('\n')
        f.close()

    except Exception as e:
        f=open(file_path3, "a", encoding="utf-8", errors='ignore')
        f.write(url)
        f.write('\n')
        f.write('****'+e+'****')
        f.write('\n')
        f.close()
           
    
    
    #file_path1=pathd1+'/'+ingredient_name+'_info.txt'
    #file_path1='F:/ROHIT/Python programming/project1/ingredients/'+ ingredient_name +'/'+ ingredient_name +'_info.txt'
        
    

def writesortedinfofile(ingredient_name, query,pathd1):
#getting websearches
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
    from urllib.request import Request, urlopen
    import requests, bs4, webbrowser, re  
    # to search 
    #query = "'"+query+"'"
    #query = " "
    listoflinks=[]  
    for j in search(query, tld="com", num=15, stop=10, pause=2): 
        #webbrowser.open(j) 
        listoflinks.append(j)
    u=[]
    uimp=[]
    unew=[]
    ufilt=[]
    mostimpsites=['healthline','nutri','india','life','heal','nourish','noshly','know','dr','doc','fact','check','arti','chem','fda','ask','is','choice','draxe','well','fit','live','science','very','havard','wiki','medici','webmd','justgotochef','drthadgala','health','food','ncbi','gov','medi']
    for i in listoflinks:
        x=i.split('#')
        u.append(x[0])
    
    u=list(set(u))
    print('u:\t')
    print(u)
    
    for r in mostimpsites:
        for p in u:
            if r in p:
                uimp.append(p)

    uimp=list(set(uimp))  
    print('uimp:\t')
    print(uimp)
    
    for r in u:
        if r not in uimp:
            unew.append(r) 
    unew=list(set(unew))        
    
    file_path2=pathd1+'/websitesvisited.txt'
    f=open(file_path2, "a", encoding="utf-8", errors='ignore')
    f.close()
    f=open(file_path2, "r", encoding="utf-8", errors='ignore')
    websitesvisited=f.read()
    f.close()
    #theweblist=websitesvisited.split(',')
    #theweblist=list(set(theweblist))
    
    for k in uimp:
        if k not in websitesvisited:
            ufilt.append(k)
    
    
    ufilt=list(set(ufilt))
    print(ufilt)
    
    for y in ufilt:
        print(y)
        sorter(y,ingredient_name,query,pathd1) 


def mineingredientinfolarge(ingredient_name,querylist):
    directory1=ingredient_name
    parent_dir1=main_info_folder
    pathd1=os.path.join(parent_dir1, directory1)

    try:  
        os.mkdir(pathd1)
        
    except OSError as error:  
        pass   

    for i in querylist:
        writesortedinfofile(ingredient_name, i,pathd1)

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




################################################################################################
#user relevant starts here

ingredient_name='maltodextrin'
    
querylist=['does ' +ingredient_name+ ' cause diseases','does '+ingredient_name+' cause cancer','is '+ingredient_name+' bad for gut health','is '+ingredient_name+' bad for stomach','benefits of '+ingredient_name,'is '+ingredient_name+' harmful','is '+ingredient_name+' bad for brain', 'is '+ingredient_name+' bad for heart']
#querylist=['is '+ingredient_name+' bad for gut health','does ' +ingredient_name+ ' cause diseases','is '+ingredient_name+' bad for stomach']   

mineingredientinfolarge(ingredient_name,querylist)