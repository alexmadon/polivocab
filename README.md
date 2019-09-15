# source

we maintain the TXT files: 

```
verbes.txt
```


# TXT to XML

we use:

```
./genxml.py
```


# add google speech

```
./xml2speech.py verbes.xml
```

that creates mp3 files in directory gspeech

# finally we generate the HTML5 from the XML

```
xsltproc style.xsl verbes.xml > verbes.html
```
