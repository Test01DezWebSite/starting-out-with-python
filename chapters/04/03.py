# Program 4-3
# This program demonstrates an infinite loop.

# Create a variable to represent the maximum
# temperature.
max_temp = 102.5

# Get temperature of substance
temperature = float(input('Enter the substance\'s Celsius temperature: '))

# As long as necessary, instruct the user to
# adjust the thermostat.
while temperature > max_temp:
	print('The temperature is too high.\n' +
		'Turn the thermostat down and wait\n' +
		'5 minutes. Then take the temperature\n' +
		'again and enter it.\n'
	)
	# No way to stop the loop now
	# temperature = float(input('Enter the substance\'s Celsius temperature: '))

# Remind the user to check the temperature again
# in 15 minutes.
print('The temperature is acceptable.\n' +
	'Check it again in 15 minutes.'
)