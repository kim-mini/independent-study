#include <stdio.h>
#pragma warning(disable:4996)
#include <stdlib.h>
#include <string.h>
#include<time.h>



int get_answer(int n);


main() {
	int num = 150;
	int m = get_answer(num);
	printf("%d", m);
}

int get_answer(int n) {
	int num[10] = { 0, };
	int n1 = n;
	int n2 = n;
	int cnt = 0;
	int answer = 0;


	for (int i = 0; n2 != 0; i++) {//10진수 -> 3진수로 변환한 값 구하기

		num[i] = n1 % 3;
		n2 /= 3;
		n1 = n2;
		cnt++;

	}
	int ll = cnt;

	int result = 1;

	for (int j = 0; j < cnt; j++) {//num의 인덱스

		for (int i = ll - 1; i > 0; i--) {//3의n승을 표현하기 위해
			result *= 3;
		}
		num[j] *= result;
		result = 1;
		ll--;
	}



	for (int i = 0; i < cnt; i++)//3진수를 모두 더한다
	{
		answer += num[i];
	}
	return answer;
}
