import pygame
from gtts import gTTS
def text_to_speech(text, output_filename="output.mp3"):
  tts=gTTS(text)
  tts.save(output_filename)
  pygame.mixer.init()
  pygame.mixer.music.load(output_filename)
  pygame.mixer.music.play()
  while pygame.mixer.music.get_busy():
    continue
text=input("enter the text to convert to audio")
text_to_speech(text)