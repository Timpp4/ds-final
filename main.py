import time
import logging
from pywikiapi import wikipedia
from finalPath import *

class article:
    name = ""
    titles = []
    depth = 0

input("PLEASE CHANGE FILENAME FROM main.py AND finalPath.py AND COMMENT OUT THIS MESSAGE AND THE quit() FUNCTION")
quit()

# Error logging
logging.basicConfig(filename='', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

# Connect to English Wikipedia
site = wikipedia('en')

# Clean Existing Files
print("Deleting old files...")
f = open("dict.txt", "w")
f.write("")
f.close()
err_path = 'C:/Users/tumpp/Desktop/torstaiDS/tmp/errLog.log'
f = open(err_path, "w")
f.write("")
f.close()
print("Old files deleted.")

def getAllLinks(title, data, depth):
    titles_tmp = []
    for page in site.query_pages(titles=[title], prop=['links'], pllimit=500, plnamespace=0):
        for t in page.links:
            titles_tmp.append(t["title"])
        art = article()
        art.name = page.title
        art.titles = titles_tmp
        art.depth = depth
        data.append(art)
    return data

def checkIfExists(data, endPage):
    for art in data:
        for i in art.titles:
            if (str(i).lower() == str(endPage).lower()):
                return True
    return False

def main():
    data = []
    find = True
    counter = 1
    tmp = 1

    start = input("From: ")
    end = input("To: ")
    
    data = getAllLinks(start, data, counter)

    if checkIfExists(data, end):
        find = False

    while find == True:
        try:
            for art in data:
                if art.depth == counter:
                    word = "*"
                    print("\nSearching for links in: "+art.name + " (" + str(len(art.titles)) + " links)")
                    for i in art.titles:
                        print(word, end="")
                        try:
                            data = getAllLinks(i, data, counter+1)
                        except Exception as err:
                            logger.error(err)
        except Exception as err:
            logger.error(err)

        for art in data:
            if checkIfExists(data, end):
                find = False
                break
        
        counter += 1
        if counter == 3:
            print("\nMax depth reached!")
            f = open("dict.txt", "a", encoding="utf-8")
            for art in data:
                f.write(str(tmp) + ";" + art.name + ";" + str(art.depth) + ";" + '|'.join(art.titles) + "\n")
                tmp += 1
            f.close()
            finalPath(start, end, counter, data)
            counter = 0
            break
    if (counter != 0):
        f = open("dict.txt", "a", encoding="utf-8")
        for art in data:
            f.write(str(tmp) + ";" + art.name + ";" + str(art.depth) + ";" + '|'.join(art.titles) + "\n")
            tmp += 1
        f.close()
        finalPath(start, end, counter, data)


start_time = time.time()
main()
print("\n************* EOF *************")
print("**** Run time %s seconds" % round((time.time() - start_time), 2))
print("*******************************\n")