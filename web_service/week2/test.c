#include <stdio.h>
int main(){
    int count = 2;
    int hap = 0;
    switch (++count) {
        case 1: hap = hap + count++;
        case 2: hap = hap + count++;
        case 3: hap = hap + count++;
        case 4: hap = hap + count++;
        case 5: hap = hap + count++;
    }
    printf("hap의 값: %d \n", hap);
    return 0;
}

