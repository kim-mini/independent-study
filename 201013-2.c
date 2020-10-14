#include <stdio.h>
#pragma warning(disable:4996)
#include <stdlib.h>
#include <string.h>
#include<time.h>


//개인 성적 학생성명, 국어, 영어, 수학 세과목의 성적을 입력받는다.
//개인성적입력, 개인성적수정, 전체성적출력, 종료
typedef struct student {
	char* name ;
	int *sungjuck;
	int all_sung;
}Student;



void insert_grup(Student* std, int hms);
void menu(void);
void choice_num(Student* man, int hms);
void view_all(Student* man, int hms);
int comp_i(void* a, void* b);



main()
{
	int hms = 0;
	Student* std = { 0, };

	printf("학생 수를 입력해 주세요 ");
	scanf("%d", &hms);

	
	insert_grup(std, hms);
	choice_num(std, hms);
}



void insert_grup(Student *std,int hms) {//구조체 생성
	std = (Student*)malloc(sizeof(Student) * hms);
	for (int i = 0; i < hms; i++) {
		std[i].name = (char**)malloc(sizeof(char) * 11);
		std[i].sungjuck = (int*)malloc(sizeof(int) * 3); 
	}	
}

void menu(void) {// 메뉴
	puts("☆☆☆☆☆성적보관소☆☆☆☆☆");
	puts("==============================");
	puts("1. 개인 성적입력");
	puts("2. 개인 성적수정");
	puts("3. 전체성적 출력");
	puts("0. 종료");
	puts("==============================\n\n");
}

void choice_num(Student* man, int hms){//메뉴 클릭하면 행동발생

	int click = 0;
	menu();

	printf("번호를 입력해주세요");
	
	scanf("%d", &click);

	switch (click) {
	case 1:
        for(int i = 0; i < hms; i++){
            printf("학생의 이름을 입력해주세요");
            gets(man[i].name);
        

            for (int j = 0; j < 3; j++) {
                printf("국어, 영어, 수학성적을 입력해주세요");
                scanf("%d", man[i].sungjuck[j]);
                man[i].all_sung += man[i].sungjuck[j];
            }
        }
		break;
	case 2:
	case 3:
		view_all(&man, hms);
		break;
	case 0:
		printf("안녕히 가세요");
		break;
	}
}

void view_all(Student *man, int hms){//3. 전체성적 출력
	char* mm[] = { "이름", "국어성적", "영어", "수학" };
    for(int i = 0; i < 4; i++){
        printf("$-4s", mm[i]);
    }

	for (int i = 0; i < hms; i++) {
		printf("%-4s", man[i].name);
		for (int j = 0; j < hms; j++){
			printf("%-4d", man[i].sungjuck[j]);
		}
	}
}

//int all_sung(Student *man){
//    qsort(man->all_sung,sizeof(man->all_sung), sizeof(int), comp_i);
//
//}
//
//int comp_i(void *a, void *b){
//	(*(int*)a, *(int*)b);
//}
