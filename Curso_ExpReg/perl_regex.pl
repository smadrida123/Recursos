#!/usr/bin/perl
use strict;
use warnings;
my $t=time;

open(my $f,"<./results.csv") or die ("no hay archivo");
my $match=0;
my $nomatch=0;
#formato archivo
# 2018-06-04,Slovakia,Morocco,1,2,Friendly,Geneva,Switzerland,TRUE
while (<$f>) {
 chomp;
#en perl cualquier expresion regular va con /expresion regular/. m= funcion match 
#ej todos los partidos en febrero ^[\d]{4,4}\-02\-.*$
#ej veces que ganaron los visitantes
 if(m/^([\d]{4,4}).*?,(.*?),(.*?),(\d+),(\d+),.*$/) {
   if($4<$5) {
    printf("%s:%s (%d) - (%d) %s\n",$1,$2,$4,$5,$3);
   $match++;
   }
 } else{
   $nomatch++;
 }
}

close($f);
printf("se encontraron \n -%d matches\n -%d no matches\n tardo %d segundos",$match,$nomatch,time()-$t);