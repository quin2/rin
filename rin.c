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

//number of emotions to associate at once
#define linkages 2

//storage array for distance matrix
float emotionDist[n_emotions][n_emotions];

//sanitizes and returns terminal input
int lastRandom = 0;
char getInput(){
  char toReturn = ' ';
  scanf("%c", &toReturn);

  if(toReturn != 'y' && toReturn != 'x' && toReturn != 'n'){
    getInput();
  }

  while ((getchar()) != '\n'); //clear input buffer

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

//asks question and returns emotion tagged if user is feeling it
int askQuestion(){
  int a = randInt(n_emotions);

  while(a == lastRandom){
    a = randInt(n_emotions);
  }

  printf("are you feeling %s?\n", emotions[a]);
  printf("answer [y/x/n]: ");
  char response = getInput();

  if(response == 'x'){
    askQuestion();
  }

  if(response == 'n'){
    return -1;
  }

  return a;
}

int main(){
  int linkage[linkages];

  //get array of two numbers to link together
  int n = 0;
  while(n < linkages){
    int emotion = askQuestion();
    if(emotion != -1){
      linkage[n] = emotion;
      n++;
    }
  }

   return (0);
}
