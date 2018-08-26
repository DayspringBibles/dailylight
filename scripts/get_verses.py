import requests 
from lxml import html
import numpy
import csv
import re
from numpy import genfromtxt
import time
def main():

    # re search complie
    chapter_number = re.compile('\d+(?=:)')
    book_name = re.compile('.*?(?=\d+:)')
    book_name_list = genfromtxt('book_abreviations.csv', delimiter=',',dtype=None)
    #
    date_list_array = [['?d=0101', '?d=0102', '?d=0103', '?d=0104', '?d=0105', '?d=0106', '?d=0107', '?d=0108', '?d=0109', '?d=0110', '?d=0111', '?d=0112', '?d=0113', '?d=0114', '?d=0115', '?d=0116', '?d=0117', '?d=0118', '?d=0119', '?d=0120', '?d=0121', '?d=0122', '?d=0123', '?d=0124', '?d=0125', '?d=0126', '?d=0127', '?d=0128', '?d=0129', '?d=0130', '?d=0131']
    , ['?d=0201', '?d=0202', '?d=0203', '?d=0204', '?d=0205', '?d=0206', '?d=0207', '?d=0208', '?d=0209', '?d=0210', '?d=0211', '?d=0212', '?d=0213', '?d=0214', '?d=0215', '?d=0216', '?d=0217', '?d=0218', '?d=0219', '?d=0220', '?d=0221', '?d=0222', '?d=0223', '?d=0224', '?d=0225', '?d=0226', '?d=0227', '?d=0228']
    , ['?d=0301', '?d=0302', '?d=0303', '?d=0304', '?d=0305', '?d=0306', '?d=0307', '?d=0308', '?d=0309', '?d=0310', '?d=0311', '?d=0312', '?d=0313', '?d=0314', '?d=0315', '?d=0316', '?d=0317', '?d=0318', '?d=0319', '?d=0320', '?d=0321', '?d=0322', '?d=0323', '?d=0324', '?d=0325', '?d=0326', '?d=0327', '?d=0328', '?d=0329', '?d=0330', '?d=0331']
    
    , ['?d=0401', '?d=0402', '?d=0403', '?d=0404', '?d=0405', '?d=0406', '?d=0407', '?d=0408', '?d=0409', '?d=0410', '?d=0411', '?d=0412', '?d=0413', '?d=0414', '?d=0415', '?d=0416', '?d=0417', '?d=0418', '?d=0419', '?d=0420', '?d=0421', '?d=0422', '?d=0423', '?d=0424', '?d=0425', '?d=0426', '?d=0427', '?d=0428', '?d=0429', '?d=0430']
    , ['?d=0501', '?d=0502', '?d=0503', '?d=0504', '?d=0505', '?d=0506', '?d=0507', '?d=0508', '?d=0509', '?d=0510', '?d=0511', '?d=0512', '?d=0513', '?d=0514', '?d=0515', '?d=0516', '?d=0517', '?d=0518', '?d=0519', '?d=0520', '?d=0521', '?d=0522', '?d=0523', '?d=0524', '?d=0525', '?d=0526', '?d=0527', '?d=0528', '?d=0529', '?d=0530', '?d=0531']
    , ['?d=0601', '?d=0602', '?d=0603', '?d=0604', '?d=0605', '?d=0606', '?d=0607', '?d=0608', '?d=0609', '?d=0610', '?d=0611', '?d=0612', '?d=0613', '?d=0614', '?d=0615', '?d=0616', '?d=0617', '?d=0618', '?d=0619', '?d=0620', '?d=0621', '?d=0622', '?d=0623', '?d=0624', '?d=0625', '?d=0626', '?d=0627', '?d=0628', '?d=0629', '?d=0630', '?d=0701']
    , ['?d=0702', '?d=0703', '?d=0704', '?d=0705', '?d=0706', '?d=0707', '?d=0708', '?d=0709', '?d=0710', '?d=0711', '?d=0712', '?d=0713', '?d=0714', '?d=0715', '?d=0716', '?d=0717', '?d=0718', '?d=0719', '?d=0720', '?d=0721', '?d=0722', '?d=0723', '?d=0724', '?d=0725', '?d=0726', '?d=0727', '?d=0728', '?d=0729', '?d=0730', '?d=0731', '?d=0801']
    , ['?d=0802', '?d=0803', '?d=0804', '?d=0805', '?d=0806', '?d=0807', '?d=0808', '?d=0809', '?d=0810', '?d=0811', '?d=0812', '?d=0813', '?d=0814', '?d=0815', '?d=0816', '?d=0817', '?d=0818', '?d=0819', '?d=0820', '?d=0821', '?d=0822', '?d=0823', '?d=0824', '?d=0825', '?d=0826', '?d=0827', '?d=0828', '?d=0829', '?d=0830', '?d=0831', '?d=0901']
    , ['?d=0902', '?d=0903', '?d=0904', '?d=0905', '?d=0906', '?d=0907', '?d=0908', '?d=0909', '?d=0910', '?d=0911', '?d=0912', '?d=0913', '?d=0914', '?d=0915', '?d=0916', '?d=0917', '?d=0918', '?d=0919', '?d=0920', '?d=0921', '?d=0922', '?d=0923', '?d=0924', '?d=0925', '?d=0926', '?d=0927', '?d=0928', '?d=0929', '?d=0930']
    , ['?d=1001', '?d=1002', '?d=1003', '?d=1004', '?d=1005', '?d=1006', '?d=1007', '?d=1008', '?d=1009', '?d=1010', '?d=1011', '?d=1012', '?d=1013', '?d=1014', '?d=1015', '?d=1016', '?d=1017', '?d=1018', '?d=1019', '?d=1020', '?d=1021', '?d=1022', '?d=1023', '?d=1024', '?d=1025', '?d=1026', '?d=1027', '?d=1028', '?d=1029', '?d=1030', '?d=1031']
    , ['?d=1101', '?d=1102', '?d=1103', '?d=1104', '?d=1105', '?d=1106', '?d=1107', '?d=1108', '?d=1109', '?d=1110', '?d=1111', '?d=1112', '?d=1113', '?d=1114', '?d=1115', '?d=1116', '?d=1117', '?d=1118', '?d=1119', '?d=1120', '?d=1121', '?d=1122', '?d=1123', '?d=1124', '?d=1125', '?d=1126', '?d=1127', '?d=1128', '?d=1129', '?d=1130']
    , ['?d=1201', '?d=1202', '?d=1203', '?d=1204', '?d=1205', '?d=1206', '?d=1207', '?d=1208', '?d=1209', '?d=1210', '?d=1211', '?d=1212', '?d=1213', '?d=1214', '?d=1215', '?d=1216', '?d=1217', '?d=1218', '?d=1219', '?d=1220', '?d=1221', '?d=1222', '?d=1223', '?d=1224', '?d=1225', '?d=1226', '?d=1227', '?d=1228', '?d=1229', '?d=1230', '?d=1231']]
    
    #date_list_array = [['?d=0101']]

    #https://www.studylight.org/devotionals/dlp/?d=0401
    with open('verse_list.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(['Day', 'Time','Section','Book','Chapter', 'Verse'])


        for date_list in date_list_array:
            for i in date_list:
                verses = get_verses(i) 
                print(verses[0])            
                verse_number = 1
                iterate = 0
                # morning
                for a in verses[1]:
                    try:
                        if verses[3][iterate] == verse_number:
                            iterate +=1
                            spamwriter.writerow([verses[0],'morning','section', book_name.search(a.replace(';',':')).group(), chapter_number.search(a.replace(';',':')).group(), "'" + a.replace(';',':').split(':',1)[1].replace(',','-')])

                        else:
                            spamwriter.writerow([verses[0],'morning','', book_name.search(a.replace(';',':')).group(), chapter_number.search(a.replace(';',':')).group(),"'" + a.replace(';',':').split(':',1)[1].replace(',','-')])
                    except:
                        spamwriter.writerow(['error','', '', '',''])
                        continue
                    verse_number +=1
                    #print(verse_number)

                verse_number = 1
              
                # evening
                for a in verses[2]:
                    try:
                        if verses[3][iterate] == verse_number:
                            iterate +=1
                            iterate = min(iterate, len(verses[3]))

                            spamwriter.writerow([verses[0],'evening','section', book_name.search(a.replace(';',':')).group(), chapter_number.search(a.replace(';',':')).group(),"'" + a.replace(';',':').split(':',1)[1].replace(',','-')])
                        else:
                            spamwriter.writerow([verses[0],'evening','', book_name.search(a.replace(';',':')).group(), chapter_number.search(a.replace(';',':')).group(),"'" + a.replace(';',':').split(':',1)[1].replace(',','-')])
                    except:
                        spamwriter.writerow(['error','', '', '',''])
                        continue
                    verse_number +=1
                time.sleep(20)
            time.sleep(60)


def get_verses(date):

    try:
        page = requests.get('https://www.studylight.org/devotionals/dlp/'+date)
    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(5)
        print("Was a nice sleep, now let me continue...")
        pass

    # page formated html
    tree = html.fromstring(page.content)
    #<h2 class="extra_title">Devotional for January 2</h2>

    day = tree.xpath('//h2[@class="extra_title"]/text()')
    day = day[0].split("Devotional for ", 1)[1]
  
    verse_list_morning = tree.xpath('//div[@class="standard"]/p[position()<last()]/span[@class="scriptRef" ]/text()')#and following-sibling::div
    verse_list_evening = tree.xpath('//div[@class="standard"]/p[last()]/span[@class="scriptRef"]/text()')

    section_breaks_morning = tree.xpath('//p[not(@class) and count(*)=0]/text()')
    section_breaks= 1# len(section_breaks_morning)
    section_break_array = [1]
    for i in section_breaks_morning:
        section_breaks = (section_breaks+len(re.split('\x97',i)))
        if section_breaks >=len(verse_list_evening):
            section_break_array.append(1)
            section_breaks = section_breaks-len(verse_list_evening)
        if section_breaks !=1:
            section_break_array.append(section_breaks)

    #print(day,verse_list_morning, verse_list_evening,section_break_array)
    return day,verse_list_morning, verse_list_evening,section_break_array

def book_lookup(name):

    my_data = genfromtxt('book_abreviations.csv', delimiter=',',dtype=None)


    book = next((item for item in my_data if item[[1]] == name))

    return book[0]


main()

