#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//emotion list: each emotion has an ID that corresponds to it's
//initial position on the array
char * emotions[] = {
  "anger",
  "annoyance",
  "contempt",
  "disgust",
  "irritation",
  "anxiety",
  "embarrassment",
  "fear",
  "helplessness",
  "powerlessness",
  "worry",
  "doubt",
  "envy",
  "frustration",
  "guilt",
  "shame ",
  "boredom",
  "despair",
  "disappointment",
  "hurt",
  "sadness",
  "shock",
  "stress",
  "tension",
  "amusement",
  "delight",
  "elation",
  "excitement",
  "happiness",
  "joy",
  "pleasure",
  "affection",
  "empathy",
  "friendliness",
  "love",
  "courage",
  "hope",
  "pride",
  "satisfaction",
  "trust",
  "calm",
  "content",
  "relaxed",
  "relieved",
  "serene",
  "interest",
  "politeness",
  "surprise",
};

//length of emotions array
#define n_emotions (sizeof (emotions) / sizeof (char *))

int lastRandom = 0;

//sanitizes and returns terminal input
char getInput(){
  char toReturn = ' ';
  scanf("%c", &toReturn);

  if(toReturn != 'y' && toReturn != 'x' && toReturn != 'n'){
    getInput();
  }

  return toReturn;
}

//generates random int between [0, max)
unsigned randInt(int max){
  srand(time(0));

  int r;

  do
  {
      r = rand();
  } while (r < -1 || r >= max);

  return r;
}

//asks question and stores answer in training array
void askQuestion(){
  int a = randInt(n_emotions);

  while(a == lastRandom){
    a = randInt(n_emotions);
  }

  printf("are you feeling %s?\n", emotions[a]);
  printf("answer [y/x/n]: ");
  char response = getInput();

  lastRandom = a;
}

int main(){
  askQuestion();
  askQuestion();
   return (0);
}
