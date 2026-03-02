import qrcode

data = input('Enter the Text or URL: ').strip()
file_name = input('Enter The Filename: ')

qrcode.QRCode(box_size = 15 , border = 5)
qr.add_data(data)
image = qr.make_image(fill_colour = 'black' , back_colour = 'white')
image.save(file_name)
print(f'QR code saved as {file_name}')awa