myWordListPath = '/usr/share/dict/words'

with open(myWordListPath, encoding="utf-8") as myFile:
    # read as string and convert to list
    #myText = myFile.read()
    #print(type(myText))
    #print(len(myText))
    #myLines = myText.split('\n')
    
    # read as list
    myLines = myFile.readlines()
    
    print(len(myLines))
    shuffle(myLines)
    print(myLines[:10])
    #myText = ' '.join(myLines[:10])
    
    myString = FormattedString('', fontSize=50, lineHeight=50, font='Comic Sans MS')
    for myLine in myLines[:50]:
        myString.append( myLine.strip() + ' ' , fill=(random(), random(), random()), font=choice(installedFonts()) )
    
    myMargin = 50
    #rect(myMargin, myMargin, width()-myMargin*2, height()-myMargin*2)
    textBox(myString, (myMargin, myMargin, width()-myMargin*2, height()-myMargin*2))
    