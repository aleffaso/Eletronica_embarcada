#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, const char * argv[])
{
	int fp, i;
	char ola_mundo[100] = "Ola Mundo!";

	fp = open ("exercicio7.txt", O_RDWR | O_CREAT, S_IRWXU);
	if(fp==-1)
	{
		printf ("Erro na abertura do arquivo.\n");
		exit (1);
	}

	for(i=0; ola_mundo[i];i++)
	write(fp, &(ola_mundo[i]), 1);
	write(fp, "\n", 1);
	close(fp);
	return(0);
}