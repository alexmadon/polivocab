#!/usr/bin/python3
import re
import hashlib



def clean(line):
    line=re.sub("^[><] *","",line)
    return line

def gethash(text):
    ahash = hashlib.md5(text.encode("utf-8")).hexdigest()
    return ahash

def genxml(filename):
    import polishipa
    (rerules,rules_with_symbols,g2p_dict,regex)=polishipa.setup()

    f=open(filename)
    lines=f.readlines()
    f.close()

    out=[]
    
    out.append("<doc>")
    for line in lines:
        line=line.strip()
        if line.startswith(">"):
            line=clean(line)
            out.append('<pl hash="'+gethash(line)+'">'+line+'</pl>')
            ipa_line=polishipa.convert(line,rerules,rules_with_symbols,g2p_dict,regex)
            out.append("<ip>"+ipa_line+"</ip>")
        elif line.startswith('<'):
            line=clean(line)
            out.append("<fr>"+line+"</fr>")
        elif line.startswith('# '):
            line=clean(line)
            out.append("<h1>"+line+"</h1>")

    out.append("</doc>")


    saveto=filename.replace(".txt",".xml")
    print("saving to",saveto)
    f=open(saveto,"w")
    f.write('\n'.join(out))
    f.close()
    


filenames=["verbes.txt"]
for filename in filenames:
    genxml(filename)
