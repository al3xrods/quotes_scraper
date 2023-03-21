
# CHECKING LANGUAGUE OF TEXT.
from langdetect import detect 

english = []
with open("a.txt", 'w', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        try:
            if detect(line) =='en':
                f.write(line)
            else:
                continue
        except:
            continue

# =============================================================================================================================================
# FINDING NOT WANTED WORDS => REMOVING LINE.

bad_words = ['bad', 'naughty']
with open('b.txt', 'r', encoding="utf-8") as oldfile, open('a.txt', 'a', encoding="utf-8") as newfile:
    for line in oldfile:
        if not any('Holiday' in line for bad_word in bad_words):
            newfile.write(line)

#=============================================================================================================================================

#REMOVING LINES LESS THAT 180 CHARACHTERS.
with open('a.txt', 'r', encoding="utf-8") as f:
    for line in oldfile.readlines():
        text = line.split('―')[0]
        if len(text) < 180:
            f.write(line)
