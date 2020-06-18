#include<stdio.h>
#include<stdlib.h>

int main(){
	srand(0x7e3);
	for(int i = 0; i < 1000; i++){
		int r = rand()%3;
		if(r == 0)
			printf("p\n");
		if(r == 1)
			printf("r\n");
		if(r == 2)
			printf("s\n");
	}
	printf("\n");
}
