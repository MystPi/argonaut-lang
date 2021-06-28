import ply.yacc as yacc
from argonautLexer import *

precedence = (
	('left', 'NOT', 'EQ', 'NEQ', 'MT', 'LT'),
	('left', 'PLUS', 'MINUS'),
	('left', 'MULT', 'DIVIDE'),
	('right', 'POW', 'MOD'),
)

env = {}
funs = {}
funs_ret = {}
exit = 0

def run(p):
	global env
	global funs
	global funs_ret
	global exit
	
	if type(p) == tuple:
		
		if p[0] == 'log':
			print(run(p[1]))
			
		if p[0] == '+':
			return run(p[1]) + run(p[2])
		elif p[0] == '-':
			return run(p[1]) - run(p[2])
		elif p[0] == '*':
			return run(p[1]) * run(p[2])
		elif p[0] == '/':
			return run(p[1]) / run(p[2])
		elif p[0] == '^':
			return run(p[1]) ** run(p[2])
		elif p[0] == '%':
			return run(p[1]) % run(p[2])
			
		elif p[0] == '==':
			return run(p[1]) == run(p[2])
		elif p[0] == '!=':
			return run(p[1]) != run(p[2])
		elif p[0] == '>':
			return run(p[1]) > run(p[2])
		elif p[0] == '<':
			return run(p[1]) < run(p[2])
			
		elif p[0] == 'and':
			return run(p[1]) and run(p[2])
		elif p[0] == 'or':
			return run(p[1]) or run(p[2])
		elif p[0] == 'not':
			return not run(p[1])
			
		elif p[0] == '->':
			env[p[1]] = run(p[2])
		
		elif p[0] == 'var':
			if p[1] not in env:
				print('NameError: Variable "'+p[1]+'" not found!')
				quit()
			else:
				return env[p[1]]
		
		elif p[0] == 'input':
			return input(run(p[1]))
			
		elif p[0] == 'toint':
			try:
				return int(run(p[1]))
			except ValueError:
				print('ValueError: Value "'+ p[1] +'" can not be converted to int!')
				quit()
				
		elif p[0] == 'fun':
			funs[p[1]] = p[2]
			funs_ret[p[1]] = p[3]
			
		elif p[0] == 'call':
			run(funs[p[1]])
			return run(funs_ret[p[1]])
			
		elif p[0] == 'if':
			if run(p[1]):
				return run(p[2])
			else:
				return None
		
		elif p[0] == 'if-else':
			if run(p[1]):
				return run(p[2])
			else:
				return run(p[3])
				
		elif p[0] == 'loop':
			for iterator in range(p[1]):
				run(p[2])
			return
			
	elif type(p) == list:
		try:
			return_list = []
			for i in p:
				return_list.append(run(i))
			return return_list
		except (IndexError, TypeError, KeyError) as e:
			return p
			
	else:
		return p
	
def p_run(p):
	'run : blocks'
	run(p[1])
	
def p_blocks(p):
	'''
	blocks : block
		   | blocks block
	'''
	if len(p) == 2:
		p[0] = [p[1]]
	else:
		p[1].append(p[2])
		p[0] = p[1]
		
def p_block(p):
	'''
	block : expression LEND
		  | input LEND
		  | var_assign LEND
		  | log_block LEND
		  | if_statement
		  | fun
		  | 
	'''
	try:
		p[0] = p[1]
	except IndexError:
		p[0] = None
		
def p_log(p):
	'''
	log_block : LOG LPAREN STRING RPAREN
			  | LOG LPAREN expression RPAREN
			  | LOG LPAREN input RPAREN
	'''
	p[0] = ('log', p[3])
	
def p_ifstatement(p):
	'if_statement : IF LPAREN expression RPAREN LBRKT blocks RBRKT'
	p[0] = ('if', p[3], p[6])
	
def p_ifelsestatement(p):
	'if_statement : IF LPAREN expression RPAREN LBRKT blocks RBRKT OWISE LBRKT blocks RBRKT'
	p[0] = ('if-else', p[3], p[6], p[10])
	
def p_fun_dec(p):
	'fun : FUN LPAREN NAME RPAREN LPAREN expression RPAREN LBRKT blocks RBRKT'
	p[0] = ('fun', p[3], p[9], p[6])
	
def p_loop(p):
	'block : LOOP LPAREN expression RPAREN LBRKT blocks RBRKT'
	p[0] = ('loop', p[3], p[6])

def p_var_assign(p):
	'''
	var_assign : NAME ASSIGN expression
			   | NAME ASSIGN STRING
			   | NAME ASSIGN input
	'''
	p[0] = ('->', p[1], p[3])
	
def p_expression(p):
	'''
	expression : expression POW expression
			   | expression MULT expression
			   | expression DIVIDE expression
			   | expression MOD expression
			   | expression PLUS expression
			   | expression MINUS expression
	'''
	p[0] = (p[2], p[1], p[3])

def p_expression_int_bool(p):
	'''
	expression : INT
			   | boolean
			   | STRING
	'''
	p[0] = p[1]
	
def p_bool(p):
	'''
	boolean : TRUE
			| FALSE
	'''
	p[0] = p[1]
	
def p_bool_ops(p):
	'''
	boolean : expression EQ expression
			| expression NEQ expression
			| expression MT expression
			| expression LT expression
			| expression AND expression
			| expression OR expression
	'''
	p[0] = (p[2], p[1], p[3])
	
def p_not_bool(p):
	'boolean : NOT expression'
	p[0] = (p[1], p[2])
	
def p_expression_var(p):
	'expression : NAME'
	p[0] = ('var', p[1])
	
def p_input(p):
	'input : INPUT LPAREN expression RPAREN'
	p[0] = ('input', p[3])
	
def p_toint(p):
	'expression : TOINT LPAREN expression RPAREN'
	p[0] = ('toint', p[3])
	
def p_call(p):
	'expression : LPAREN NAME RPAREN'
	p[0] = ('call', p[2])

def p_error(p):
	if p is not None:
		print("SyntaxError: Illegal use of token '%s' found!" % p.value)
	else:
		print("SyntaxError: Unexpected end of input!")
	quit()

parser = yacc.yacc()

def execute(file):
	parser.parse(file)
