from urllib.request import  urlopen
from PIL import Image
import io





# Opening an image in python binary mode
# getting the path or url of the image and assigning it to a variable
image = "/Users/5th gen/Documents/GitHub/Projects/PythonProjects/image/python1.jpeg"
image2 = "image/python2.jpeg"
with open(image2, mode="rb") as image_file:
    content = image_file.read()
#print(content)
print(len(content))  #prints the size of the image 


# Checking the size of an image from a url
url = 'https://storage.googleapis.com/fm-01/car.jpg'
img = Image.open(urlopen(url))
image = img.tobytes()
print(len(image))


# reading images from urls
url = "https://www.facebook.com/photo?fbid=778498209298507&set=pob.100000303181374/79792836_778498212631840_8624473001007513600_n.jpeg"
image = urlopen(url)
image_file = io.BytesIO(image.read())
im = Image.open(image_file)
im = im.tobytes()