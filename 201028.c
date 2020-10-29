#include <stdio.h>
#pragma warning( disable : 4996)
#include <stdlib.h>
#include <string.h>
#include <time.h>


int choiceLevel(void); //게임의 레벨을 입력받아 정할 수 있도록 하는 함수
char* makeAnswer(int len); //게임의 렌덤 정답 값을 만들어내는 함수
void StartGame(void);//게임의 몸통이 되는 함수

int main(int argc, char ** argv) 
{
	StartGame();
}


void StartGame(void) {//게임의 몸통이 되는 함수
	int len = 0;
	char* gameAnswer;

	puts("==========Game Start!==========\n");

	len = choiceLevel();
	gameAnswer = makeAnswer(len);
	for (int i = 0; i < len; i++) {
		printf("%d", gameAnswer[i]);
	}
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

	char* Answer = (char*)malloc(sizeof(char)*len); // 정답을 한 숫자씩 받아주는 배열
	memset(Answer, 0, sizeof(char) * len); // Answer 초기화
	
	for (int i = 0; i < len; i++) {
 		char overlap = 0; 
		srand((unsigned int)time(NULL));//랜덤으로 받아주도록 설정
		Answer[i] = (char)(rand() % 10 + (int)'0');
	//	printf("%c", Answer[i]);

		if (i = 0){
			if(Answer[i] == '0') {
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

	return Answer; //힙영역의 메모리의 주소값을 리턴한다.
}

int userInput(int len) { //유저가 숫자를 입력하게 한다.
		char* userAnswer = (char*)malloc(sizeof(char)*len);
		memset(userAnswer, 0,sizeof(char)*len);

		printf("숫자 %d개를 입력해주세요", len);
		scanf(userAnswer);
		
		for(int i = 0; i < len; i ++){
			if(userAnswer[i] == )
		}
}

