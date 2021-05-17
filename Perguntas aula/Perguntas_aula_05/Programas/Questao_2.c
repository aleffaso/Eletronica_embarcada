#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, const char * argv[])
{
	int fp, i,j;
	char nome[100];
	char idade[100];

	fp = open ("%c.txt", O_WRONLY | O_CREAT, S_IRWXU);

	if(fp==-1)
	{
		printf ("Erro na abertura do arquivo.\n");
		exit (1);
	}	
	printf("Digite seu nome: ");
	gets(nome);
	for(i=0; nome[i]; i++)
	write(fp, &(nome[i]), 1);
	write(fp, "\n", 1);
	
	printf("Digite sua idade: ");
	gets(idade);
	for(j=0; idade[j]; j++)
	write(fp, &(idade[i]), 1);	
	write(fp, "\n", 1);

	close(fp);
	return 0;
}