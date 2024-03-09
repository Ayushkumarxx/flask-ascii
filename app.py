from flask import Flask, request, render_template, send_file
from PIL import Image, ImageDraw, ImageFont
import math
import os
app = Flask(__name__,  static_folder='static')

# Function to cycle through characters of a string
repeatedCharIndex = 0
def getRepeatedChar(repeatedChar):
    global repeatedCharIndex
    repeatedCharLength = len(repeatedChar)
    
    char = repeatedChar[repeatedCharIndex]
    repeatedCharIndex = (repeatedCharIndex + 1) % repeatedCharLength
    
    return char

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get input from the form
        image_file = request.files['image']
        text = request.form['text']
        
        # Process the image
        scaleFactor = 0.3
        oneCharWidth = 10
        oneCharHeight = 16

        im = Image.open(image_file)
        
        fnt = ImageFont.load_default()
        width, height = im.size
        im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.Resampling.NEAREST)
        width, height = im.size
        pix = im.load()
        static_folder_path = os.path.join(os.path.dirname(__file__), 'static')
        output_img_path = os.path.join(static_folder_path, 'output.png')
        
        # Delete the existing output image if it exists
        if os.path.exists(output_img_path):
            os.remove(output_img_path)

        if not os.path.exists(static_folder_path):
           os.makedirs(static_folder_path)

        
        outputImg2 = Image.new("RGB", (oneCharWidth * width, oneCharHeight * height) , color=(0,0,0))
        d2 = ImageDraw.Draw(outputImg2)

        for i in range(height):
            for j in range(width):
                r, g, b = pix[j, i]
                h = int(r/3 + g/3 + b/3)
                pix[j, i] = (h, h, h)
                d2.text((j*oneCharWidth, i*oneCharHeight), getRepeatedChar(text), font=fnt, fill=(r,g,b))

        outputImg2.save(output_img_path)
        
        # Return the output image
        return render_template('index.html', output_image=output_img_path)
       

    return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
