import requests
from bs4 import BeautifulSoup
import os
import re
import scriptures
import json

book_abr = {"Genesis":"GEN","Exodus":"EXO","Leviticus":"LEV","Numbers":"NUM","Deuteronomy":"DEU","Joshua":"JOS",
           "Judges":"JDG","Ruth":"RUT","I Samuel":"1SA","II Samuel":"2SA","I Kings":"1KI",
           "II Kings":"2KI","I Chronicles":"1CH","II Chronicles":"2CH","Ezra":"EZR","Nehemiah":"NEH",
           "Esther":"EST","Job":"JOB","Psalms":"PSA","Proverbs":"PRO","Ecclesiastes":"ECC",
           "Song of Solomon":"SNG","Isaiah":"ISA","Jeremiah":"JER","Lamentations":"LAM","Ezekiel":"EZK",
           "Daniel":"DAN","Hosea":"HOS","Joel":"JOL","Amos":"AMO","Obadiah":"OBA",
           "Jonah":"JON","Micah":"MIC","Nahum":"NAM","Habakkuk":"HAB","Zephaniah":"ZEP",
           "Haggai":"HAG","Zechariah":"ZEC","Malachi":"MAL","Matthew":"MAT","Mark":"MRK",
           "Luke":"LUK","John":"JHN","Acts":"ACT","Romans":"ROM","I Corinthians":"1CO",
           "II Corinthians":"2CO","Galatians":"GAL","Ephesians":"EPH","Philippians":"PHP","Colossians":"COL",
           "I Thessalonians":"1TH","II Thessalonians":"2TH","I Timothy":"1TI","II Timothy":"2TI","Titus":"TIT",
           "Philemon":"PHM","Hebrews":"HEB","James":"JAS","I Peter":"1PE","II Peter":"2PE",
           "I John":"1JN","II John":"2JN","III John":"3JN","Jude":"JUD","Revelation of Jesus Christ":"REV"}

dailyLight = {}

def get_day(myMonth,myDay):
    # Define some variable
    page_url = 'http://www.dailylightdevotional.org/'+ myMonth + '/'+ myMonth + myDay+'.html'
    day = {}
    when ="MORNING"

    # Retrieve the text of the day
    page = requests.get(page_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    # We use balise <TD> as no best markup can be found
    am_pm = soup.find('td')

    # Initiate a list of verse
    verses = []

    # Retrieve the list of raw verses + Ref
    verse_list = am_pm.text.split('\n\n')
    if len(verse_list) < 3:
        verse_list = [a.text for a in soup.find_all('p')]

    # Get the Date in Raw format
    fullDate = verse_list[0].strip()
    when = "MORNING"
    print(fullDate)

    # Loop trough all remaining verses
    for verse in verse_list[2:]:
        if verse.strip() == "EVENING" or verse.strip() == "Evening":
            day[when] = verses
            verses = []
            when = "EVENING"
        elif verse.strip() and verse.strip()[:3] != "var":
            # remove leading and trailing spaces, EOL, Tab
            verse = re.sub(r"   ",r"",verse.strip())
            verse = re.sub(r"\n",r"",verse)
            verse = re.sub(r"\t",r"",verse)

            # Remove dot notation for book reference
            verse = re.sub(r"([a-z])\.( [0-9])",r"\1\2",verse)
            verse = re.sub(r"([a-z])\.([0-9])",r"\1 \2",verse)

            # Repace comma separated chapter/verse by :
            verse = re.sub(r"([0-9]), ([0-9]+-)",r"\1:\2",verse)

            # Replace comma separated verse by hyphen
            # This deals with first 2 verses
            verse = re.sub(r"(\. )([a-zA-Z ]+ [0-9]+:)([0-9]+), ([0-9]+)",r"\1\2\3-\2\4",verse)
            # This one deals with an additional 3rd
            verse = re.sub(r"(-)([a-zA-Z ]+ [0-9]+:)([0-9]+), ([0-9]+)",r"\1\2\3-\2\4",verse)

            # Some reference are not handle right by scriptures package
            verse = re.sub(r"(Ex)( [0-9])",r"\1od\2",verse)
            verse = re.sub(r"(Exo)( [0-9])",r"\1d\2",verse)
            verse = re.sub(r"(Jud)( [0-9])",r"\1g\2",verse)
            verse = re.sub(r"(Thes)( [0-9])",r"\1s\2",verse)
            verse = re.sub(r"(Jude [0-9]+):",r"\1-",verse)
            verse = re.sub(r"John l([0-9:])",r"John 1\1",verse)
            verse = re.sub(r"Is.a ([0-9]+)",r"Isa \1",verse)

            # Some references are wrong in the original text
            # Apr 28th (1 Thess 6:16-18, should be thess 5,
            verse = re.sub(r"(I Thess) 6(:16-18)",r"\1 5\2",verse)
            # May 17th (Heb. 20, 21, should be Heb. 13:20, 21,
            verse = re.sub(r"(Heb) (20, 21)",r"\1 13:\2",verse)
            # June 8th (Matt 4:40 should be Mark 4:40)
            verse = re.sub(r"(Ma)tt (4:40)",r"\1rk \2",verse)
            # July 1st (Gal 5:27 should be Gat 5:22)
            verse = re.sub(r"(Gal) 5:27",r"\1 5:22",verse)
            # Oct 25th (Mark 18:19-20 should be Matt 18:19-20)
            verse = re.sub(r"(Ma)rk( 18:19)",r"\1tt\2",verse)
            verse = re.sub(r"(Ma)rk( 18:20)",r"\1tt\2",verse)
            # Nov 20th (Prov 56 should be Psam 56)
            verse = re.sub(r"Prov( 56)",r"Psa\1",verse)

            # Extract verse reference and text
            ref = scriptures.extract(verse)
            #print(ref)
            #print(verse)

            if ref :
                # retrieve the text from DailyLight
                verse_dailyLight = re.sub(r"(\.)([^.]*)$",r"\1",verse)
                verse_kjv = ""

                #print(ref)

                for book, chap1, verse1, chap2, verse2 in ref:
                    verse_kjv += get_verse_KJV(book,chap1,verse1) + " "

                verse_kjv = verse_kjv[:-1]
                current_verse = {"book":book,"book_abr":book_abr[book],"chapter":chap1,"verse1":verse1,"verse2":verse2}
                current_verse["verse_dailyLight"] = verse_dailyLight
                current_verse["verse_kjv"] = verse_kjv

                # Add to the verse collection
                if verse_kjv == verse_dailyLight :
                    current_verse["verse_type"] = "full"
                    #print("full")
                else :
                    current_verse["verse_type"] = "partial"
                    #print("partial")
                    #print(verse_dailyLight)
                    #print(verse_kjv)
                    #print(ref)
                verses.append(current_verse)

    day[when] = verses
    return(day)

def get_month(myMonth,maxDay):
    for i in range(1,10):
        myday = get_day(myMonth,'0'+str(i))
        dailyLight[myMonth+'0'+str(i)] = myday
        #print(str(i) + " morning :" + str(len(myday["MORNING"]))+ " evening :" + str(len(myday["EVENING"])))
    for i in range(10,maxDay+1):
        myday = get_day(myMonth,str(i))
        dailyLight[myMonth+str(i)] = myday
        #print(str(i) + " morning :"  + str(len(myday["MORNING"]))+ " evening :" + str(len(myday["EVENING"])))

def get_verse_KJV(book,chapter,verse):
    url = 'https://www.bible.com/bible/1/' + book_abr[book] + '.' + str(chapter) + '.KJV'
    #print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    span_text = soup.find('span', attrs={'class':'verse v'+str(verse)})
    #print(span_text)
    verses = span_text.find_all('span', attrs={'class':'content'})
    verse = ""
    for verse_text in verses:
        verse += verse_text.text
    return(verse.strip())



get_month('01',31)
get_month('02',29)
get_month('03',31)
get_month('04',30)
get_month('05',31)
get_month('06',30)
get_month('07',31)
get_month('08',31)
get_month('09',30)
get_month('10',31)
get_month('11',30)
get_month('12',31)

# Export as JSON fil    e
jsonfile = json.dumps(dailyLight)
f = open("dailyLight.json","w")
f.write(jsonfile)
f.close()

# Test area
#print(book_abr['John'])
#get_verse_KJV('Deuteronomy', 31, 8)
#get_verse_KJV('John', 17, 24)
#get_verse_KJV('Mark', 1, 34)
#get_day('04','23')
#get_month('01',31)

## Remaining Issues to be fixed
# Missing Reference in text or wrong split(Feb10, Mar 28, Apr 24, Aug 1, Dec 17, Dec 28)
# Wrong Tagging <p> instead of </p> screwing the last verse (May7)
