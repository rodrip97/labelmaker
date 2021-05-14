import pandas as pd
import qrcode
import os


def qr_maker():
    dirpath = os.path.dirname(os.path.abspath(__file__))
    data = pd.read_excel(os.path.join(dirpath, "nodes.xlsx"), engine='openpyxl')
    dataqr = data['Barcode/QR1-Data']  # selects the cell with the QR data
    image_path = os.path.join(os.path.dirname(dirpath), 'static', 'images')

    list_images = []
    for number, item in enumerate(dataqr):  # for each row create a different QR code
        img = qrcode.make(item)
        img.save(os.path.join(image_path, f"{number}'qr.jpg"))
        list_images.append(f"static/images/{number}'qr.jpg")

    return list_images


def sid_finder():

    dirpath = os.path.dirname(os.path.abspath(__file__))
    siddata = pd.read_excel(os.path.join(dirpath, "nodes.xlsx"), engine='openpyxl')
    return siddata['SID'].values.tolist()


if __name__ == '__main__':
    list_items = qr_maker()
    for i in list_items:
        print(i)

    list_sid = sid_finder()
    for nr in list_sid:
        print(nr)



