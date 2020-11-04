#include <stdio.h>
#pragma warning( disable : 4996)
#include <stdlib.h>
#include <string.h>
#include <time.h>


void StartGame(void);//게임의 몸통이 되는 함수
int choiceLevel(void); //게임의 레벨을 입력받아 정할 수 있도록 하는 함수
char* makeAnswer(int len); //게임의 렌덤 정답 값을 만들어내는 함수
char* userInput(int len, int* cnt); //유저가 숫자를 입력하게 한다
int checkInput(char* user, int len);//입력받는 값을 체크해준다
void compareAnswer(char* Ans, char* inpans, int len);//유저에게 입력받은 숫자와 게임의 정답 비교



int main(int argc, char** argv)
{
	StartGame();
}


void StartGame(void) {//게임의 몸통이 되는 함수
	int len = 0;
	int cnt = 0;
	char* gameAnswer;
	char* inputAnswer;

	puts("==========Game Start!==========\n");

	len = choiceLevel();
	gameAnswer = makeAnswer(len);

	//printf("!!!!!!!!!!!!!!!!!!!!!!!!!!11%s", gameAnswer);

	while (1) {
		
		inputAnswer = userInput(len, &cnt);

		compareAnswer(gameAnswer, inputAnswer, len);
		if (gameAnswer == inputAnswer) {
			break;
		}
	}

	puts("========게임이 완료되었습니다========");
	printf("%d번 만에 맞추셨습니다", cnt);
}

int choiceLevel(void) { //게임의 레벨을 입력받아 정할 수 있도록 하는 함수
	int len_Answer = 0;

	puts("레벨을 입력해 주세요\n");
	printf("1. Easy\n2. Nomal\n3. Hard \n\t\t\tlevel : ");//1 = 3자릿수, 2 = 4자릿수, 3 = 5자릿수
	scanf("%d", &len_Answer);

	len_Answer += 2;//자릿수를 나타내려고 +2

	return len_Answer;
}

char* makeAnswer(int len) { //게임의 렌덤 정답 값을 만들어내는 함수

	char* Answer = (char*)malloc(sizeof(char) * len); // 정답을 한 숫자씩 받아주는 배열
	memset(Answer, 0, sizeof(char) * len); // Answer 초기화

	for (int i = 0; i < len; i++) {
		char overlap = 0;
		srand((unsigned int)time(NULL));//랜덤으로 받아주도록 설정
		Answer[i] = (char)(rand() % 10 + (int)'0');
			//printf("생성된 정답 %c", Answer[i]);

		if (i == 0) {
			if (Answer[i] == '0') {
				i--;
				continue;
			}
		}

		if (i != 0) {
			for (int j = 0; j < i; j++) {
				if (Answer[i] == Answer[j]) {
					overlap++;
				}
			}
			if (overlap == 1) {
				i--;
				continue;
			}
		}

	}

	return Answer; //힙영역의 메모리의 주소값을 리턴한다
}

char* userInput(int len, int* cnt) { //유저가 숫자를 입력하게 한다
	int check = 0;

	char* userAnswer = (char*)malloc(sizeof(char) * len);
	memset(userAnswer, 0, sizeof(char) * len);

	while (1) {
		printf("숫자 %d개를 입력해주세요", len);
		scanf("%s", userAnswer);
		cnt++;
		check = checkInput(userAnswer, len);

		if (check == -1) {//입력받은 값이 첫번째자리가 0이거나 겹치는 숫자가 있으면 -1을 리턴한다
			memset(userAnswer, 0, sizeof(char) * len);
			cnt--;
			continue;// -1이라면 다시 값을 받도록한다
		}
		else {
			break;
		}
	}
	return userAnswer;
}

int checkInput(char* user, int len) {//입력받는 값을 체크해준다
	int returnNum = 0;

	for (int i = 0; i < len; i++) {
		int faile = 0;

		if (i == 0) {
			if (user[i] == '0') {
				faile++;
			}
		}
		else {
			for (int j = 0; j < i; j++) {
				if (user[i] == user[j]) {
					faile++;
				}
			}
		}
		if (faile == 1) {
			returnNum = -1;
			break;
		}
		break;
	}
	return returnNum;
}

void compareAnswer(char* Ans, char* inpans, int len) {//유저에게 입력받은 숫자와 게임의 정답 비교
	int strike = 0;
	int ball = 0;

	for (int i = 0; i < len; i++) {
		for (int j = 0; j < len; j++) {
			if (Ans[i] == inpans[j]) {
				if (i == j) {
					strike++;
				}
				else {
					ball++;
				}
			}
		}
	}
	if (strike == len) {
		printf("%10d strike", strike);
		puts("==========CLEAR!=========");
	}

	printf("[%s] '%d'strike / '%d'ball\n", Ans, strike, ball);
}
