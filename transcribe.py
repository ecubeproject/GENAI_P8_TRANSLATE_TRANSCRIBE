# The WhisperAPI currently accepts the following file types:
# mp3, mp4, mpeg, mpga, m4a, wav, and webm
from openai import OpenAI
import config

client = OpenAI(api_key=config.API_KEY)

# Load the audio file

f = open("audio_files/apple.mp3", "rb")
f2 = open("audio_files/german.mp3", "rb")

# Call the appropriate method for transcription
result = client.audio.transcriptions.create(file=f, model="whisper-1")
result2 = client.audio.translations.create(file=f2, model="whisper-1")
print(result)
print(result2)
