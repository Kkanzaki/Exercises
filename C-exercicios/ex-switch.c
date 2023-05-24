#include <stdio.h>

int main() {
    char op;
    double a,c,total;
    printf("Digite o primeiro número:\n");
    scanf("%lf",&a);
    printf("Digite o segundo numero:\n");
    scanf("%lf",&c);
    printf("Digite o operador desejado:\n");
    scanf(" %c",&op);
    
    switch(op){
        case '+':
            total = a+c;
            printf("%.2lf",total);
            break;
        case '-':
            total = a-c;
            printf("%.2lf",total);
            break;
        case '*':
            total = a*c;
            printf("%.2lf",total);
            break;
        case '/':
            if (c == 0){
                printf("Impossível dividir por zero");
            }
            else {
                total = a/c;
                printf("%.2lf",total);
            }
            break;
        default:
            printf("Impossível Calcular");
    }
}
