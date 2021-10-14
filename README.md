# Packaged-food-ingredients-information-extractor-

## I) Webscraping:
- Open extractpara.py file:
- Come to #user relevant starts here line
- Put the ingredient name you want to get the information of:
- eg: ingredient_name="maltodextrin"
- Put all the relevant queries you want to search information about : in the querylist=['does ' +ingredient_name+ ' cause diseases','does '+ingredient_name+' cause cancer']
- Run the extractpara.py file

- In the same space where .py files are stored: A folder named "ingredients" will be created -> which will include folder with ingredient name -> into which 
- You will get two .txt files :
  1. infofile.txt -> contains all information extracted in paragraphs. Every paragraph starting with query and website name.
  2. websites visisted

## II) Filtering info
- Now one may want to filter the information file to get only specific information: 
- eg:if you want only cancer related information

- Go to filterer.py file:
- Come to #user relevant starts here line
- Provide all the related information:
- for example : 
  - cancerkwlist=['cancer','carcino','tumo','toxi','onco','poison'] (cancer related keywords)
  - domain_area='cancer'
  - ingredient_name='maltodextrin'
  - ingredient_name_rel=['sugar','malt','dextri'] (ingredient related keywords)

### NOTE: while providing keywords provide only specific keywords only, keep it minimum. (To avoid ambiguity)

- Run the filterer.py file.

- Check the folder you'll get a domain related folder -> which will include 4 .txt files: (As per our example domain name is "cancer")
  1. cancer_filteredinfo.txt -> (all cancer specific information) [filtering level-1]
  2. cancer_filteredinfo_namespecific.txt -> (cancer related info specific to ingredient name only) [filtering level-2]
  3. cancer_filteredinfo_namespecific_removed ambiguity.txt (words like might, myth, believed that, has been, not clear paragraphs are removed) [filtering level-3]
  4. cancerrelevant_phrases and result.txt [words and noun phrases which are relevant to cancer this file is just to check the purity of information for verification]

### This information can be further used to prepare data sheet. Use it for further analysis of ingredient information and use ML algorithms for classification and analysis.
