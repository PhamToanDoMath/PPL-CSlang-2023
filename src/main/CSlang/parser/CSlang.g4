grammar CSlang;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

// 3.4: Keywords
BREAK:'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
FOR: 'for';
TRUE: 'true';
FALSE: 'false';
BOOLEAN: 'bool';
INT: 'int';
FLOAT: 'float';
STRING: 'string';
RETURN: 'return';
NULL: 'null';
CLASS: 'class';
SELF: 'self';
VAR: 'var';
CONST: 'const';
VOID: 'void';
CONSTRUCTOR: 'constructor';
SUPER: 'super';

// 3.5: Operators
NEW: 'new';
ADD: '+' ;
SUB: '-' ;
MUL: '*' ;
DIV: '/' ;
DSLASH: '\\';
PERCENT: '%';
NOT: '!';
AND: '&&';
OR: '||' ;
NOT_EQUALOP: '!=';
EQUALOP: '==';
EQUAL: '=';
LESS_THAN: '<';
LESS_OR_EQUAL_THAN: '<=';
GREATER_THAN: '>';
GREATER_OR_EQUAL_THAN: '>=';
ASSIGNMENT_OP: ':=';
STRING_CONCAT : '^';
EXTEND: '<-';

// 3.6: Separtors
CM: ',';
DOT: '.';
LB: '(';
RB: ')';
LP: '{';
RP: '}';
LS: '[';
RS: ']';
SEMI: ';';
COLON: ':';

// 3.1 Charaters set
WS : [ \t\b\f\r\n]+ -> skip ; // skip spaces, tabs, newlines, backspace, form feed, carriage return

//3.2 Comments
COMMENT_BLOCK: ([/][*] .*? [*][/]) -> skip;
COMMENT_LINE: ([/][/] .*? ([\n] | EOF)) -> skip;

program: classDecl+ EOF;

// 2.1 Class declaration
classDecl: CLASS (idLit EXTEND)? idLit LP classStmtsNullable RP;
constructorDecl: 'func' CONSTRUCTOR listDeclParams blockStmt;
classStmtsNullable: (classStmt)*;
classStmt:  attributeStmt| methodDecl | constructorDecl;
attributeStmt: varDeclStmt | valDeclStmt;
// 2.3 Method declaration
singleDeclParam: idLit COLON varType;
declParams: listIds COLON varType;
listDeclParams: LB  (declParams | ((declParams CM)+ singleDeclParam))? RB;
methodDecl: 'func' mixedId listDeclParams COLON varType blockStmt;

// 3.3 Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;
STATIC_ID: [@][a-zA-Z0-9_]+;
idLit: ID;
staticId: STATIC_ID;
mixedId: idLit | staticId;

// 3.7 Literals
literal
	: INTLIT | FLOATLIT | booleanLit | STRINGLIT
	| indexedArrayLit
	;
variableLit: mixedId | staticMemberAccess | memberAccess | indexOperator;
indexedArrayLit: LS listExps RS;
nullLit : NULL;
selfLit : SELF;

INTLIT: [0-9]+;
booleanLit: TRUE | FALSE;

fragment EXPONENT: [eE] (ADD | SUB)? INTLIT ;
fragment DECIMAL: DOT INTLIT;
FLOATLIT
	: INTLIT DECIMAL EXPONENT
	| INTLIT DECIMAL
	| INTLIT EXPONENT
	;

//4.1 Data types
primitiveType
	: INT
	| FLOAT
	| STRING
	| BOOLEAN
	;


classType: idLit;

varType
	: primitiveType
	| arrayType
	| classType
	| VOID
	;

// 4.2 Array type
arrayType: LS INTLIT RS primitiveType;

// 5 Expression
exp: exp (STRING_CONCAT) exp | exp1;
exp1: exp1 ( EQUALOP | NOT_EQUALOP | GREATER_THAN | LESS_THAN | GREATER_OR_EQUAL_THAN | LESS_OR_EQUAL_THAN ) exp1 | exp2;
exp2: exp2 ( OR | AND ) exp3 | exp3;
exp3: exp3 ( ADD | SUB ) exp4 | exp4;
exp4: exp4 ( DIV | MUL | PERCENT | DSLASH) exp5| exp5;
exp5: <assoc=right> (NOT | SUB | ADD) exp5 | operand;

operand: operand LS exp RS | operand1;
operand1: operand1 DOT idLit listParams? | operand2;
operand2: (operand3 DOT)? staticId listParams? | operand3;
operand3: <assoc=right> objectCreation | operand4;
operand4: mixedId | nullLit | selfLit | literal | operand5;
operand5: LB exp RB;

listExps: exp? (CM exp)*;
listExpsNotNull: exp (CM exp)*;
listParams: LB listExps RB;

// 5.5 Index operator
indexOperator: operand LS exp RS;

// 5.6 Member access
memberAccess: operand DOT idLit;
staticMemberAccess: (operand DOT)? staticId;
instanceMethodInvocation: operand DOT idLit listParams;
staticMethodInvocation: (operand DOT)? staticId listParams;

// 5.7 Object creation
objectCreation: NEW idLit listParams;


// 6.1 Variable declare statement
listIds: idLit (CM idLit)*;
listMixedIds: mixedId (CM mixedId)*;
varDeclStmt: VAR (declareWithoutAssign| declareWithAssign) SEMI;
valDeclStmt: CONST (declareWithoutAssign| declareWithAssign) SEMI;

declareWithAssign
	: mixedId COLON varType EQUAL exp
	| mixedId CM declareWithAssign CM exp
	;
declareWithoutAssign: listMixedIds COLON varType ;

// 6.2 Assignment statement
assignStmt: variableLit ASSIGNMENT_OP exp;
assignStmtSemi: assignStmt SEMI;

// 6.3 If statement
ifStmt: IF preStmt? exp blockStmt (ELSE elseStmt)?;
preStmt: blockStmt;
elseStmt: blockStmt;
// 6.4 For statement
forStmt: FOR assignStmt SEMI exp SEMI assignStmt blockStmt;

// 6.5 Break statement
breakStmt: BREAK SEMI;

// 6.6 Continue statement
continueStmt: CONTINUE SEMI;

// 6.7 Return statement
returnStmt: RETURN exp? SEMI;

// 6.8 Method invocation statement
methodInvocationStmt: (staticMethodInvocation| instanceMethodInvocation) SEMI;

// 6.9 Block statement
blockStmt: LP stmts RP;
stmts: (stmt)*;

stmt: varDeclStmt | valDeclStmt | assignStmtSemi 
	| ifStmt | forStmt | breakStmt | continueStmt 
	| returnStmt | methodInvocationStmt | blockStmt
	;

// Exceptions
ERROR_CHAR: .{raise ErrorToken(self.text)};

UNCLOSE_STRING: ["] STR_CHAR* UNCLOSE_CHAR
{
	y = str(self.text)
	raise UncloseString(y[1:])
};
fragment A: [0-9];
fragment ESC_ILLEGAL: [\\] ~[btfrn"\\] ;
fragment SUPPORT_ESC: [\\] [btfrn"\\];
fragment UNCLOSE_CHAR: '\n' | EOF;
ILLEGAL_ESCAPE: ["] STR_CHAR* ESC_ILLEGAL
{
	y = str(self.text)
	raise IllegalEscape(y[1:])
};

fragment STR_CHAR: [a-zA-Z0-9,-.():<>?_=+!@#$%^&*/|;' ] | SUPPORT_ESC;
STRINGLIT: ["] STR_CHAR* ["]{
    self.text = self.text[1:-1]
};