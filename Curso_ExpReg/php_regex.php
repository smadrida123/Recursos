<?php
$file=fopen("./results.csv","r");
$match=0;
$nomatch=0;
$t=time();

#while not(!) in the file (feof) of file
#preg_match('EXPRESION REGULAR',CADENA DE CARACTERES,$m)

#ej traer todos los empates en la historia
# 2018-01-30,Jamaica,Korea Republic,2,2,Friendly,Antalya,Turkey,TRUE ejemplo formato
while(!feof($file)){
    $line=fgets($file);
    if(preg_match(
       '/^(\d{4}.*?),(.+),(.+),(\d+),(\d+),.*$/i',
       $line,
       $m
      )
    ){
      if($m[4]==$m[5]){
        printf("empate:%s: %s,%s [%d-%d]\n",$m[1],$m[2],$m[3],$m[4],$m[5]);
      } elseif ($m[4]>$m[5]){
        echo "local\n";
      }  else{
        echo "visitante\n";
      }
      #print_r($m);
      $match++;
    } else {
      $nomatch++;
    }
}
fclose($file);

printf("\n\nmatch %d\nnomatch %d\n",$match,$nomatch);
printf("tiempo en segundos: %d\n",time()-$t);