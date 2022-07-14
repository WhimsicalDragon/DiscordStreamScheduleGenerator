# Discord Stream Schedule Maker

This is a simple python program to that generates a stream schedule message for discord.

---
## Author

WhimsicalDragon1337 [Twitter](https://twitter.com/Whimsical1337)
You could've watched me code this live at on [twitch](https://www.twitch.tv/whimsicaldragon1337) ~~if my internet had been working when I was coding this~~

---
## Usage

1. Set the input file (this is stored in the **INPUTFILE** variable), this should be a .json file. An example json file is provided. 
2. Set the "StreamCount" to the number of streams you will be including. Add that many elements to the "Streams" array. 
3. Fill in the "title", "year", "month", "day", "hour", and "minute" information for each stream. The program assumes that your timezone is the same for the streamtimes, if this is not the case please adjust for the correct timezone.
4. Place your completed json file in the same directory as the streamTimes.py program. 
5. Set the minimum padding between the stream title and the time (this is stored in the **MINIMUMPADDINGLENGTH** variable). 
6. Set the padding character, this is the character that will fill in the blank space between your title and the stream time (this is stored in the **PADDINGCHAR** variable). 
7. Set the outpute file which is where your message will be printed to (this is stored in the **OUTPUTFILE** variable). 
8. Run streamTimes.py with the python interperter. You can do this by typing **python streamTimes.py** or **python3 streamTimes.py** (This program was written for python 3 and may not work in python 2). 
9. You completed discord message will be printed to the command line as well as your file. You may then copy & paste the output file or the command line output and past it into discord.

Video documentation [here](https://youtu.be/_ZQeiRmHpyI)

---
## Support

I am a starving graduate student. Please give me money so I can keep coding dumb stuff. You can do that [here](https://ko-fi.com/whimsicaldragon1337)