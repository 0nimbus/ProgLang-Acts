%{
#include "calc.tab.h"
void yyerror(char *);
%}

%%

[0-9]+      { printf("\033[0;36m[NUMBER] %s\033[0m\n", yytext); yylval = atoi(yytext); return NUMBER; }
[a-zA-Z]+   { printf("\033[0;35m[IDENTIFIER] %s\033[0m\n", yytext); return IDENTIFIER; }
"+"         { printf("\033[0;33m[OPERATOR] +\033[0m\n"); return '+'; }
"-"         { printf("\033[0;33m[OPERATOR] -\033[0m\n"); return '-'; }
"*"         { printf("\033[0;33m[OPERATOR] *\033[0m\n"); return '*'; }
"/"         { printf("\033[0;33m[OPERATOR] /\033[0m\n"); return '/'; }
"("         { printf("\033[0;32m[PAREN] (\033[0m\n"); return '('; }
")"         { printf("\033[0;32m[PAREN] )\033[0m\n"); return ')'; }
\n          { return '\n'; }
[ \t]       ;
.           { printf("\033[0;31m[INVALID] %s\033[0m\n", yytext); yyerror("Invalid character"); }

%%

int yywrap(void) { return 1; }