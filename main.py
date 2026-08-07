text = '''
I once made a remark about the hidden books of the Bible. A certain luke, kept people looking so hard for facts, and for others, it was a revelation. Some were in a jam, especially since the names of the books were not capitalized. But the truth finally struck home to numbers of our readers. To others it was a job. We want it to be a most fascinating little moment for you. Yes, there will be some really easy ones to spot. Others may require judges to help find them. I will  quickly admit it usually takes the preacher to find one of them, and there will be loud lamentations when it is found. A little lady says she brews a cup of tea so she can concentrate better. See how you will compete. Relax now, for there really are sixteen books of the Bible in this paragraph.
'''

books = ['genesis',
'exodus',
'leviticus',
'numbers',
'deuteronomy',
'joshua',
'judges',
'ruth',
'samuel',
'kings',
'chronicles',
'ezra',
'nehemiah',
'esther',
'job',
'psalms',
'proverbs',
'ecclesiastes',
'song of solomon',
'isaiah',
'jeremiah',
'lamentations',
'ezekiel',
'daniel',
'hosea',
'joel',
'amos',
'obadiah',
'jonah',
'micah',
'nahum',
'habakkuk',
'zephaniah',
'haggai',
'zechariah',
'malachi',
'matthew',
'mark',
'luke',
'john',
'acts',
'romans',
'corinthians',
'galatians',
'ephesians',
'philippians',
'colossians',
'thessalonians',
'timothy',
'titus',
'philemon',
'hebrews',
'james',
'peter',
'jude',
'revelation']

new_text = text.replace(" ","").replace("'","").replace(".","").replace(",","").lower()

books_found = []

for i in books:
    var = ''
    if i in new_text:
        if len(str(new_text.index(i))) == 2:
            var = '0'+ str(new_text.index(i))
        else: var = str(new_text.index(i))

        books_found.append(f'{var}: {i}')


books_found.sort()


printbook = [books_found[i][4:] for i in range(len(books_found))]

for i in range(len(printbook)):
    print(f'{i+1} {printbook[i]}')
