import config 
#import tts
import stt

# This function requests user input and then check if voice input is empty, requer to write
def user_input_detection() -> str:
	input_user = stt.voice_input()
	print(input_user)
	if not input_user:
		input_user = input('Write request manually - ')

	while True:
		# Validate if input isn't empty and 'delete'(in the moment) spaces and contains only words
		if input_user and input_user.replace(' ', '').isalpha(): # r'[A-Za-z ]+' Can also make with regular expressions
			print('Successfully input!', input_user)
			return input_user
		else:
			input_user = input('Please write only words - ')

def user_input_cleaning(user_input: str) ->  str:
	# Cleans user input by removing 'call_words' like 'eva' or 'say'. To get exect command
	
	split_user_input = user_input.lower().split()
	filtered_user_input = ' '.join([word for word in split_user_input if word not in config.call_words])
	
	return filtered_user_input

def function_detection(user_input: str) -> str:
	# This function take user input with 'str' type and then try to detect what want a user
	
	split_user_input = user_input.split()
	command = split_user_input[0] # The first word to match a command
	arg = ' '.join(split_user_input[1:]) if len(split_user_input) > 1 else None  # Pass remaining words as arguments

	if command in config.functions:
		
		# Check have we argument [open (youtube.com) - argument] Example
		if arg:
			result = config.functions[command](arg)	# Pass argument if there is one
			print(result)
		else:
			result = config.functions[command]() # Call without argument
			print(result)		
	else: 
		print(f'Function {user_input.split()[0]} doesn\'t exist!')

	return f'User input - {user_input}'

while True:
	#tts.voice_output('Hi, how are doing? How i can help you')
	user_input = user_input_detection()
	cleaned_input = user_input_cleaning(user_input) # Clean the user input
	function_detection(cleaned_input)				# Detect and execute the function	







'''

	Good explanation of how function_detection is worked, here - https://chatgpt.com/share/671b975e-1808-800c-a5f9-e29e90952143


'''	
