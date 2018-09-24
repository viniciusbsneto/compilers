import re

# Main function
def main():
	'''
	Main function - the first function to be executed
	'''
	sourceCodeName = input("Digite o nome do programa fonte: ")

	tokens = []

	with open(sourceCodeName) as f:
		c = f.read(1)
		while True:
			if not c:
				break
			consumeIrrelevantCharacters(f, c)
			t = createToken(f, c)
			tokens.append(t)
		f.close()		
		print(tokens)

# Main function sub-routines
def consumeIrrelevantCharacters(sourceCodeFile, c):
	'''
	Sub-routine that ignores irrelevant characters
	like comments, spaces, linebreaks and tabs
	'''
	if(c == "BeginComment"):
		while (c != "EndComment"):
			c = sourceCodeFile.read(1)

	while (re.match('\s', c, 1)):
		c = sourceCodeFile.read(1)

def createToken(sourceCodeFile, c):
	'''
	Sub-routine that creates the tokens
	'''
	token = ""
	if(re.match('\w', c, 1)):
		while (re.match('\w|\d', c, 1)):
			token += c
			c = sourceCodeFile.read(1)
		return token
	if(re.match('\d', c, 1)):
		while (re.match('\d', c)):
			token += c
			c = sourceCodeFile.read(1)
		return token
	
# Begin of program execution
main()