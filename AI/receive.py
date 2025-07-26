
# TODO: import your module
from send_to_openai import openAiProcessing
import requests
import os
import sys

# Get the folder where the script is located, done for you
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, "../backend/public/image.jpg")

url = "http://192.168.50.40/1024x768.jpg" # You will have to change the IP Address

# Function to download the image from esp32, given to you
def download_image():
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Image saved to: {filename}")
    else:
        print("Failed to download image. Status code:", response.status_code)

# TODO: Download the image and get a response from openai
def get_description():
    download_image()
    openAiProcessing(filename)
    

# TODO: How to control when to take photo?

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "get_description":
        get_description()

