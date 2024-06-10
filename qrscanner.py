import qrcode
from pyzbar.pyzbar import decode
from PIL import image


myqr = qrcode.make("https://www.linkedin.com/in/ros-/")
myqr.save("myqr.png", scale = 8)

# myqr = qrcode.make_image(fill_color = "red",back_color = "black")
#  to decode the link 

b = decode(image.open("myqr.png"))
print(b[0].data.decode("ascii"))