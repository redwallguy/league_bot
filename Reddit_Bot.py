#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
import requests
import re
import pyquery
import urllib
import praw
import random
import pudb
import sys

PyQuery = pyquery.PyQuery

listOfChampions = []
listOfAbilities = []
listOfLore = []
listOfSkins = []
listOfItems = []
TaricQuotes = []

with open("championList.txt") as f:
    listOfChampions = re.split("#####",f.read()) #Creates champion list from file
    listOfChampions.remove('')

with open("abilities.txt") as f:
    layer1Abilities = re.split("xxDELIM3xx",f.read())
    layer1Abilities.remove('')
    for champ in layer1Abilities:
        temp1 = []
        layer2Abilities = re.split("xxDELIM2xx",champ)
        layer2Abilities.remove('')
        for abil in layer2Abilities:
            layer3Abilities = re.split("xxDELIM1xx", abil)
            temp1.append(layer3Abilities)
        listOfAbilities.append(temp1)

with open("Skinlist.txt") as f:
    layer1Skins = re.split("xxDELIM3xx",f.read())
    layer1Skins.remove('')
    for champ in layer1Skins:
        temp1 = []
        layer2Skins = re.split("xxDELIM2xx",champ)
        layer2Skins.remove('')
        for skin in layer2Skins:
            layer3Skins = re.split("xxDELIM1xx", skin)
            layer3Skins.remove('')
            temp1.append(layer3Skins)
        listOfSkins.append(temp1)

with open("Itemlist.txt") as f:
    layer1Items = re.split("xxDELIM2xx",f.read())
    layer1Items.remove('')
    for item in layer1Items:
        temp1 = re.split("xxDELIM1xx",item)
        listOfItems.append(temp1)

with open("Taricquotes.txt") as f:
    TaricQuotes = re.split("#####",f.read())
    TaricQuotes.remove('')

with open("ChampAliases.txt") as f:
    aliases = {}
    layer1Nicks = re.split("#####",f.read())
    layer1Nicks.remove('')
    for champ in layer1Nicks:
        temp2 = re.split("=",champ)
        chName = temp2[0]
        nicks = re.split("\|",temp2[1])
        aliases[chName] = nicks

with open("Lore.txt") as f:
    listOfLore = re.split("#####",f.read())
    listOfLore.remove('')

testStr1 = "Gnar/Skins"
testStr2 = "Jayce/Lore"
testStr3 = "Bastion"
testStr4 = "PAX Jax"
testStr5 = "Classic Akali"
testStr6 = "Urf the Manatee"
testStr7 = "Zhonya's Ring"
testStr8 = "Winter's Bite"
testStr9 = "waiFu"
testStr10 = "GNAR!"
testStr11 = "Xayah"
testStrings = [testStr1, testStr2, testStr3, testStr4, testStr5,
               testStr6, testStr7, testStr8, testStr9, testStr10, testStr11]

def giveResults(i):
    testResults = []
    print(i)
    for champ in listOfChampions:
        index = listOfChampions.index(champ)
        if i.strip() == champ:
            testResults.append("Overview")
            testResults.append(champ)
            testResults.append(listOfLore[index])
            testResults.append(listOfAbilities[index])
            testResults.append(listOfSkins[index])
            print(testResults)
            return testResults
        if i.strip() == champ + "/Lore":
            testResults.append("Lore")
            testResults.append(listOfLore[index])
            print(testResults)
            return testResults
        if i.strip() == champ + "/Abilities":
            testResults.append("Abilities")
            testResults.append(listOfAbilities[index])
            print(testResults)
            return testResults
        if i.strip() == champ + "/Skins":
            testResults.append("Skins")
            testResults.append(listOfSkins[index])
            print(testResults)
            return testResults
        chAls = aliases[champ]
        for nick in chAls:
            if i.strip().lower() == nick.lower():
                testResults.append("Overview")
                testResults.append(champ)
                testResults.append(listOfLore[index])
                testResults.append(listOfAbilities[index])
                testResults.append(listOfSkins[index])
                print(testResults)
                return testResults
        for skin in listOfSkins[index]:
            if i.strip() == skin[0]:
                testResults.append("Skin")
                testResults.append(skin)
                print(testResults)
                return testResults
        for ability in listOfAbilities[index]:
            if i.strip() == ability[0]:
                testResults.append("Ability")
                testResults.append(ability)
                print(testResults)
                return testResults
    for item in listOfItems:
        if i.strip() == item[0]:
            testResults.append("Item")
            testResults.append(item)
            print(testResults)
            return testResults
    return testResults

for test in testStrings:
    giveResults(test)

reddit = praw.Reddit('bot', user_agent="Taric's Knowledge Bot by u/redwallguy")

subreddit = reddit.subreddit("postpreview")

redditregex = re.compile(r"\[\[(.+?)\]\]")

for comment in subreddit.stream.comments():
        body = comment.body
        matches = redditregex.findall(body)
        if matches != []:
            if len(matches) > 5:
                a = 5
            else:
                a = len(matches)
            finalstr = ""
            for i in range(a):
                noMatch = False
                basis = giveResults(matches[i])
                if basis != []:
                    if basis[1] == "Taric":
                        finalstr += "Hey, it's me!\n\n"
                    if basis[0] == "Overview":
                        finalstr += (basis[1] + ":  \n\n")
                        finalstr += (basis[2] + "  \n\n")
                        for index, j in enumerate(basis[3]):
                            if index == 0:
                                finalstr += ("Passive: " + j[0] + "" \
                                             "  \n")
                            elif index == 1:
                                finalstr += ("Q: " + j[0] + "  \n")
                            elif index == 2:
                                finalstr += ("W: " + j[0] + "  \n")
                            elif index == 3:
                                finalstr += ("E: " + j[0] + "  \n")
                            else:
                                finalstr += ("R: " + j[0] + "  \n")
                        finalstr += "\nSkins:\n"
                        for j in basis[4]:
                            finalstr += (j[0] + "  \n")
                    elif basis[0] == "Lore":
                        finalstr += basis[1] + "\n"
                    elif basis[0] == "Skins":
                        for j in basis[1]:
                            finalstr += (j[0] + "  \n")
                    elif basis[0] == "Abilities":
                        for index, j in enumerate(basis[1]):
                            if index == 0:
                                finalstr += ("Passive: " + j[0] + "  \n")
                            elif index == 1:
                                finalstr += ("Q: " + j[0] + "  \n")
                            elif index == 2:
                                finalstr += ("W: " + j[0] + "  \n")
                            elif index == 3:
                                finalstr += ("E: " + j[0] + "  \n")
                            else:
                                finalstr += ("R: " + j[0] + "  \n")
                    elif basis[0] == "Skin":
                        finalstr += ("["+basis[1][0]+"]("+basis[1][1]+")" \
                                "  \n")
                        finalstr += ("Cost: " + basis[1][2] + "  \n")
                        finalstr += ("Date Released:  " + basis[1][3] + "\n")
                    elif basis[0] == "Ability":
                        finalstr += (basis[1][0] + ": " + basis[1][1] + "" \
                                    "  \n")
                    elif basis[0] == "Item":
                        finalstr += (basis[1][0] + ":\n" + basis[1][1] + "\n")
                    else:
                        pass
                else:
                    noMatch = True
                print(noMatch)
                if not noMatch:
                    finalstr += "*****  \n"
            if finalstr not in "":
                finalstr += "######I'm a bot-in-training! If you have questions or bugs," \
                            " [PM](https://www.reddit.com/message/compose/?to=Tarics" \
                            "KnowledgeBot) me  \n  \n"
                quote = TaricQuotes[random.randint(0, len(TaricQuotes)-1)]
                finalstr += ("_"+quote+"_")
                print(finalstr)
                comment.reply(finalstr)
