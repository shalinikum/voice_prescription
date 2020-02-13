
from gtts import gTTS
language = 'en'



FileName = ['Name.mp3','Age.mp3','Gender.mp3','Symptoms.mp3','Diagnosis.mp3','Prescription.mp3','Advice.mp3']
KeyWords = ['Name','Age','Gender','Symptoms','Diagnosis','Prescription','Advice']

def prompt(text,file_name):
	output = gTTS(text = text, lang = language,slow = False)
	output.save('/home/shalini/Desktop/sih_2020/{}'.format(file_name))
	
	


for i in range(0,len(KeyWords)):
	prompt(KeyWords[i],FileName[i])
	
	