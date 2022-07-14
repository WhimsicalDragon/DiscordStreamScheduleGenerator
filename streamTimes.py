import datetime
import math
import io
import json

INPUTFILE = "schedule.json"
MINPADDINGLENGTH = 5
PADDINGCHAR = '-'


streamTime = datetime.datetime(2022,7,14,hour=1,minute=30)

def convertToEpoch(streamTime):

    return math.trunc(streamTime.timestamp())

def loadJson(INPUTFILE):
    input = io.open(INPUTFILE,"r")
    data = json.loads(input.read())

    return data

def writeSchedule(data,MINPADDINGLENGTH,PADDINGCHAR):
    streamCount = data["StreamCount"]

    times = []
    titles = []
    schedule = ""
    longestTitleLen = 0

    for i in range(streamCount):
        times.append(
            convertToEpoch(
                datetime.datetime(
                    data["Streams"][i]["year"],
                    data["Streams"][i]["month"],
                    data["Streams"][i]["day"],
                    hour=data["Streams"][i]["hour"],
                    minute=data["Streams"][i]["minute"])
                )
            )

        titles.append(data["Streams"][i]["title"])

        if len(titles[i]) > longestTitleLen:
            longestTitleLen = len(titles[i])

    for i in range(streamCount):

        schedule += (titles[i] + " ").ljust(longestTitleLen+1+MINPADDINGLENGTH,PADDINGCHAR) + " <t:" + str(times[i]) + ">"

        if i != streamCount-1:
            schedule += "\n"

    print(schedule)


data = loadJson(INPUTFILE)

writeSchedule(data,MINPADDINGLENGTH,PADDINGCHAR)
