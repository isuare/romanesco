import xml.etree.ElementTree as ET
import sys
import re
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


def xmltotxt(file, wfile):
    tree = ET.parse(file)
    root = tree.getroot()
    with open(wfile, 'a') as txt:
        for pmid in root.iter('rohtext'):
            txt.write(pmid.text)

def preprocessing(wfile, endfile):
    with open(endfile, 'a') as e:
        for line in wfile:
            sent = sent_tokenize(line)
            for s in sent:
                words = word_tokenize(s)
                w = ' '.join([str(v) for v in words])
                e.write(w + "\n")





def main():
    file = sys.argv[1]
    wfile = file.split(".")[0] + ".txt"
    endfile = wfile.split("-")[0] + ".txt"
    with open(file, 'r') as text:
        xmltotxt(text, wfile)

    with open(wfile, 'r') as text:
        preprocessing(text, endfile)


if __name__ == '__main__':
    main()
