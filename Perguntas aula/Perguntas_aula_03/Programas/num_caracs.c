#include <stdio.h>
#include <stdlib.h>

int Num_Caracs(char *string)
{
int i;
for(i = 0; string[i]!= '\0'; i++){
	}
return i;
}

int main(){

char nome[30];
scanf("%s", nome);
int i = Num_Caracs(nome);
printf("quantidade: %d \n", i);
return 0;
} 
