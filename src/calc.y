%{
#include <stdio.h>
int yylex(void);
void yyerror(char *);
%}

%token NUMBER IDENTIFIER
%left '+' '-'
%left '*' '/'
%left IMPLICIT_MULT

%%

input:    /* empty */
        | input line
;

line:     '\n'       { printf("\033[1;32m=> Valid expression\033[0m\n"); }
        | exp '\n'   { printf("\033[1;32m=> Valid expression\033[0m\n"); }
        | error '\n' { yyclearin; printf("\033[1;31m=> Recovered from error\033[0m\n"); }
;

exp:      NUMBER
        | IDENTIFIER
        | exp '+' exp
        | exp '-' exp
        | exp '*' exp
        | exp '/' exp { if($3 == 0) yyerror("Division by zero"); }
        | '(' exp ')'
        | exp exp %prec IMPLICIT_MULT
;

%%

void yyerror(char *s) {
    extern char *yytext;
    fprintf(stderr, "\033[1;31mERROR:\033[0m %s at '\033[1;33m%s\033[0m'\n", s, yytext);
}

int main() {
    printf("\033[1;34mEnter expressions (Ctrl+D to exit):\033[0m\n");
    yyparse();
    return 0;
}