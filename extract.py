import PyPDF2
import PIL
import png
import minecart
import os

inp = input("What file would you like to extract from? ")
print(inp)
pdfFile = open(inp, 'rb') 
text = open ('temp.txt', 'wb')
read = PyPDF2.PdfFileReader(pdfFile)
i = 0
s = ""
while i < read.getNumPages():
    page = read.getPage(i)
    s += page.extractText()
    i += 1

text.write(s.encode('utf-8', 'ignore'))

pdffile = open(inp, 'rb')
doc = minecart.Document(pdffile)

page = doc.get_page(0) # getting a single page
i = 0
#iterating through all pages
for page in doc.iter_pages():
    try:
        img = page.images[0].as_pil()  # requires pillow
        t = os.path.dirname(os.path.realpath(inp)) + "\\" + str(i) + '.jpg'
        img.save(t, "JPEG", quality=80, optimize=True, progressive=True)
        i += 1
    except:
        print()
