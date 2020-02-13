from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
import send
import editing
language = "en"
r = sr.Recognizer()


def prompt(text2,file_name):
	output = gTTS(text = text2, lang = language,slow = False)
	output.save('file_name.mp3')
	playsound('file_name.mp3')


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




from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
#pdf.cell(200, 10, txt=Name, ln=1, align="C")

#pdf.cell(200, 10, txt=Gender, ln=1, align="C")





KeyWords = ['Name','Age','Gender','Symptoms','Diagnosis','Prescription','Advice']
FileName = ['Name.mp3','Age.mp3','Gender.mp3','Symptoms.mp3','Diagnosis.mp3','Prescription.mp3','Advice.mp3']

Result = []


for i in range(0,len(KeyWords)):
	b = 'a'
	prompt(KeyWords[i],FileName[i])
	while b != 'next':
		result = record(KeyWords[i] ,KeyWords[i] )
		a = result.split(" ")
		b = a[-1]
	
	Result.append(result)
	pdf.cell(200, 10, txt=KeyWords[i] +': ' +  Result[i], ln=1, align="C")

pdf.output("Result[0].pdf")


send.send_mail('shalinisaigal0@gmail.com','hello',"Result[0].pdf","we are sending a attachment",'sih987659@gmail.com')