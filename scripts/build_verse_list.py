import requests 
from lxml import html
import csv

def main():
    

    with open('test_references.csv') as csvfile, open('test_references 2.csv', 'wb') as csvfile2:
        #spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        fieldnames = spamreader.fieldnames + ['text']

        csvwriter = csv.DictWriter(csvfile2, fieldnames)
        csvwriter.writeheader()
        for text, row in enumerate(spamreader, 1):
            if row['day'] not in (None, ""):
                
                verse = get_verse(row['book'], row['chapter'], row['verse'])

                try:
                    csvwriter.writerow(dict(row,  text = verse))
                except:
                    pass
                #print(row['book'])
                #print(row['chapter'])
                #print(row['verse'])

                #print(row)

    
def get_verse(book, chapter, verse):

    page = requests.get('https://www.bible.com/bible/351/' + book + '.' + chapter + '.BYSB')

    # page formated html
    tree = html.fromstring(page.content)

    if "-" not in verse:
        verse_text = tree.xpath('//span[@class="verse v' + verse + '"]/span[@class="content"]/text()')[0]

    else: 
        verse1 = int(verse.split('-')[0])
        verse2 = int(verse.split('-')[1])
        verse_text = ''
        while verse1 <= verse2:
            
            verse_text += str(tree.xpath('//span[@class="verse v' + str(verse1) + '"]/span[@class="content"]/text()')[0])

            verse1 += 1
                 
    return(verse_text)


main()
