from gtts import gTTS
import os

mon_text = input()

lecture = gTTS(text=mon_text, lang='fr')

lecture.save("01_test.wav")
os.popen("01_test.wav")
