from flask import Flask, escape, request,json,jsonify
from PIL import Image
import base64
from flask_cors import CORS
from io import BytesIO

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    id = request.args.get("id")
    #img = Image.open(r'C:\Users\Kural D Venkat\Desktop\image.png')

    image = open(r'C:\Users\Kural D Venkat\Desktop\image.png', 'rb') #open binary file in read mode 
    image_read = image.read() 
    image_64_encode = base64.encodestring(image_read)

    #data = {}
    #data['image'] = image_64_encode.decode("utf-8")
    return str(data)

if __name__ == "__main__":
    app.run(debug=True)

