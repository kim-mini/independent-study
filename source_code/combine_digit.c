#include <stdio.h>
#pragma warning(disable:4996)
#include <stdlib.h>
#include <string.h>
#include<time.h>

int solution(int n);


main() {
	int N = 0;
	int a = 0;

	scanf("%d",&N);

	a = solution(N);
	printf("%d", a);
}

int solution(int n) {
	int answer = 0;
	int num[9] = { (int*)malloc(sizeof(int) * 9) };
	int n2 = n;
	int n3 = n;

	for (int i = 0;i < sizeof(num)/sizeof(int);i++) {
		num[i] = n2 % 10;
		n3 = (n3-num[i])* 0.1;
		n2 = n3;
		
		
	}

	for (int i = 0; i < sizeof(num) / sizeof(num[0]); i++) {
		answer += num[i];
	}
	return answer;
}
