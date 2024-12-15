import pyttsx3
import pdfplumber
from PyPDF2 import PdfReader

#get file name and location
file = r'C:\Users\glamb\OneDrive\Desktop\Proyectos\PDF to Audio\sample.pdf'

#create a pdf object
pdfObj = open(file, 'rb')

#create a pdf reader object
pdfReader = PdfReader(pdfObj)

#get number of pages
pages = len(pdfReader.pages)

#create a pdfplumber object and loop through each page
with pdfplumber.open(file) as pdf:
    for i in range(pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()