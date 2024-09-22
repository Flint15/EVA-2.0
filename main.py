def user_input_detection() -> str:
	# This function requests user input and then check if the user input isn't words, then request to write only words
	input_user = input('Write request manually - ')

	while True:
		# Validate if input isn't empty and contains only words
		if input_user and input_user.isalpha():
			print('Successfully input!')
			return input_user
		else:
			input_user = input('Please write only words - ')

def function_detection(user_input: str) -> str:
	# This function take user input with 'str' type and then try to detect what want a user

	if user_input in config.functions:
		result = config.functions[user_input]()
		print(result)
	
	return f'User input - {user_input}'

while True:
	user_input = user_input_detection()
	print(function_detection(user_input))
