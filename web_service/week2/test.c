#include <stdio.h>
int main(){
FILE *f1, *f2;
char c;
// echo File : a.txt
printf("File : a.txt\n");

// cat a.txt
f1 = fopen("a.txt", "r");
while((c = getc(f1)) != EOF)
    printf("%c", c);
fclose(f1);

// echo ----- end of a.txt
printf("----- end of a.txt\n");

// echo Copy a.txt to b.txt
printf("Copy a.txt to b.txt\n");

// cat a.txt > b.txt
f1 = fopen("a.txt", "r");
f2 = fopen("b.txt", "w");
while((c = getc(f1)) != EOF)
    fputc((int)c,f2);
fclose(f2);
fclose(f1);

// echo File: b.txt
printf("File: b.txt\n");

// cat b.txt
f1 = fopen("b.txt", "r");
while((c = getc(f1)) != EOF)
    printf("%c", c);
fclose(f1);

// echo ----- end of b.txt
printf("----- end of b.txt\n");

return 0;
}