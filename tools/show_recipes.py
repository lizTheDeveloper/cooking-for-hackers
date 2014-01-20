import os
import json

for recipe in os.listdir("../recipes"):
    f = open("../recipes/%s" % recipe)
    full_text = f.readlines()
    status = ""
    front_matter = ""
    directions = ""
    for line in full_text:
        if line[0] == "{":
            status = "start"
            front_matter = "{"
        if line[0] == "}":
            status = "end"
            front_matter += line
        if status == "start":
            front_matter += line
        if status == "end":
            directions += line
    print front_matter
    ##front_matter = json.loads(front_matter)
    ##print front_matter["title"]