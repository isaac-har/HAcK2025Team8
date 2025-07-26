from APIkey import apikey
import base64
from openai import OpenAI
import os
# TODO: Import your libaries

client = OpenAI(api_key=apikey)



# Image encoding, code provided
def encode_image(image_path):
    with open(image_path, "rb") as image_F:
        return base64.b64encode(image_F.read()).decode('utf-8')

def openAiProcessing(image_path):
    # Getting the Base64 string
    base64_image = encode_image(image_path)

    # TODO: Sending a request and getting a response
    response = client.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "user",
                "content": [
                    { "type": "input_text", "text": "what's in this image?" },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{base64_image}",
                    },
                ],
            }
        ],
    )

    aiAnalyzedText = response.output_text
    print("AI Response:", aiAnalyzedText)


    # TODO: How do we make things audible?
    script_dir = os.path.dirname(os.path.abspath(__file__))
    speech_file_path = os.path.join(script_dir, "../backend/public/aiSpeech.mp3")
    
    #TODO: FIGURE OUT THIS SPEECH FILE PATH AND SEND TO WEBSITE

    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="ballad",
        input=aiAnalyzedText,
        instructions="Speak in a refined, clear, and serious manner as if you are a prim british butler.",
    ) as response:
        response.stream_to_file(speech_file_path)

    # TODO: Can we put everything together?

