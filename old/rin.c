//BIG TODO:
//test file in and file out functions
//deal with garbage inputs
//prevent numbers from cropping up many times in a row
//fix fucky double storgae function causing segfault
//in fucture: add testing to file io
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
#define n_emotions 48

//number of emotions to associate at once
#define linkages 3

#define fileName "train.rin"

//storage array for distance matrix
float emotionDist[n_emotions][n_emotions];

//sanitizes and returns terminal input
//how to reject wrong characters correctly?
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
  printf("\n");

  if(response == 'x'){
    askQuestion();
  }

  if(response == 'n'){
    return -1;
  }

  return a;
}

//loads the training array into the program
void fileIn(){
  FILE *f = fopen(fileName, "rb");
  fread(emotionDist, sizeof(float), n_emotions * n_emotions, f);
/*
  for(i=0;i<5;i++)
   {
       (fgets (clientDataNew[i], 128, fp));
   }
   */
  fclose(f);
}

//moves the current training array back to a local file
void fileOut(){
  FILE *f = fopen(fileName, "wb");
  fwrite(emotionDist, sizeof(float), n_emotions * n_emotions, f);
  fclose(f);
}

//tracks on number of training sessions
float logTraining(){
  float nTrained;
  FILE *f = fopen("log", "r");
  fscanf(f, "%f", &nTrained);

  nTrained += linkages;

  fprintf(f, "%f", nTrained);
  fclose(f);

  return nTrained;
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

  fileIn(); //implies empty train.rin is available!!
  //test fileIN and fileOut first


  //find every possible combination of linkages, move to array
  for(int i = 0; i < linkages - 1; i++){
    for(int j = i + 1; j < linkages; j++){
      printf("possible linkage is %s, %s\n", emotions[linkage[i]], emotions[linkage[j]]);
      printf("possible linkage is %s, %s\n", emotions[linkage[j]], emotions[linkage[i]]);
    }
  }

  //start operating on array!

   return (0);
}
