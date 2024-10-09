from flask import Flask, request
from PIL import Image
import io

app = Flask(__name__)

# Replace with the server's IP address
server_ip = "0.0.0.0"  # Replace with the actual IP address

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    response = f"Received message: {message}"
    return response

@app.route('/analyze_image', methods=['POST'])
def analyze_image():
    # Check if a file was uploaded
    if 'image' not in request.files:
        return 'No image file was provided.', 400

    file = request.files['image']

    # Check if the file is empty or has an invalid extension
    if file.filename == '':
        return 'No image file was provided.', 400

    # Process the image
    try:
        img = Image.open(file.stream)
        width, height = img.size
        format = img.format
        mode = img.mode
        response = f"Image details:\nWidth: {width}\nHeight: {height}\nFormat: {format}\nMode: {mode}"
        return response
    except Exception as e:
        return f"Error processing the image: {str(e)}", 500

if __name__ == '__main__':
    app.run(host=server_ip, port=1111, debug=True)  # Use the server's IP address