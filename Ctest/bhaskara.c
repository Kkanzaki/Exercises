#include <stdio.h>
#include <math.h>

int main() {
    float a,b,c,delta,x1,x2;

    printf("Insira A: \n");
    scanf("%f",&a);
    printf("Insira B: \n");
    scanf("%f",&b);
    printf("Insira C: \n");
    scanf("%f",&c);
   
   delta=pow(b,2)-4*a*c;

if (delta > 0){
    x1=((-b)+ sqrt(delta))/(2*a);
    x2=((-b)- sqrt(delta))/(2*a);
    printf("O valor do Delta é %.2f\n x1=%.2f e x2=%.2f\n",delta,x1,x2);
}
else if(delta < 0){
    printf("O Delta é negativo\n");
}
}