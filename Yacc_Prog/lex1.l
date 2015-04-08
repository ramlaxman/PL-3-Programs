%option reentrant
%option bison-bridge
%option noyywrap
%option bison-locations
%{
  #include "parser.h"

%}

%%


"(" { return (LPAREN); }
")" { return (RPAREN); }
\n {return(N);}
.|[ \t]+   { }
%%

