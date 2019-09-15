#!/usr/bin/python3
import time
import re
import argparse
import hashlib
from google_speech import Speech # https://github.com/desbma/GoogleSpeech

# text = "Hello World"
# lang = "en"
# speech = Speech(text, lang)
# speech.play()


import xml.etree.ElementTree as ET

def get_google_speech(opts):
    
    tree = ET.parse(opts.xmlfile)
    root = tree.getroot()
    
    els=root.findall(".//pl")
    
    # print(els)
    
    pattern=re.compile("\((N ?)?[\d]\)")
    elnb=1
    for el in els:
        text=el.text
        lang = "pl"
        ahash = hashlib.md5(text.encode("utf-8")).hexdigest()
        filename="gspeech/"+ahash+".mp3"
        print("filename",filename)
    
        speech = Speech(text, lang)
        speech.save(filename)
        time.sleep(0.5)
        
        elnb=elnb+1
        
        # 2024

def parse_cli():
    xx="parse_cli"
    parser = argparse.ArgumentParser(description="""Call google speech
example:
./xml2speech.py
./xml2speech.py 2024
""",formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('xmlfile',help="the xml file to generate speech for")
    opts = parser.parse_args()
    # debug(xx,"opts:",opts)
    return opts

if __name__ == "__main__":
    opts=parse_cli()
    get_google_speech(opts)
