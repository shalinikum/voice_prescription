from gtts import gTTS
import os
#import pygame
#pygame.init()
#pygame.display.set_mode()

mytext = "text to speech conversion using python"

language = "en"
output = gTTS(text = mytext, lang = language,slow = False)

output.save('output.mp3')
#os.system("start output.mp3")

#drum = pygame.mixer.Sound("./output.mp3")
from playsound import playsound
playsound('output.mp3')