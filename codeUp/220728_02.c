#include <stdio.h>
/* 
    1. printf
    2. if
    3. 함수
*/
void printMessage(int n);

int main(){
    int a = 9;
    printf("일반 문자열\n");
    printf("%d\n",a);
    if (a<11) {
        printf("11보다 작음\n");
        //print("11보다 작음\n"); 작성 불가능
    } 
    else {
        printf("11보다 큼\n");
    }
    printMessage(a);

    return 0;
}

void printMessage(int n){ //if문에 대괄호가 없어도 된다.
    if (n>9)
        printf("9보다 크다.\n");
    else if (n==9)
        printf("9와 같다.\n");
    else
        printf("9보다 작다.\n");
}