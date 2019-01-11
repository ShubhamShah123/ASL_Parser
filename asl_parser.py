#---------#---------#---------#---------#---------#--------#
import ply.yacc
import ply.lex

from ParseTree import *
import sys

#---------#---------#---------#---------#---------#--------#
tokens = [ 'IDENTIFIER', 'INTEGER', 'REAL', 'STRING', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'ASSIGN', 'AT', 'COLON', 'COMMA', 'EQ', 'GE', 'GT',
'LPAREN', 'RPAREN', 'LBRACE', 'LBRACKET', 'LT', 'LE', 'NE', 'PERIOD', 'PTR', 'RBRACE', 'RBRACKET', 'SEMICOLON']

reserved = {
    'while' : 'WHILE', 'then' : 'THEN', 'and' : 'AND', 'by' : 'BY', 'const' : 'CONST', 'div' : 'DIV', 'do' : 'DO', 'elif' : 'ELIF', 'else' : 'ELSE',
    'exit' : 'EXIT', 'extends' : 'EXTENDS', 'for' : 'FOR', 'func' : 'FUNC', 'if' : 'IF', 'loop' : 'LOOP', 'mod' : 'MOD', 'next' : 'NEXT', 'not' : 'NOT',
    'of' : 'OF', 'or' : 'OR', 'read' : 'READ', 'record' : 'RECORD', 'return' : 'RETURN', 'to' : 'TO', 'var' : 'VAR', 'write' : 'WRITE',
    'null' : 'NULL'
}

tokens += reserved.values()

t_ignore = ' \f\r\t\v'
t_REAL = r'(\d+)[.](\d+)([eE][+-]?\d+)?'
t_INTEGER = r'\d+'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_ASSIGN = r'='
t_AT = r'@'
t_COLON = r':'
t_COMMA = r','
t_EQ = r'=='
t_GE = r'>='
t_GT = r'>'
t_LE = r'<='
t_LT = r'<'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_PERIOD = r'\.'
t_PTR = r'\->'
t_SEMICOLON = r';'


def t_IDENTIFIER( t ) :
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
  return t

def t_STRING( t ):
  r'["][ a-zA-Z0-9:]*["]'
  return t

def t_comment(t):
  r'//[^\n]*'
  pass

def t_newline( t ) :
  r'\n+'
  t.lexer.lineno += t.value.count( '\n' )

def t_error( t ) :
  print( f'Illegal character "{t.value[0]}", line {t.lineno}.' )
  t.lexer.skip( 1 )

  raise ValueError( 'Lexical error' )

#---------#---------#---------#---------#---------#--------#
# TODO: Put your ASL ply parser routines here.

# Below are a few sample kinds of parser routines to give
# you an idea of how your routines could be structured.

start = 'program'

def p_program( p ) :
  r'program : block'
  p[0] = PT_Program( p[1] )

def p_block( p ) :
  r'block : LBRACE block_items RBRACE'
  p[0] = PT_Block( p[2] )

def p_block_item( p ):
  r'block_item : statement'
  p[0] =  p[1] 

# --- Block Items ---
def p_block_items_epsilon( p ):
  r'block_items : epsilon'
  p[0] = []

def p_block_items_one( p ):
  r'block_items : block_item'
  p[0] = [p[1]]

def p_block_items_many( p ):
  r'block_items : block_items SEMICOLON block_items'
  p[0] = p[1] + p[3]


def p_LValue_ID( p ):
  r'lvalue : IDENTIFIER'
  p[0] = PT_LValue_ID( p[1] )

def p_LValue_lvalue_exp( p ):
  r'lvalue : lvalue LBRACKET expression RBRACKET'
  p[0] = PT_LValue_Exp( p[1], p[3])

def p_LValue_lvalue_ID( p ):
  r'lvalue : lvalue PERIOD IDENTIFIER'
  p[0] = PT_LValue_Period_Id( p[1], p[3])

def p_Statement_Assign( p ):
  'statement : lvalue ASSIGN expression'
  p[0] = PT_Statement_Assign(p[1] , p[3])


# --- Statement: WRITE ---
def p_Statement_write( p ):
  'statement : WRITE LPAREN expressions RPAREN'
  p[0] = PT_Statement_Write( p[3] )

# --- Literals ----

def p_Literal_Real(p):
  r'literal : REAL'
  p[0] =  PT_Expression_Literal('REAL', p[1])

def p_Literal_Int(p):
  r'literal : INTEGER'
  p[0] =  PT_Expression_Literal('INTEGER', p[1])

def p_Literal_String(p):
  r'literal : STRING'
  p[0] =  PT_Expression_Literal('STRING', p[1])

# --- Record Init ---
def p_record_init_id( p ):
  r'record_init : IDENTIFIER ASSIGN expression'
  p[0] = PT_Statement_Assign(p[1], p[3])

def p_record_init_one( p ):
  r'record_inits : record_init'
  p[0] = p[1]

def p_record_init_many( p ):
  r'record_inits : record_init COMMA record_init'
  p[0] = p[1] + p[3] 

# --- Array Init ----
def p_array_init_expr_one( p ):
  r'array_init : LBRACKET expression OF RBRACKET expression'
  p[0] = PT_Array_Init(p[2], p[5])

# --- Expressions ---
def p_expressions_epsilon( p ):
  r'expressions : epsilon'
  p[0] = []

def p_expressions_one( p ):
  r'expressions : expression'
  p[0] = [ p[1] ]

def p_expressions_many( p ):
  r'expressions : expressions COMMA expression'
  # p[0] = p[1] + p[3]
  p[1].append(p[3])
  p[0] = p[1]

# --- Expression Productions ---


def p_expression_expression( p ):
  r'expression : LPAREN expression RPAREN'
  p[0] = PT_Expression_LValue( p[2] )

def p_expression_expressions( p ):
  r'expression : expression LPAREN expressions RPAREN'
  p[0] = p[1] + p[3]

def p_expression_lvalue( p ):
  r'expression : lvalue'
  p[0] = PT_Expression_LValue( p[1] )

def p_expression_literal( p ):
  r'expression : literal'
  p[0] = p[1]

def p_unary_op_minus( p ):
  r'unary_op : MINUS'
  p[0] = PT_Unary_Op_Minus( p[1] )

def p_unary_op_not( p ):
  r'unary_op : NOT'
  p[0] = PT_Unary_Op_Not( p[1] )

def p_expression_unaryop( p ):
  r'expression : unary_op expression'
  p[0] = PT_Expression_UnaryOp(p[1], p[2])

# --- Type Expr ---
def p_type_expr_id( p ):
  r'type_expr : IDENTIFIER'
  p[0] = p[1]

def p_type_expr_Axpr( p ): 
  r'type_expr : AT type_expr'
  p[0] = PT_TypeExpr(p[2])




def p_header( p ) :
  'header : INTEGER'
  p[0] = PT_Header( p[1] )

def p_footer( p ) :
  'footer : IDENTIFIER'
  p[0] = PT_Footer( p[1] )


# --- Error Production ---
def p_error( p ) :
  print("[ERROR]: ",p)
  if p is None :
    print( 'Syntax error!' )

  else :
    print( f'Syntax error at "{p.value}", line {p.lineno}' )

  raise ValueError( 'Syntactic error' )

# -------------------------

# --- Epsilon Production ---
def p_epsilon( p ):
  r'epsilon :'
  p[0] = None

#---------#---------#---------#---------#---------#--------#
def _main( inputFile ) :
  with open( inputFile, 'r' ) as fp :
    data = fp.read()
  name = inputFile.split('.')[0]
  ext = inputFile.split('.')[1]
  file_name = name + '.parse'
  cg_file_name = name + '.s'
  open(file_name, 'w').close()
  
  try :
    _  = ply.lex.lex()
    parser = ply.yacc.yacc()
    value = parser.parse( data )

    print( "---- PARSING ----" )
    value.dump(file_name)

    print("---- SEMANTIC CHECK -----")
    value.semantic_check(file_name)

    print("---- CODE GEN  ---")
    value.code_gen(cg_file_name)
    
  except ValueError :
    print( 'Error during processing.  Abort.' )

#---------#---------#---------#
if __name__ == '__main__' :
  import sys

  if len( sys.argv ) > 1 :
    _main( sys.argv[ 1 ] )

  else :
    print( 'Input file name required.' )

#---------#---------#---------#---------#---------#--------#
