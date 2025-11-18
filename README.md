# AI-debator

## A functional AI debator where you can set personalities to fight it out against a debate topic?
Have you ever felt so lost in ChatGPT's reponses? Need a second opinion. Well heres my semi-useful, super useless product that does nothing other than give you suggestions that probably suck. You can now ask anyone, yes anyone, even that rural country farmer down in southern USA to debate about anything - literally anything from "Is the moon fake?" to "Where should I go this week end in New York?" the choice is really yours.
**Please note that the choice's the AI makes is not what I condone, take action with the idea that its the AI choice and you should be weary.**
* Allows user's to set two AI personalities to debate
* Uses AI to check who won the debate
* Pretty useless 🤡
  
## DENO
When running this program it will use OLLAMA to generate text which will then be read out by COQUI and SOUNDDEVICE, this will then go back and fourth with each debator until the end (default is 10) Sometimes the AI does get very heated so thats pretty fun, just tamper with the program a bit.

## Project is made with love using [COQUI TTS 🐸](https://github.com/coqui-ai/TTS) and [OLLAMA 🦙](https://ollama.com)
To use this project pick an IDE and make sure you have the following libraries on your python virutal enviroment, COQUI TTS, OLLAMA, SOUNDDEVICE.
**Note you should do this in a seperate folder**
1. Use an IDE, perferrably VS-CODE since thats what I used to code this.
2. Download the python file from this project.
3. Set up your python virutal enviroment (refer to google if you don't know), use **python 3.11.0** .
4. Download the following libraries: [COQUI TTS](https://github.com/coqui-ai/TTS), [OLLAMA](https://ollama.com) **note that the websites will have installation instructions**, and SoundDevice.
5. Make sure you have OLLAMA installed on your system with a specific model you want to use.
6. Replace the AImodel variable with the one you have in your system.
7. Make sure to set up a file to store the chat history and make the right file-path to it at the first variable in the code "historyFile" **note the default will be history.txt**.
8. Set up debator voices, you can do this by just fetching the voices avaliable (you can do this manually or just use the numbers 225-376).
9. Set up your debator 1 and 2 which are the context to what each debator is ie: country farmer, city boy, police officer, ect.
10. Set up debateLengthMax which is the max amount both of them will talk in total.
11. Enjoy and listen to AI argue.

## If you want to contribute
If for some reason you want to contribute or do something with the python files go ahead with my spagette code, I probably wont be reading anything from this repo for a while due to school, nor will I do updates.
