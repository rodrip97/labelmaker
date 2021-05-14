import pandas as pd
import qrcode
import os

data = pd.read_excel("nodes.xlsx") # uses pandas to open the file with the QR code data
dataqr = data['Barcode/QR1-Data'] # selects the cell with the QR data
dirpath = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(dirpath, 'images')


for number, item in enumerate(dataqr): # for each row create a different QR code
    img = qrcode.make(item)
    img.save(os.path.join(image_path, f"{number}'qr.jpg"))
