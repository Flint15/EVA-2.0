import torch
import torchaudio
import sounddevice as sd

# Define language and speker
language = 'en'
speaker = 'lj_16khz'

# Select device (CPU or GPU)
device =  torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load the Silero TTS model
model, symbols, sample_rate, example_text, apply_tts = torch.hub.load(
	repo_or_dir='snakers4/silero-models',
	model='silero_tts',
	language=language,
	speaker=speaker
	)

# Move model to the appropriate device
model = model.to(device)

# Function to generate and play audio
def voice_output(text):
	try:	
		# Generate audio using the TTS model
		audio = apply_tts(texts=[text],
						  model=model,
						  sample_rate=sample_rate,
						  symbols=symbols,
						  device=device)

		# Play audio
		sd.play(audio[0].numpy(), sample_rate)
		sd.wait()
	except Exception as e:
		print(f'Error during audio playback: {e}')

if __name__ == '__main__':
	voice_output('My bones hurt like hell')
