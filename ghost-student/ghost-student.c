#include "img.h"

#include <libxml/tree.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define RED "\x1B[31m"
#define GRN "\x1B[32m"
#define RST "\x1B[0m"

#define GB_LEN 7
#define HW_LEN 7
typedef struct Grade {
  unsigned int id;
  unsigned int hw_grade[7];
  char letter_grade[4];
} Grade;


void print_flag() {
  FILE *flag;
  int c;

    flag = fopen("/home/challenger/ghost-student/flag", "r");
  if (flag == NULL)
    flag = fopen("/home/challenger/.dummy_flag", "r");
  if (flag == NULL){
    printf(
        "[%s] Something is WRONG, please contact your instructor or your TA\n",
        __FUNCTION__);
    exit(-1);
  }

  printf(GRN "%s\n" RST, DEAD_CANARY_IMG);
  printf("Congratulations!! Take this key with you\n");
  printf("-----------------------------------------------\n");
  while ((c = getc(flag)) != EOF)
    putchar(c);
  printf("-----------------------------------------------\n");
  exit(0);
}


void print_gradebook(Grade* gradebook) {
  char output[512];
  int cnt, avg;
  int i, j;

  cnt = snprintf(output, 512, "\nEntry#\tStudentID\tHW-AVG\tLetterGrade\n");
  for (i = 0; i < GB_LEN; i++) {
    cnt += snprintf(output + cnt, 512, "[%u]\t%-9d\t", i, gradebook[i].id);
    for (j = 0, avg = 0; j < HW_LEN; j++) {
      avg += gradebook[i].hw_grade[j];
    }
    avg /= 7;
    cnt += snprintf(output + cnt, 512, "%-6d\t", avg);
    cnt += snprintf(output + cnt, 512, "%-1s\n", gradebook[i].letter_grade);
  }
  puts(output);
}
void print_individual(Grade *grade) {
  char output[512];
  int cnt = 0;
  int avg;
  int i;

  cnt += snprintf(output + cnt, 512, "---------------------------\n");
  cnt += snprintf(output + cnt, 512, "StudentID: %d\n", grade->id);
  cnt += snprintf(output + cnt, 512, "HW1 HW2 HW3 HW4 HW5 HW6 HW7\n");
  for (i = 0, avg = 0; i < HW_LEN; i++) {
    cnt += snprintf(output + cnt, 512, "%-3u ", grade->hw_grade[i]);
  }
  avg /= HW_LEN;
  cnt +=
      snprintf(output + cnt, 512, "\nLetter grade: %s\n", grade->letter_grade);
  cnt += snprintf(output + cnt, 512, "---------------------------\n");
  puts(output);
}

void show_menu(Grade* gradebook) {
  char output[16];
  unsigned int choice;
  unsigned int idx;

  while (choice != 0) {

    printf("\nGradebook Program Menu\n");
    printf("\t1. Print gradebook\n");
    printf("\t2. Print individual grade\n");
    printf("\t3. Change Letter Grade\n");
    

    printf("\t0. Exit\n");
    printf("CMD >>> ");
    fflush(stdout);
    if (fgets(output, 3, stdin) == NULL)
      exit(0);
    sscanf(output, "%d", &choice);

    switch (choice) {
    case 1:
      print_gradebook(gradebook);
      break;

    case 2:
      printf("Enter entry# >>> ");
      fflush(stdout);
      if (fgets(output, 9, stdin) == NULL)
        exit(0);
      sscanf(output, "%d", &idx);
      /* We have 7 students */
      if (idx <= 7)
        print_individual(&gradebook[idx]);
      else
        printf(RED "Out of index\n" RST);
      break;

    case 3:
      printf("Enter entry# >>> ");
      fflush(stdout);
      if (fgets(output, 9, stdin) == NULL)
        exit(0);
      sscanf(output, "%d", &idx);
      /* We have 7 students */
      if (idx < 7){
	printf("Enter the new letter grade >>> ");
	fflush(stdout);
        gets(gradebook[idx].letter_grade);
      }
      else
        printf(RED "Out of index\n" RST);


      
      break;
    case 0:
      break;

    default:
      printf("Wrong choice");
      break;
    }
  }
}
void manage_gradebook() {
  
  Grade gradebook[7] = {
      {
          .id = 20171234,
          .hw_grade = {72, 60, 70, 75, 85, 60, 94},
          .letter_grade = "C",
      },
      {
          .id = 20183949,
          .hw_grade = {79, 98, 88, 68, 75, 71, 94},
          .letter_grade = "B",
      },
      {
          .id = 20193847,
          .hw_grade = {99, 69, 90, 89, 76, 93, 63},
          .letter_grade = "B",
      },
      {
          .id = 20160921,
          .hw_grade = {95, 71, 84, 64, 71, 97, 97},
          .letter_grade = "B",
      },
      {
          .id = 20152292,
          .hw_grade = {81, 85, 90, 62, 98, 69, 93},
          .letter_grade = "B",
      },
      {
          .id = 20192383,
          .hw_grade = {99, 98, 91, 82, 91, 75, 95},
          .letter_grade = "A",
      },
      {
          .id = 20172088,
          .hw_grade = {49, 20, 70, 50, 34, 72, 87},
          .letter_grade = "D",
      },

  };
  print_gradebook(gradebook);
  show_menu(gradebook);
  return;
}
void remove_null_in_canary64(void) {
  asm volatile("movq %%fs:0x28, %%rax;"
               "or $0x12, %%rax;"
               "movq %%rax, %%fs:0x28;"
               :
               :
               : "rax","rcx");
}
/* Emulate early versions of canary */
void remove_null_in_canary(void) {
  asm volatile("movl %%gs:0x14, %%eax;"
               "or $0x12, %%eax;"
               "movl %%eax, %%gs:0x14;"
               :
               :
               : "eax");
}

static void provide_gadgets(void) {
  srand(time(0));
  sqrt(rand());
  xmlGetProp(NULL, "ID");
}


int main() {
  remove_null_in_canary64();
  provide_gadgets();

  printf(RED "%s\n" RST, GHOST_TEXT);
  printf(RED "%s\n" RST, GHOST_IMG);
  printf(RED
         "\nWarning: This program is protected by a randomly generated stack canary \n" RST);
  printf(RED
         "\nFind the GHOST STUDENT, and he will whisper the value of canary into your ears...\n\n" RST);
  
  manage_gradebook();
  printf("Terminating...\n");
  return 0;
}
