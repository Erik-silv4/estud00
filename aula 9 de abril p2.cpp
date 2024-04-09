#include <stdio.h>
#include <locale.h>

struct{
	char nome[20], esporte[20];
	int idade;
	float peso;
	double altura;
}Atleta;

int main(){
	setlocale(LC_ALL, "Portuguese");
	
	printf("-------------------------------------------------------------------------\n");
	printf("|\t\t\t\t\t\t\t\t\t|\n");
	printf("|\t\t\tMenu do Atlerta\t\t\t\t\t|\n");
	printf("|\t\t\t\t\t\t\t\t\t|\n");
	printf("-------------------------------------------------------------------------\n\n");
	printf("Digite seu nome: ");
	gets(Atleta.nome);
	printf("\nDitite sua idade: ");
	scanf("%d", &Atleta.idade);
	printf("\nDigite seu peso: ");
	scanf("%f", &Atleta.peso);
	printf("\nDigite sua altura: ");
	scanf("%lf", &Atleta.altura);
	
	printf("\n\n-------------------------------------------------------------------------\n");
	printf("|\t\t\t\t\t\t\t\t\t|\n");
	printf("|\t\t\tInformaçôes do Atlerta\t\t\t\t|\n");
	printf("|\t\t\t\t\t\t\t\t\t|\n");
	printf("|\tNome: %s\t\t\t\t\t\t\t|\n", Atleta.nome);
	printf("|\tIdade: %d\t\t\t\t\t\t\t|\n", Atleta.idade);
	printf("|\tPeso: %1.f\t\t\t\t\t\t\t|\n", Atleta.peso);
	printf("|\tAltura: %2.lf\t\t\t\t\t\t\t|\n", Atleta.altura);
	printf("-------------------------------------------------------------------------");

	return 0;
}
