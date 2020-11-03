#include <stdio.h>
#pragma warning(disable:4996)
#include <stdlib.h>
#include <string.h>
#include<time.h>


//개인 성적 학생성명, 국어, 영어, 수학 세과목의 성적을 입력받는다.
//개인성적입력, 개인성적수정, 전체성적출력, 종료
typedef struct student {
	char name[11];
	int sungjuck[3];
	int all_sung;
	int rank;
}Student;


void modify_info(Student* man, int hms);
void input_info(Student* man, int hms);
void menu(void);
void choice_num(Student* man, int hms);
void view_all(Student* man, int hms);
void all_sung(Student* man, int hms);




int main()
{
	int hms = 0;
	Student* std;

	printf("학생 수를 입력해 주세요 ");
	scanf("%d", &hms);

	//std = (Student*)calloc(hms, sizeof(Student));
	std = (Student*)malloc(sizeof(Student)*hms);//동적메모리 할당
	memset(std, 0, sizeof(Student)*hms);//동적메모리 초기화
	

	choice_num(std, hms);
	free(std);

	return 0;
}//동적할당하면 free를 해놓자



void menu(void) {// 메뉴
	puts("\n☆☆☆☆☆성적보관소☆☆☆☆☆");
	puts("==============================");
	puts("1. 개인 성적입력");
	puts("2. 개인 성적수정");
	puts("3. 전체성적 출력");
	puts("0. 종료");
	puts("==============================\n");
}

void choice_num(Student* man, int hms) {//메뉴 클릭하면 행동발생

	int click = 0;
	


	while (1)
	{
		menu();

		printf("번호를 입력해주세요 ");

		scanf("%d", &click);

		switch (click) {
		case 1:
			input_info(man, hms);
			break;


		case 2:

			modify_info(man, hms);
			break;

		case 3:
			view_all(man, hms);
			break;

		case 0:
			printf("안녕히 가세요");
			break;
		}

		if (click == 0) {
			break;
		}


	}
}

void modify_info(Student* man, int hms) {
	int num = 0;

	for (int i = 0; i < hms; i++) {
		printf("%d번 %s\n", i + 1, man[i].name);
	}
	printf("\n몇번 학생의 정보를 수정하시겠습니까 ");
	scanf("%d", &num);


	//man[num - 1] = (Student*)calloc(1, sizeof(Student));
	memset(&man[num-1], 1,0,sizeof(Student));//첫번째 인자는 주소값을 넣어야한다.

	printf("%d번 학생의 정보를 수정합니다\n이름을 입력해 주세요 ", num);
	scanf("%s", man[num - 1].name);
	printf("%d번 학생의 국어, 영어, 수학성적을 입력해주세요 ", num);
	for (int i = 0; i < 3; i++) {
		scanf("%d", &man[num - 1].sungjuck[i]);
	}
	man[num - 1].all_sung = 0;

	for (int j = 0; j < 3; j++) {

		man[num - 1].all_sung += man[num - 1].sungjuck[j];
	}
	printf("입력이 완료되었습니다\n\n");
	all_sung(man, hms);
}

void input_info(Student* man, int hms) {
	for (int i = 0; i < hms; i++) {
		printf("학생의 이름을 입력해주세요 ");
		scanf("%s", man[i].name);

		printf("국어, 영어, 수학성적을 입력해주세요 ");
		for (int j = 0; j < 3; j++) {
			scanf("%d", &man[i].sungjuck[j]);
		}
		
		for (int j = 0; j < 3; j++) {
			man[i].all_sung += man[i].sungjuck[j];
		}
		
	}
	all_sung(man, hms);
}

void view_all(Student* man, int hms) {//3. 전체성적 출력
	char* mm[] = { "이름", "국어성적", "영어성적", "수학성적", "총점", "등수" };
	for (int i = 0; i < 6; i++) {
		printf("%-10s", mm[i]);
	}
	printf("\n");

	for (int i = 0; i < hms; i++) {
		printf("%-10s", man[i].name);
		for (int j = 0; j < 3; j++) {
			printf("%-10d", man[i].sungjuck[j]);

		}
		printf("%-10d", man[i].all_sung);
		printf("%-10d\n\n", man[i].rank);
	}
}

void all_sung(Student* man, int hms) {
	int rank = 1;

	for (int i = 0; i < hms;) {
		
		
		//if(man[i]->sungjuck[3])
		for (int j = 0; j < hms;) {
			

			if (man[i].all_sung > man[j].all_sung) {
				j++;
			}
			else if (man[i].all_sung < man[j].all_sung) {
				rank++;
				j++;
			}
			else if (man[i].all_sung == man[j].all_sung) {
				j++;
				if (i > j) {
					rank++;
				}
			}
		}

		man[i].rank = rank;
		rank = 1;
		i++;

	}
}
