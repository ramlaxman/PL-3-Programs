%define api.pure true
%locations
%token-table
%glr-parser
%lex-param {void *scanner}
%parse-param {void *scanner}

%{
/* your top code here */
#include<omp.h>
int t;
%}

%token LPAREN
%token RPAREN
%token N

%%

document  : 
   	  | document exprs N {printf("\n successful parsing by thread ID=%d\n",omp_get_thread_num()); } 
;
exprs
    :
    | expr exprs
;
expr
    : parens
;
parens
    : LPAREN exprs RPAREN
;

%%

int yyerror() {
    printf("\nparse error: thread ID=%d\n",omp_get_thread_num());

}
