# the ai part
from ollama import chat
from ollama import ChatResponse
import torch
from TTS.api import TTS

# key inputs and other librarys
import sounddevice as sd   

#setups
historyFile = "history.txt" # make sure this is the right file path
AImodel = 'gemma3:4b' # you should change this to the model you are using
#debate setups
debateTopic = '' # set this to the debate topic you want
debator1 = '' # set this to the debator you want
debator2 = '' # set this to the debator you want
debator1Voice = "p226" # set this to the voice you want
debator2Voice = "p248" # set this to the voice you want
debator = 1
debateLength = 0
debateLengthMax = 10 # this will make the debate longer or shorter
debateResponse = None

for i in range(debateLengthMax):
    #use this for premade ai voice
    tts = TTS("tts_models/en/vctk/vits")
    #history; to change the history file just rename the historyfile variable, make sure to clear your history file after using it
    historyContent = ""
    with open(historyFile, "r") as file:
        historyContent = file.read()


    if debator == 1:
        if debateResponse == None:
            response: ChatResponse = chat(model=AImodel, messages=[
              {
                'role': 'user',
                'content': f'You are {debator1} Your only job is to produce the next message in a heated debate about: {debateTopic}. Strict rules: 1)Speak ONLY as {debator1} 2)NEVER write lines for {debator2}. 3)NEVER include speaker labels (no "{debator1}:" or "{debator2}:"), only produce your raw message. 4)Refer to the other person ONLY as "you", not by name. 5)Use emotional, hostile language. 6)Use simple vocabulary. 7)You may use logical fallacies and personal attacks. 8)Only use the symbols "!" and "?". 9)No formatting. 10)Maximum 2 short sentences. 11)Do NOT repeat what you said earlier. 12)Respond directly to the last thing they said.; Context: You are starting the debate; Now generate only your next message as {debator1}.',
              },
            ])
        else:
            response: ChatResponse = chat(model=AImodel, messages=[
              {
                'role': 'user',
                'content': f'You are {debator1} Your only job is to produce the next message in a heated debate about: {debateTopic}. Strict rules: 1)Speak ONLY as {debator1} 2)NEVER write lines for {debator2}. 3)NEVER include speaker labels (no "{debator1}:" or "{debator2}:"), only produce your raw message. 4)Refer to the other person ONLY as "you", not by name. 5)Use emotional, hostile language. 6)Use simple vocabulary. 7)You may use logical fallacies and personal attacks. 8)Only use the symbols "!" and "?". 9)No formatting. 10)Maximum 2 short sentences. 11)Do NOT repeat what you said earlier. 12)Respond directly to the last thing they said.; Context: The other persons last message was: {debateResponse}. Conversation so far: {historyContent}.; Now generate only your next message as {debator1}.',
              },
            ])
        debateResponse = (response['message']['content'])
        debateResponse = debateResponse.replace("*", "")
        
        with open("history.txt", "a") as file:
            file.write(f"\n\n{debateLength}.{debator1} : {debateResponse}\n")

        wav = tts.tts(text=debateResponse, speaker=debator1Voice)
        sd.play(wav, samplerate=22050)
        sd.wait()
        debator = 2
        debateLength += 1
    elif debator == 2:
       response: ChatResponse = chat(model=AImodel, messages=[
          {
            'role': 'user',
            'content': f'You are {debator2} Your only job is to produce the next message in a heated debate about: {debateTopic}. Strict rules: 1)Speak ONLY as {debator2} 2)NEVER write lines for {debator1}. 3)NEVER include speaker labels (no "{debator1}:" or "{debator2}:"), only produce your raw message. 4)Refer to the other person ONLY as "you", not by name. 5)Use emotional, hostile language. 6)Use simple vocabulary. 7)You may use logical fallacies and personal attacks. 8)Only use the symbols "!" and "?". 9)No formatting. 10)Maximum 2 short sentences. 11)Do NOT repeat what you said earlier. 12)Respond directly to the last thing they said.; Context: The other persons last message was: {debateResponse}. Conversation so far: {historyContent}.; Now generate only your next message as {debator2}.',
          },
        ])
       debateResponse = (response['message']['content'])
       debateResponse = debateResponse.replace("*", "")

       with open(historyFile, "a") as file:
           file.write(f"\n\n{debateLength}.{debator2} : {debateResponse}\n")

       wav = tts.tts(text=debateResponse, speaker=debator2Voice)
       sd.play(wav, samplerate=22050)
       sd.wait()
       debator = 1
       debateLength += 1

# deciding the winner to the debate
response: ChatResponse = chat(model=AImodel, messages=[
  {
    'role': 'user',
    'content': f'You will now say who is the winner of the debate on topic {debateTopic} out of two people {debator1} and {debator2}, based off the debate they had from {historyContent}, give each debator a rating out of 10; keep this short and simple to the point',
  },
])
debateWinner = (response['message']['content'])
print(debateWinner) 

