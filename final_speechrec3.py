from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
import send
import pdf_generation
import updating_csv

from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="KeyWords[i]"+': ' +  "Result[i]", ln=1, align="C")
#pdf.cell(200, 10, txt=Name, ln=1, align="C")

#pdf.cell(200, 10, txt=Gender, ln=1, align="C")





language = "en"
r = sr.Recognizer()
sr.operation_timeout = 10
#sr.adjust_for_ambient_noise(Microphone, duration = 1) 
def record(text_display,parameter):
	with sr.Microphone() as source:
		print(text_display)
		audio = r.listen(source)
		try:
			parameter= r.recognize_google(audio)
			print("You said : {}".format(parameter))
		except:
			print("Sorry could not recognize what you said")
	return parameter




KeyWords = ['Name','Age','Gender','Symptoms','Diagnosis','Prescription','Advice']
#KeyWords = ['Name','Age','Gender']
FileName = ['Name.mp3','Age.mp3','Gender.mp3','Symptoms.mp3','Diagnosis.mp3','Prescription.mp3','Advice.mp3']


Result = {'Name': [], 'Age': [], 'Gender': [], 'Symptoms': [], 'Diagnosis': [], 'Prescription': [], 'Advice': []} 

#print(Result.keys())
for i in range(0,len(KeyWords)):
	result = ''
	playsound(FileName[i])
	while 'next' not in result.split() :
		result = record(KeyWords[i] ,KeyWords[i])
		if result == 'enable editing':
			Result = updating_csv.edit_credentials(Result)
			break
		elif result != 'next':
			print(type(Result[KeyWords[i]]))

			Result[KeyWords[i]].append(result)



a = list(Result.keys())
b = list(Result.values())

for i in Result:
	text = i + ' ' + str(Result[i])
	pdf.cell(200, 10, txt=text, ln=1, align="C")

pdf.output("Result[0].pdf")





send.send_mail('shalinisaigal0@gmail.com','hello',"Result[0].pdf","we are sending a attachment",'sih987659@gmail.com')