grammar Arithmetic;




// Novas Regras do Parser
program: statement+ ;
statement: assignment | expr | if_statement;
assignment: VAR ASSIGN expr ;

// Regras do Parser
expr: term ( (PLUS | MINUS) term )* ;
term: factor ( (MUL | DIV) factor )* ;
factor: INT | VAR | LPAREN expr RPAREN | TRUE | FALSE;


// Regras do IF
if_statement: IF condition block (ELSE block)?;
block: BEGIN program END;
condition: LPAREN ( boolean_expr | comparison_expr ) RPAREN;
boolean_expr: (boolean (( AND | OR ) boolean)*);
comparison_expr: expr ( GTHAN | LTHAN | EQUALS | NEQUALS ) expr;
boolean: TRUE | FALSE;

// Tokens do IF
TRUE: 'true';
FALSE: 'false';
AND: '&';
OR: '|';
GTHAN: '>';
LTHAN: '<';
EQUALS: '==';
NEQUALS: '!=';
IF: 'if';
ELSE: 'else';



BEGIN: '{';
END: '}';

   
// Novas Regras do Lexer
VAR: [a-zA-Z]+ ;
ASSIGN: '=' ;

// Regras do Lexer
PLUS: '+' ;
MINUS: '-' ;
MUL: '*' ;
DIV: '/' ;
INT: [0-9]+ ;
LPAREN: '(' ;
RPAREN: ')' ;
WS: [ \t\r\n]+ -> skip ;