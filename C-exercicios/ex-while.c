#include <stdio.h>

int main() {
    int i;
    i = 0;
    while (i<100){
        i++;
        printf("%d ",i);
        if(i%10 == 0){
            printf("\n");
        }
    }
    return 0;
}
