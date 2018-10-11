// Single-line comment
typedef double[15] vetor;
/**** Multi
	  line
	  comment
	  			****/
typedef struct al {
	float nota1, nota2;
} aluno;

int A, B, C, D;
vetor E;
aluno F;

int fatorial(int a;){
	int i, result;
	i = 1;
	result = 1;
	while (i < a) {
		result = result*i;
		i = i + 1;
	};
 	return result;
}

float exp(float a, b;){
	int i;
	float result;
	i = 1;
	result = a;
	if (b == 0) {
		result = 1;
	} else {
		while (i < b){
			result = a * a;
			i = i + 1;
		};
	};
	return result;
}

double maior(vetor a;){
	int i;
	double result;
	i = 0;
	result = a[0];
	while (i < 15){
		if (a[i] > result) {
			result = a[i];
		};
	};
	return result;
}

aluno lerDados(){
	aluno result;
	printf("digite as notas do aluno");
	scanf(result.nota1);
	scanf(result.nota2);
	return result;
}

int main(){
	A = 10.0;
	B = fatorial(A);
	C = exp(A,B);
	D = maior(E);
}