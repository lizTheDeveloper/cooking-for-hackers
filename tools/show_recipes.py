import os
import json

recipes_by_title = {}
recipes_by_index = {}
counter = 0
for recipe in os.listdir("../recipes"):
    f = open("../recipes/%s" % recipe)
    full_text = f.readlines()
    status = ""
    front_matter = ""
    directions = ""
    for line in full_text:
        if line[0] == "{":
            status = "start"
            front_matter = ""
        if line[0] == "}":
            status = "end"
            front_matter += line
        if status == "start":
            front_matter += line
        if status == "end":
            directions += line
    front_matter = json.loads(front_matter)
    front_matter["directions"] = directions
    recipes_by_title[front_matter["title"]] = front_matter
    recipes_by_index[counter] = front_matter["title"]
    counter +=1

print "Hello! Here's the recipe index"
for _id in recipes_by_index.keys():
    print "%d) %s" % (_id, recipes_by_index[_id])

print "Type the number of the recipe or 'quit' to quit"

while user_input != "quit":
    user_input = raw_input("> ")

    if user_input.isnumeric():

        


def getRecipeById(_id):
    return recipes_by_title[recipes_by_index[_id]]

def printFormattedRecipe(_id):
    ##Recipe is formatted as a dictionary
    print "Title: %s" 
    print "Serves %s" 