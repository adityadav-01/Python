import qrcode  # QR code library import karte hain

data = "https://github.com/adityadav-01"  # Link jo QR me store hoga
qr = qrcode.make(data)  # QR code generate karte hain
qr.save("qrcode.png")   # QR code ko image file me save karte hain
print("QR CODE GENERATED SUCCESSFULLY")  # Confirmation message
