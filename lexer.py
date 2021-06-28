import ply.lex as lex

reserved = {
	'log':'LOG',
	'input':'INPUT',
	'toInt':'TOINT',
	
	'loop':'LOOP',
	'if':'IF',
	'owise':'OWISE',
	'fun':'FUN',
	
	#'var':'VAR',
	
	'and':'AND',
	'or':'OR',
	'not':'NOT'
}

tokens = [
	
	'INT',
	'STRING',
	'NAME',
	
	'TRUE',
	'FALSE',
	
	'LEND',
	'LPAREN',
	'RPAREN',
	'LBRKT',
	'RBRKT',
	'COMMA',
	
	'PLUS',
	'MINUS',
	'DIVIDE',
	'MULT',
	'POW',
	'MOD',
	'ASSIGN',
	
	'EQ',
	'NEQ',
	'MT',
	'LT'
	
] + list(reserved.values())

t_LEND = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRKT = r'{'
t_RBRKT = r'}'
t_COMMA = r'\|'
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'\/'
t_MULT = r'\*'
t_POW = r'\^'
t_MOD = r'\%'
t_ASSIGN = r'->'
t_EQ = r'=='
t_NEQ = r'!='
t_MT = r'>'
t_LT = r'<'

t_ignore = ' \t\n'
t_ignore_COMMENTS = r'\[-[\S\s]*?-\]'

def t_TRUE(t):
	'true'
	t.value = True
	return t
	
def t_FALSE(t):
	'false'
	t.value = False
	return t

def t_INT(t):
	'\d+'
	t.value = int(t.value)
	return t

def t_STRING(t)	:
	'"(?:"|.)*?"'
	t.value = t.value.lstrip('"').rstrip('"')
	return t
	
def t_NAME(t):
	'[a-zA-Z][a-zA-Z0-9_]*'
	t.type = reserved.get(t.value, t.type)
	return t

def t_error(t):
	print("SyntaxError: Illegal characters in '%s' found!" % t.value)
	t.lexer.skip(1)

lexer = lex.lex()
