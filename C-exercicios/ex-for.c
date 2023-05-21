#include <stdio.h>

int main() {
   int n, i;
   
   printf("Digite um numero inteiro: ");
   scanf("%d", &n);

   printf("Os números entre 1 e %d são:\n", n);
   for (i=1;i<=n;i++){
      printf("%d\n",i);
   }
   return 0;
}
