import speech_recognition as sr

recognizer = sr.Recognizer()

def voice_input():
	try:	
		with sr.Microphone() as source:
			print('Now you can say')
			recognizer.adjust_for_ambient_noise(source)
			user_input = recognizer.listen(source) 
		return recognizer.recognize_google(user_input)
	
	except sr.UnknownValueError:
		# Raised when recognizer doesn't understand the audio

		return 'I can\'t understand what are you saying'

	except OSEError as e:
		# Raised if there's a problem eccessing the micriphone
		print('Microphone not found or not accesible')

		return None

	except Exception as e:
		# Raised for unexpected errors
		print(f'Error - {e}')
		
		return None

if __name__ == '__main__':
	print(voice_input())
