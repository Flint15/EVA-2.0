import time 
import webbrowser
import psutil
import config

def get_time():
	# Return the current time to track opened sites

	return time.strftime('%H:%M:%S')

def open_site(website):
	# Open the specified site in the default web browser

	# Process the input to create a valid URL
	if 'dot com' in website:
		website = website.replace('dot com', '.com')
	else:
		website += '.com'

	url = f'https://www.{website}'
		
	try:	
		webbrowser.open(url)
		time.sleep(2) # Wait for the browser to open
	except Exception as e:
		print(f'Error opening site: {e}')

		return None

	# Track the opened site process
	for process in psutil.process_iter(['pid', 'name', 'cmdline']):
		cmdline = process.info.get('cmdline')  # Safely get cmdline
		if cmdline and isinstance(cmdline, list):  # Ensure cmdline is a list
			if url in ' '.join(cmdline):
				print('1')	
				config.opened_sites[url] = process.info['pid']  # Track URL and PID
				print(f'Opened site: {url} with PID: {process.info["pid"]}')
				config.pid = process.info['pid']  # Store the PID in config

				return None

	return None		

def close_site(website):
	# Close the specified site if it's opened

	# Process the input to create a valid URL
	if 'dot com' in website:
		website = website.replace('dot com', '.com')
	else:
		website += '.com'	

	url = f'https://{website}'
		
	if url in config.opened_sites:
		pid = config.opened_sites[url]

		try:
			p = psutil.Process(config.pid)
			p.terminate() # Close the browser process
			print(f'Site {website} is closed')
			del config.opened_sites[website] # Remove from tracking
		except psutil.NoSuchProcess:
			print(f'No opened site found or already closed')

	else:
		print(config.opened_sites)
		print(f'No opened site found for: {config.opened_sites[url]}')		
