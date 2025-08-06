import os
import requests
from gtts import gTTS

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    if not ELEVENLABS_API_KEY:
        raise ValueError("ELEVENLABS_API_KEY environment variable is not set!")
    
    try:
        url = f"https://api.elevenlabs.io/v1/text-to-speech/dPKFsZN0BnPRUfVI2DUW"
        
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": ELEVENLABS_API_KEY  # This is the crucial header that was missing
        }
        
        data = {
            "text": input_text,
            "model_id": "eleven_turbo_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }
        
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # This will raise an exception for 4xx/5xx status codes
        
        with open(output_filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"Audio saved successfully to {output_filepath}")
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        print(f"Response status: {response.status_code}")
        print(f"Response text: {response.text}")
        raise
    except Exception as e:
        print(f"ElevenLabs API error: {e}")
        raise

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    if not ELEVENLABS_API_KEY:
        raise ValueError("ELEVENLABS_API_KEY environment variable is not set!")
    
    try:
        url = f"https://api.elevenlabs.io/v1/text-to-speech/dPKFsZN0BnPRUfVI2DUW"
        
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json", 
            "xi-api-key": ELEVENLABS_API_KEY  # Critical authentication header
        }
        
        data = {
            "text": input_text,
            "model_id": "eleven_turbo_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }
        
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        
        # Save the audio file
        with open(output_filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"Audio generated and saved to {output_filepath}")
        
        # Play audio code (your existing code)
        import subprocess
        import platform
        os_name = platform.system()
        try:
            if os_name == "Darwin":  # macOS
                subprocess.run(['afplay', output_filepath])
            elif os_name == "Windows":  # Windows
                subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
            elif os_name == "Linux":  # Linux
                subprocess.run(['aplay', output_filepath])
            else:
                raise OSError("Unsupported operating system")
        except Exception as play_error:
            print(f"An error occurred while trying to play the audio: {play_error}")
            
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        if hasattr(e, 'response'):
            print(f"Response status: {e.response.status_code}")
            print(f"Response text: {e.response.text}")
        raise
    except Exception as e:
        print(f"ElevenLabs API error: {e}")
        raise
