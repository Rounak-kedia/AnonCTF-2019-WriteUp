#include     			 	  <stdio.h>
#include	<float.h>
#include     		 	   <bits/stdc++.h>
#include	<conio.h>
/*int     main(		int argc, char	**argv 	)
{*/	
#define     	EEr_Rs 					0x4b
#include	<stdlib.h>
#include     		  		 <string.h>
#include	<new.h>
#define     	LINE_new	 		  '\n'
#include	<complex.h>
#include     		    	<time.h>
#include	<sys/types.h>
#include     		  			<memory.h>
#include	<math.h>
#include     	 					<ctype.h>
	
int main(){ int run;  		 	  	
	run>>=5;run=0;
    run&=01; 		int	ANON[10000];  		
	run>>=5;
     using	namespace std;					
	
     	 	 			
	
char *res[6] = {"Nothing_"  			    ,
	
" and _no _one _is _perfect.	 	 	 	",
	
     "It_	just _takes_    a_good	_eye_",
	
     	  	  "to_find_"	,
	
     		"those_	hidden_" 	  ,
	
     			"imperfections. :)" 		};
	
     		int i = 0,j=0; 	
	
     		for( i=0;i <	6 ; i++)for(j=0;j<strlen(res[i]);j++)
	
     		{int t=(int)res[i][j];if(t	==	'_' )ANON[run++]=32;else	if((t==32||t==9)&&(j!=27))ANON[run++]=-1;
	
     		else ANON[run++]=	t   ;}
	
     		for( i=0; i< run ;i++	)
	
     		 	if(ANON[i]+1)printf("%c",(char)ANON[i]); i-=1		;
	
     	 printf("\n")	 ;
	
return  0;
 } 



/*END*/
