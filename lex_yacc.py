# List of token names (reserved words)
reserved = {

	'typedef' : 'TYPEDEF',
	'double'  : 'DOUBLE',
	'struct'  : 'STRUCT',
	'int' 	  : 'INT',
	'float'   : 'FLOAT',
	'while'   : 'WHILE',
	'if'      : 'IF',
	'return'  : 'RETURN',
	'else'    : 'ELSE',
	'printf'  : 'PRINTF',
	'scanf'   : 'SCANF',
	'main'    : 'MAIN',

}

# List of token names
tokens = [
		
	'COMMA',
	'SEMICOLON',
	'ADD',
	'SUB',
	'MULT',
	'DIV',
	'OPEN_PARENTHESIS',
	'CLOSE_PARENTHESIS',
	'EQUALS',
	'ASSIGNMENT',
	'DIFFERENT',
	'LT',
	'GT',
	'OPEN_BRACKETS',
	'CLOSE_BRACKETS',
	'OPEN_CURLY',
	'CLOSE_CURLY',
	'PUNCTUATION',
	'STRING',
	'NUMBER',
	'IDENTIFIER',
	'ERROR'

] + list(reserved.values())

# Regular expression rules for simple tokens
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_ADD = r'\+'
t_SUB = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_OPEN_PARENTHESIS = r'\('
t_CLOSE_PARENTHESIS = r'\)'
t_EQUALS = r'\=+\=+'
t_DIFFERENT = r'\!+\=+'
t_ASSIGNMENT = r'\='
t_LT = r'\<'
t_GT = r'\>'
t_OPEN_BRACKETS = r'\['
t_CLOSE_BRACKETS = r'\]'
t_OPEN_CURLY = r'\{'
t_CLOSE_CURLY = r'\}'
t_PUNCTUATION = '\.'

# A string containing ignored (literal) characters (spaces and tabs)
t_ignore = ' \t'

# Define a rule so we can track line numbers
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

# Define a rule to ignore single-line or multi-line comments
def t_COMMENT(t):
	r'[/]+[/]+.*|([/][*][^*]*[*]+([^*/][^*]*[*]+)*[/])'
	pass

# Define a rule to classify string
def t_STRING(t):
	r'\'+.*\'+|\"+.*\"+'
	t.type = 'STRING'
	return t

# Define a rule to classify a number
def t_NUMBER(t):
	r'\d+[.\d]*'
	t.type = 'NUMBER'
	return t

# Define a rule to classify an identifier
def t_IDENTIFIER(t):
	r'[a-zA-Z_]+[a-zA-Z_0-9]*'
	t.type = reserved.get(t.value, 'IDENTIFIER')
	return t

# Error handling rule
def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Reference to file and input text
with open('program.c') as f:
	content = f.read()
f.close()

# Tokenize
lexer.input(content)
print("\n|----------------------------ANÁLISE LÉXICA----------------------------|\n")
print("Formato: (CLASSE, lexema, linha)\n")
while True:
	tok = lexer.token()
	if not tok: 
	    break      # No more input
	print("(%s, '%s', %s)" %(tok.type, tok.value, tok.lineno))
print("\n")


def p_PROGRAMA(p):
	'''
	PROGRAMA : DECLARACOES DEF_FUNCOES
	'''
	p[0] = p[1] + p[2]

def p_DECLARACOES(p):
	'''
	DECLARACOES : DEF_TIPOS DEF_VARIAVEIS
	'''
	p[0] = p[1] + p[2]

def p_DEF_VARIAVEIS(p):
	'''
	DEF_VARIAVEIS : DEF_VARIAVEL SEMICOLON DEF_VARIAVEIS
				  | empty
	'''
	if (len(p) == 4):
		p[0] = p[1] + p[2] + p[3]
	else:
		p[0] = ''

def p_DEF_TIPOS(p):
	'''
	DEF_TIPOS : DEF_TIPO SEMICOLON DEF_TIPOS
			  | empty
	'''
	if (len(p) == 4):
		p[0] = p[1] + p[2] + p[3]
	else:
		p[0] = ''

def p_DEF_FUNCOES(p):
	'''
	DEF_FUNCOES : FUNCAO DEF_FUNCOES
				| empty
	'''
	if (len(p) == 3):
		p[0] = p[1] + p[2]
	else:
		p[0] = ''

def p_IDENTIFICADOR(p):
	'''
	IDENTIFICADOR : IDENTIFIER
	'''
	p[0] = p[1]

def p_NUMERO(p):
	'''
	NUMERO : NUMBER
	'''
	p[0] = p[1]

def p_DEF_TIPO(p):
	'''
	DEF_TIPO : TYPEDEF TIPO_DADO IDENTIFICADOR
	'''
	p[0] = p[1] + p[2] + p[3]

def p_DEF_VARIAVEL(p):
	'''
	DEF_VARIAVEL : TIPO_DADO IDENTIFICADOR LISTA_ID
	'''
	p[0] = p[1] + p[2] + p[3]

def p_LISTA_ID(p):
	'''
	LISTA_ID : OPEN_BRACKETS NUMERO CLOSE_BRACKETS LISTA_ID
			 | COMMA IDENTIFICADOR LISTA_ID
			 | empty
	'''
	if (len(p) == 5):
		p[0] = p[1] + p[2] + p[3] + p[4]
	elif (len(p) == 4):
		p[0] = p[1] + p[2] + p[3]
	else:
		p[0] = ''

def p_TIPO_DADO(p):
	'''
	TIPO_DADO : INT
			  | FLOAT
			  | DOUBLE
			  | STRUCT IDENTIFICADOR OPEN_CURLY DEF_VARIAVEIS CLOSE_CURLY
			  | IDENTIFICADOR
	'''
	if (len(p) == 6):
		p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
	else:
		p[0] = p[1]

def p_FUNCAO(p):
	'''
	FUNCAO : NOME_FUNCAO BLOCO
	'''
	p[0] = p[1] + p[2]

def p_NOME_FUNCAO(p):
	'''
	NOME_FUNCAO : TIPO_DADO IDENTIFICADOR OPEN_PARENTHESIS DEF_VARIAVEIS CLOSE_PARENTHESIS
	'''
	p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

def p_BLOCO(p):
	'''
	BLOCO : OPEN_CURLY DEF_VARIAVEIS COMANDOS CLOSE_CURLY
	'''
	p[0] = p[1] + p[2] + p[3] + p[4]

def p_COMANDOS(p):
	'''
	COMANDOS : COMANDO SEMICOLON COMANDOS
			 | empty
	'''
	if (len(p) == 4):
		p[0] = p[1] + p[2] + p[3]
	else:
		p[0] = ''

def p_COMANDO(p):
	'''
	COMANDO : NOME ASSIGNMENT VALOR
			| WHILE OPEN_PARENTHESIS EXP_LOGICA CLOSE_PARENTHESIS BLOCO
			| IF OPEN_PARENTHESIS EXP_LOGICA CLOSE_PARENTHESIS BLOCO ELSENT
			| PRINTF OPEN_PARENTHESIS NOME_NUMERO CLOSE_PARENTHESIS
			| SCANF OPEN_PARENTHESIS NOME CLOSE_PARENTHESIS
			| RETURN VALOR
	'''
	if (len(p) == 7):
		p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
	elif (len(p) == 6):
		p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
	elif (len(p) == 4):
		p[0] = p[1] + p[2] + p[3]
	else:
		p[0] = p[1] + p[2]

def p_ELSENT(p):
	'''
	ELSENT : ELSE BLOCO
		 | empty
	'''
	if (len(p) == 3):
		p[0] = p[1] + p[2]
	else:
		p[0] = ''

def p_VALOR(p):
	'''
	VALOR : EXP_MATEMATICA
		  | IDENTIFICADOR PARAMETROS
		  | STRING
	'''
	if (len(p) == 3):
		p[0] = p[1] + p[2]
	else:
		p[0] = p[1]

def p_PARAMETROS(p):
	'''
	PARAMETROS : OPEN_PARENTHESIS PARAMETRO CLOSE_PARENTHESIS
	'''
	p[0] = p[1] + p[2] + p[3]

def p_PARAMETRO(p):
	'''
	PARAMETRO : LISTA_PARAM
			  | empty
	'''
	if (len(p) == 2):
		p[0] = p[1]
	else:
		p[0] = ''

def p_LISTA_PARAM(p):
	'''
	LISTA_PARAM : NOME_NUMERO COMMA LISTA_PARAM
	            | NOME_NUMERO
	'''
	if (len(p) == 4):
		p[0] = p[1] + p[2] + p[3]
	else:
		p[0] = p[1]

def p_EXP_LOGICA(p):
	'''
	EXP_LOGICA : EXP_MATEMATICA OP_LOGICO EXP_LOGICA
			   | EXP_MATEMATICA
	'''
	if (len(p) == 4):
		p[0] = p[1] + p[2] + p[3]
	else:
		p[0] = p[1]

def p_OP_LOGICO(p):
	'''
	OP_LOGICO : GT
			  | LT
			  | EQUALS
			  | DIFFERENT
	'''
	p[0] = p[1]

def p_EXP_MATEMATICA(p):
	'''
	EXP_MATEMATICA : NOME_NUMERO OP_MATEMATICO EXP_MATEMATICA
				   | NOME_NUMERO
	'''
	if (len(p) == 4):
		p[0] = p[1] + p[2] + p[3]
	else:
		p[0] = p[1]

def p_OP_MATEMATICO(p):
	'''
	OP_MATEMATICO : ADD
				  | SUB
				  | MULT
				  | DIV
	'''
	p[0] = p[1]

def p_NOME_NUMERO(p):
	'''
	NOME_NUMERO : NOME
				| NUMERO
	'''
	p[0] = p[1]

def p_NOME(p):
	'''
	NOME : IDENTIFICADOR
		 | IDENTIFICADOR PUNCTUATION NOME
		 | IDENTIFICADOR OPEN_BRACKETS NOME_NUMERO CLOSE_BRACKETS
	'''
	if (len(p) == 5):
		p[0] = p[1] + p[2] + p[3] + p[4]
	elif (len(p) == 4):
		p[0] = p[1] + p[2] + p[3]
	else:
		p[0] = p[1]

def p_empty(p):
	'''
	empty :
	'''
	pass

def p_error(p):
	if p:
		print("Syntax error at token %s in line %s" %(p.type, p.lineno))
	else:
		print("Syntax error at EOF")

# Build the parser
import ply.yacc as yacc
parser = yacc.yacc()

print("|-------------------------ANÁLISE SINTÁTICA-------------------------|\n")

# Parsing
parser.parse(content)
