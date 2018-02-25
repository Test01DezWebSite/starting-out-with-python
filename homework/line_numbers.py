# Matthew Kosloski
#
# Program asks the user for the 
# name of a file. The contents
# of the file should be printed
# and preceeded with a line number.

def main():

	filename = input('Name of the file: ')

	try:

		infile = open(filename, 'r')

		result = ''
		current_line = 1

		for line in infile:
			result += f'{current_line}: {line}'
			current_line += 1

		infile.close()

	except IOError:
		print(f'Failed to read file {filename}. :(')
	else:
		print(f'Contents of {filename}:\n')
		print(result)

main()