import os
from elevenlabs import generate, save, set_api_key

# Set the API key globally (recommended approach)
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")
if ELEVENLABS_API_KEY:
    set_api_key(ELEVENLABS_API_KEY)

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    if not ELEVENLABS_API_KEY:
        raise ValueError("ELEVENLABS_API_KEY environment variable is not set!")
    
    try:
        # Use the direct generate function (most reliable)
        audio = generate(
            text=input_text,
            voice="dPKFsZN0BnPRUfVI2DUW",  # This should work with voice ID
            model="eleven_turbo_v2"
        )
        
        # Save the audio
        save(audio, output_filepath)
        print(f"Audio saved successfully to {output_filepath}")
        
    except Exception as e:
        print(f"ElevenLabs API error: {e}")
        raise

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    if not ELEVENLABS_API_KEY:
        raise ValueError("ELEVENLABS_API_KEY environment variable is not set!")
    
    try:
        # Use the direct generate function
        audio = generate(
            text=input_text,
            voice="dPKFsZN0BnPRUfVI2DUW",
            model="eleven_turbo_v2"
        )
        
        # Save the audio file
        save(audio, output_filepath)
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
            
    except Exception as e:
        print(f"ElevenLabs API error: {e}")
        raise
