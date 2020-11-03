#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

main(void)
{
    int n = 0;
    int ans = 0;

    printf("정수를 입력해주세요 : ");
    scanf("%d", &n);
    ans = get_answer(n);
    printf("%d의 약수들의 합은 %d입니다.", n, ans);
    return 0;
}


int get_answer(int n) {// 약수구하기
    int answer = 0;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            answer += i;
        }
    }
    return answer;
}
