import requests 
from lxml import html
import csv

def main():
    verse = get_verse('1CO', '1', '1-2')

    print(verse)  

    
def get_verse(book, chapter, verse):

    page = requests.get('https://www.bible.com/bible/351/' + book + '.' + chapter + '.BYSB')

    # page formated html
    tree = html.fromstring(page.content)

    if "-" not in verse:
        verse_text = tree.xpath('//span[@class="verse v' + verse + '"]/span[@class="content"]/text()')

    else: 
        verse1 = int(verse.split('-')[0])
        verse2 = int(verse.split('-')[1])
        verse_text = ''
        while verse1 <= verse2:
            
            verse_text += str(tree.xpath('//span[@class="verse v' + str(verse1) + '"]/span[@class="content"]/text()')[0])

            verse1 += 1

    return(verse_text)

main()
