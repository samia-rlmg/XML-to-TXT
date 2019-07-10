# Python script to convert XML caption file to plaintext file
# Syntax: python xml_to_txt.py /path/to/myFile.xml > caption.txt

import sys
import xml.etree.ElementTree as ET

# If the user has specified a file, continue.
if len(sys.argv) > 1:
    xmlFile = sys.argv[1]

    f = open(xmlFile, "r")

    tree = ET.parse(f)

    # Isolate each track
    root = tree.getroot()
    media = root[0][4]
    video = media[0]
    tracks = video.findall("track")

    # Find each track of type "GraphicAndType" (meaning it contains a caption)
    for track in tracks:
        try:
            clipitems = track.findall("clipitem")
            for clipitem in clipitems:
                filters = clipitem.findall("filter")
                for filter in filters:
                    if filter[0].tag == "effect":
                        effect = filter[0]
                        if effect[1].text == "GraphicAndType":
                            try:     # If the caption is not empty, print its content
                                if len(effect[0].text) > 1: # Filter out empty captions
                                    print(effect[0].text)
                            except:
                                continue
        except:
            print("No text in track")

# If the user has not specified a file, prompt them to use the correct syntax
else:
    print("You must specify a filename\nSyntax: python xml_to_txt.py /path/to/myFile.xml")
