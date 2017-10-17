#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
import requests
import re
import pyquery
import urllib
import praw
import random
import pudb

PyQuery = pyquery.PyQuery

listOfChampions = []
listOfAbilities = []
listOfLore = []
listOfSkinsv1 = []
listOfSkins = []
listOfItems = []
TaricQuotes = []

p2 = PyQuery("http://leagueoflegends.wikia.com/wiki/Champion")

for i in p2.items("li[style='display:inline-block;width:10em;'] > div[class='character_icon']"):
    print(i.attr("data-character"))
    listOfChampions.append(i.attr("data-character").strip())

#pu.db

for x in listOfChampions:
        try:
            tempAbilityArray = []
            tempInnate = []
            tempQ = []
            tempW = []
            tempE = []
            tempR = []

            ptemp = PyQuery("http://leagueoflegends.wikia.com/" + x +
                            "/Abilities")

            if not (ptemp("div[class='skill skill_in" \
                        "nate'] > div > div:first-child").attr("id")):
                tempInnate.append(ptemp("div[class='skill skill_in" \
                                    "nate'] > div > div:first-child" \
                                    "> table:nth-child(2) > tr:first-child" \
                                    "> td:first-child > div > img").attr("" \
                                    "alt").replace(".27", "'").replace(".21", "!").strip())
            else:
                tempInnate.append(ptemp("div[class='skill skill_in" \
                                        "nate'] > div > div:first-child"
                                        ).attr("id" \
                                        ).replace("_", " ") \
                                    .replace(".27", "'").replace(".21", "!").strip())
            tempInnate.append(ptemp("div[class='skill skill_in" \
                                              "nate']").text().strip())
            tempAbilityArray.append(tempInnate)
            tempQ.append(ptemp("div[class='skill skill_q" \
                               "'] > div > div:first-child").attr("id" \
                                ).replace("_", " ") \
                         .replace(".27", "'").replace(".21", "!").strip())
            tempQ.append(ptemp("div[class='skill skill_q" \
                                              "']").text().strip())
            tempAbilityArray.append(tempQ)
            tempW.append(ptemp("div[class='skill skill_w" \
                               "'] > div > div:first-child").attr("id" \
                                ).replace("_", " ") \
                         .replace(".27", "'").replace(".21", "!").strip())
            tempW.append(ptemp("div[class='skill skill_w" \
                                              "']").text().strip())
            tempAbilityArray.append(tempW)
            tempE.append(ptemp("div[class='skill skill_e" \
                               "'] > div > div:first-child").attr("id" \
                                ).replace("_", " ") \
                         .replace(".27", "'").replace(".21", "!").strip())
            tempE.append(ptemp("div[class='skill skill_e" \
                                              "']").text().strip())
            tempAbilityArray.append(tempE)
            tempR.append(ptemp("div[class='skill skill_r" \
                               "'] > div > div:first-child").attr("id" \
                                ).replace("_", " ") \
                         .replace(".27", "'").replace(".21", "!").strip())
            tempR.append(ptemp("div[class='skill skill_r" \
                                              "']").text().strip())
            tempAbilityArray.append(tempR)
            listOfAbilities.append(tempAbilityArray)
            for i in listOfAbilities[len(listOfAbilities)-1]:
                    print(i[0])
                    print(i[1])
        except urllib.error.HTTPError:
            tempAbilityArray = []
            tempInnate = []
            tempQ = []
            tempW = []
            tempE = []
            tempR = []

            ptemp = PyQuery("http://leagueoflegends.wikia.com/" + x)

            if not (ptemp("div[class='skill skill_in" \
                        "nate'] > div > div:first-child").attr("id")):
                tempInnate.append(ptemp("div[class='skill skill_in" \
                                    "nate'] > div > div:first-child" \
                                    "> table:nth-child(2) > tr:first-child" \
                                    "> td:first-child > div > img").attr("" \
                                    "alt").replace(".27", "'").replace(".21", "!").strip())
            else:
                tempInnate.append(ptemp("div[class='skill skill_in" \
                                        "nate'] > div > div:first-child" \
                                        ).attr("id" \
                                        ).replace("_", " ") \
                                  .replace(".27", "'").replace(".21", "!").strip())
            tempInnate.append(ptemp("div[class='skill skill_in" \
                                              "nate']").text().strip())
            tempAbilityArray.append(tempInnate)
            tempQ.append(ptemp("div[class='skill skill_q" \
                               "'] > div > div:first-child").attr("id" \
                                ).replace("_", " ") \
                         .replace(".27", "'").replace(".21", "!").strip())
            tempQ.append(ptemp("div[class='skill skill_q" \
                                              "']").text().strip())
            tempAbilityArray.append(tempQ)
            tempW.append(ptemp("div[class='skill skill_w" \
                               "'] > div > div:first-child").attr("id" \
                                ).replace("_", " ") \
                         .replace(".27", "'").replace(".21", "!").strip())
            tempW.append(ptemp("div[class='skill skill_w" \
                                              "']").text().strip())
            tempAbilityArray.append(tempW)
            tempE.append(ptemp("div[class='skill skill_e" \
                               "'] > div > div:first-child").attr("id" \
                                ).replace("_", " ") \
                         .replace(".27", "'").replace(".21", "!").strip())
            tempE.append(ptemp("div[class='skill skill_e" \
                                              "']").text().strip())
            tempAbilityArray.append(tempE)
            tempR.append(ptemp("div[class='skill skill_r" \
                               "'] > div > div:first-child").attr("id" \
                                ).replace("_", " ") \
                         .replace(".27", "'").replace(".21", "!").strip())
            tempR.append(ptemp("div[class='skill skill_r" \
                                              "']").text().strip())
            tempAbilityArray.append(tempR)
            listOfAbilities.append(tempAbilityArray)
            for i in listOfAbilities[len(listOfAbilities)-1]:
                    print(i[0])
                    print(i[1])
for x in listOfChampions:
        ptemp = PyQuery("http://leagueoflegends.wikia.com/wiki/" \
                        + x + "/Background")
        listOfLore.append(ptemp("center").text() + "\n" \
                          + "\n" + ptemp("center + p").text())
        print(listOfLore[len(listOfLore)-1])
for x in listOfChampions:
        ptemp = PyQuery("http://leagueoflegends.wikia.com/wiki/" \
                        + x + "/Skins")
        tempSkinsArray = []
        for j in ptemp.items("div[class='wikia-gallery-item']"):
            shottest = j("div[class='wikia-gallery-item'] > div >" \
                         " div[class='gallery-image-wrapper accent']" \
                         ).attr("id")
            if "Screenshot" not in shottest and shottest != "Jpg" and \
               "_-" not in shottest:
                SkinArrayx2 = []
                skinStr = j("div[class='wikia-gallery-item'] > "
                            "div[class='lightbox-caption']").text()

                SkinArrayx2.append(skinStr)
                newurl = "http://leagueoflegends.wikia.com"
                newurl += j("div[class='wikia-gallery-item'] > div >" \
                            " div[class='gallery-image-wrapper accent']" \
                            " > a").attr("href")
                ptemp2 = PyQuery(newurl)
                skinlink = ptemp2("div[class='fullImageLink'] > a").attr("h" \
                                                                         "ref")
                SkinArrayx2.append(skinlink)
                for i in SkinArrayx2:
                    print(i)
                tempSkinsArray.append(SkinArrayx2)
        listOfSkinsv1.append(tempSkinsArray)
regex1 = re.compile(r"(\w+?\.?\s,?)+?(?=\d{3,4}\s)")
regex2 = re.compile(r"\d{3,4}")
regex3 = re.compile(r"\d{2}-\w{3,4}-\d{4}")
for x in listOfChampions:
    regex4 = re.compile(r".+?"+x)
    regex5 = re.compile(r"" + x + r"\s(.+?)\s/")
    regex6 = re.compile(r"Classic "+x)
    tempSkinsArray = []
    j = listOfSkinsv1[listOfChampions.index(x)]
    for i in j:
        try:
            temptempSkinsArray = []
            strToParse = i[0]
            print(strToParse)
            if strToParse.find("Urf the Manatee") == -1:
                if regex1.search(strToParse):
                    temptempSkinsArray.append(regex1.search(strToParse).group(0))
                    temptempSkinsArray.append(regex2.search(strToParse).group(0))
                    if not regex3.search(strToParse):
                        temptempSkinsArray.append("Upcoming skin")
                    else:
                        temptempSkinsArray.append(regex3.search(strToParse).group(0))
                    temptempSkinsArray.append(i[1])
                elif regex6.search(strToParse):
                    temptempSkinsArray.append(regex6.search(strToParse).group(0))
                    temptempSkinsArray.append("Free")
                    temptempSkinsArray.append(regex3.search(strToParse).group(0))
                    temptempSkinsArray.append(i[1])
                else:
                    temptempSkinsArray.append(regex4.search(strToParse).group(0))
                    temptempSkinsArray.append(regex5.search(strToParse).group(1) \
                                              .rstrip())
                    if not regex3.search(strToParse):
                        temptempSkinsArray.append("Upcoming skin")
                    else:
                        temptempSkinsArray.append(regex3.search(strToParse).group(0))
                    temptempSkinsArray.append(i[1])
            else:
                regex7 = re.compile(r"Urf the Manatee")
                regex8 = re.compile(r"Urf the Manatee(.+?)/")
                temptempSkinsArray.append(regex7.search(strToParse).group(0))
                temptempSkinsArray.append(regex8.search(strToParse).group(1) \
                                          .rstrip())
                temptempSkinsArray.append(regex3.search(strToParse).group(0))
                temptempSkinsArray.append(i[1])
            tempSkinsArray.append(temptempSkinsArray)
        except:
            pass
    listOfSkins.append(tempSkinsArray)
p3 = PyQuery("http://leagueoflegends.wikia.com/wiki/Item")

for x in p3.items("div[id='container'] td > span > div > div > a"):
    tempItems = []
    tempItems.append(x.attr("title"))
    print(tempItems[0])
    tempItems.append("http://leagueoflegends.wikia.com" + x.attr("href"))
    print(tempItems[1])
    ptemp = PyQuery("http://leagueoflegends.wikia.com" + x.attr("href"))
    descStr = ""
    for i in ptemp.items("div[class*='pi-item pi-data']"):
        descStr += i.text()
        descStr += "\n"
    tempItems.append(descStr)
    print(tempItems[2])
    listOfItems.append(tempItems)

p4 = PyQuery("http://leagueoflegends.wikia.com/wiki/Taric/Quotes")

for x in p4.items("li"):
    if x.children("span a img[alt*='taunt']"):
        pass
    elif x.children("span a img[alt*='laugh']"):
        pass
    elif x.children("span a img[alt*='item']"):
        pass
    elif x.children("i"):
        print(x.text())
        if("Malphite" not in x.text()):
            TaricQuotes.append(x.text())
    else:
        pass

testStr1 = "Gnar/Skins"
testStr2 = "Jayce/Lore"
testStr3 = "Bastion"
testStr4 = "PAX Jax"
testStr5 = "Classic Akali"
testStr6 = "Urf the Manatee"
testStr7 = "Zhonya's Ring"
testStr8 = "Winter's Bite"
testStr9 = "Pool Party Fiora"
testStr10 = "GNAR!"
testStrings = [testStr1, testStr2, testStr3, testStr4, testStr5,
               testStr6, testStr7, testStr8, testStr9]
moreResults = []

def giveResults(i):
    index=0
    testResults = []
    i2 = i
    for x in listOfChampions:
        index = listOfChampions.index(x)
        if i2.startswith(x):
            if i2 == x:
                tempResults = []
                tempResults.append(False)
                tempResults.append(x)
                tempResults.append(listOfLore[index])
                tempResults.append(listOfAbilities[index])
                tempResults.append(listOfSkins[index])
                testResults.append(tempResults)
                return testResults
            elif i2 == (x + "/Lore"):
                testResults.append("Lore")
                testResults.append(listOfLore[index])
                return testResults
            elif i2 == (x + "/Skins"):
                testResults.append("Skins")
                testResults.append(listOfSkins[index])
                return testResults
            elif i2 == (x + "/Abilities"):
                testResults.append("Abilities")
                testResults.append(listOfAbilities[index])
                return testResults
            else:
                 for j in listOfSkins[index]:
                    if i2 == j[0]:
                        testResults.append("Skin")
                        testResults.append(j)
                        return testResults
        elif i2.find(x) != -1:
            for j in listOfSkins[index]:
                 if i2 == j[0]:
                    testResults.append("Skin")
                    testResults.append(j)
                    return testResults
        elif i2 == "Mundo" and x == "Dr. Mundo":
            if i2.startswith("Mundo"):
                if i2 == "Mundo":
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == ("Mundo/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == ("Mundo/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == ("Mundo/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2 == "Yi" and x == "Master Yi":
            if i2.startswith("Yi"):
                if i2 == "Yi":
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == ("Yi/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == ("Yi/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == ("Yi/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Xin") != -1 and x == "Xin Zhao":
            if i2.startswith("Xin"):
                if i2 == "Xin":
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == ("Xin/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == ("Xin/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == ("Xin/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("MF") != -1 and x == "Miss Fortune":
            if i2.startswith("MF"):
                if i2 == "MF":
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == ("MF/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == ("MF/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == ("MF/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("J4") != -1 and x == "Jarvan IV":
            if i2.startswith("J4"):
                if i2 == "Mundo":
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == ("J4/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == ("J4/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == ("J4/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Sol") != -1 and x == "Aurelion Sol":
            if i2.startswith("Sol"):
                if i2 == "Sol":
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == ("Sol/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == ("Sol/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == ("Sol/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Dickshoe McGee") != -1 and x == "Shaco":
            a = "Dickshoe McGee"
            index = listOfChampions.index("Shaco")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Satan") != -1 and x == "Teemo":
            a = "Satan"
            index = listOfChampions.index("Teemo")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Blitz") != -1 and x == "Blitzcrank":
            a = "Blitz"
            index = listOfChampions.index("Blitzcrank")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Cait") != -1 and x == "Caitlyn":
            a = "Cait"
            index = listOfChampions.index("Caitlyn")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Cass") != -1 and x == "Cassiopeia":
            a = "Cass"
            index = listOfChampions.index("Cassiopeia")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Cho") != -1 and x == "Cho'Gath":
            a = "Cho"
            index = listOfChampions.index("Cho'Gath")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Eve") != -1 and x == "Evelynn":
            a = "Eve"
            index = listOfChampions.index("Evelynn")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Ez") != -1 and x == "Ezreal":
            a = "Ez"
            index = listOfChampions.index("Ezreal")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("GP") != -1 and x == "Gangplank":
            a = "GP"
            index = listOfChampions.index("Gangplank")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Kass") != -1 and x == "Kassadin":
            a = "Kass"
            index = listOfChampions.index("Kassadin")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Kat") != -1 and x == "Katarina":
            a = "Kat"
            index = listOfChampions.index("Katarina")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Kha") != -1 and x == "Kha'Zix":
            a = "Kha"
            index = listOfChampions.index("Kha'Zix")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Kog") != -1 and x == "Kog'Maw":
            a = "Kog"
            index = listOfChampions.index("Kog'Maw")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("LB") != -1 and x == "LeBlanc":
            a = "LB"
            index = listOfChampions.index("LeBlanc")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Lee") != -1 and x == "Lee Sin":
            a = "Lee"
            index = listOfChampions.index("Lee Sin")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Liss") != -1 and x == "Lissandra":
            a = "Liss"
            index = listOfChampions.index("Lissandra")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Malph") != -1 and x == "Malphite":
            a = "Malph"
            index = listOfChampions.index("Malphite")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Malz") != -1 and x == "Malzhar":
            a = "Malz"
            index = listOfChampions.index("Malzahar")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Mao") != -1 and x == "Maokai":
            a = "Mao"
            index = listOfChampions.index("Maokai")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Morde") != -1 and x == "Mordekaiser":
            a = "Morde"
            index = listOfChampions.index("Mordekaiser")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Morg") != -1 and x == "Morgana":
            a = "Morg"
            index = listOfChampions.index("Morgana")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Susan") != -1 and x == "Nasus":
            a = "Susan"
            index = listOfChampions.index("Nasus")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Naut") != -1 and x == "Nautilus":
            a = "Naut"
            index = listOfChampions.index("Nautilus")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Nid") != -1 and x == "Nidalee":
            a = "Nid"
            index = listOfChampions.index("Nidalee")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Noc") != -1 and x == "Nocturne":
            a = "Noc"
            index = listOfChampions.index("Nocturne")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Ori") != -1 and x == "Orianna":
            a = "Ori"
            index = listOfChampions.index("Orianna")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Panth") != -1 and x == "Pantheon":
            a = "Panth"
            index = listOfChampions.index("Pantheon")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Poopy") != -1 and x == "Poppy":
            a = "Poopy"
            index = listOfChampions.index("Poppy")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Sej") != -1 and x == "Sejuani":
            a = "Sej"
            index = listOfChampions.index("Sejuani")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Shyv") != -1 and x == "Shyvana":
            a = "Shyv"
            index = listOfChampions.index("Shyvana")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Trist") != -1 and x == "Tristana":
            a = "Trist"
            index = listOfChampions.index("Tristana")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Trynd") != -1 and x == "Tryndamere":
            a = "Trynd"
            index = listOfChampions.index("Tryndamere")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("TF") != -1 and x == "Twisted Fate":
            a = "TF"
            index = listOfChampions.index("Twisted Fate")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("ManBearPig") != -1 and x == "Udyr":
            a = "ManBearPig"
            index = listOfChampions.index("Udyr")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Veig") != -1 and x == "Veigar":
            a = "Veig"
            index = listOfChampions.index("Veigar")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Vel") != -1 and x == "Vel'Koz":
            a = "Vel"
            index = listOfChampions.index("Vel'Koz")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Vik") != -1 and x == "Viktor":
            a = "Vik"
            index = listOfChampions.index("Viktor")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Vlad") != -1 and x == "Vladimir":
            a = "Vlad"
            index = listOfChampions.index("Vladimir")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Voli") != -1 and x == "Volibear":
            a = "Voli"
            index = listOfChampions.index("Volibear")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("WW") != -1 and x == "Warwick":
            a = "WW"
            index = listOfChampions.index("Warwick")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Wu") != -1 and x == "Wukong":
            a = "Wu"
            index = listOfChampions.index("Wukong")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Yas") != -1 and x == "Yasuo":
            a = "Yas"
            index = listOfChampions.index("Yasuo")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Zil") != -1 and x == "Zilean":
            a = "Zil"
            index = listOfChampions.index("Zilean")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        elif i2.find("Weedwick") != -1 and x == "Warwick":
            a = "Weedwick"
            index = listOfChampions.index("Warwick")
            if i2.startswith(a):
                if i2 == a:
                    tempResults = []
                    tempResults.append(False)
                    tempResults.append(x)
                    tempResults.append(listOfLore[index])
                    tempResults.append(listOfAbilities[index])
                    tempResults.append(listOfSkins[index])
                    testResults.append(tempResults)
                    return testResults
                elif i2 == (a+"/Lore"):
                    testResults.append("Lore")
                    testResults.append(listOfLore[index])
                    return testResults
                elif i2 == (a+"/Skins"):
                    testResults.append("Skins")
                    testResults.append(listOfSkins[index])
                    return testResults
                elif i2 == (a+"/Abilities"):
                    testResults.append("Abilities")
                    testResults.append(listOfAbilities[index])
                    return testResults
                else:
                    pass
        else:
            pass
        for x in listOfAbilities:
            for j in x:
                if i2 == j[0]:
                    testResults.append("Ability")
                    testResults.append(j)
                    return testResults
        for x in listOfItems:
            if i2 == x[0]:
                testResults.append("Item")
                testResults.append(x)
                return testResults
            return testResults
    return []

for x in testStrings:
    moreResults.append(giveResults(x))

for i in moreResults:
    if type(i) == list:
        for j in i:
            if type(j) == list:
                for k in j:
                    print(k)
            else:
                print(j)
    else:
        print(i)
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
                basis = giveResults(matches[i])
                if basis != []:
                    if "Taric" in matches[i]:
                        finalstr += "Hey! It's me!  \n"
                    if type(basis[0]) == list:
                        if basis[0][0] == False:
                            finalstr += (basis[0][1] + ":  \n")
                            finalstr += ((basis[0][2]) + "  \n")
                            for index, j in enumerate(basis[0][3]):
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
                            for j in basis[0][4]:
                                finalstr += (j[0] + "  \n")
                    elif basis[0] == "Lore":
                        finalstr += basis[1]
                    elif basis[0] == "Skins":
                        for j in basis[1]:
                            finalstr += (j[0] + "  \n")
                    elif basis[0] == "Abilities":
                        for index, j in basis[1]:
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
                        finalstr += ("["+basis[1][0]+"]("+basis[1][3]+")" \
                                "  \n")
                        finalstr += ("Cost: " + basis[1][1] + "  \n")
                        finalstr += ("Date Released:  " + "\n")
                    elif basis[0] == "Ability":
                        finalstr += (basis[1][0] + ": " + basis[1][1] + "" \
                                    "  \n")
                    else:
                        pass
                finalstr += "*****  \n"
            finalstr += "######I'm a bot-in-training! If you have questions or bugs," \
                        " [PM](https://www.reddit.com/message/compose/?to=Tarics" \
                        "KnowledgeBot) me  \n  \n"
            quote = TaricQuotes[random.randint(0, len(TaricQuotes)-1)]
            finalstr += ("_"+quote+"_")
            comment.reply(finalstr)
