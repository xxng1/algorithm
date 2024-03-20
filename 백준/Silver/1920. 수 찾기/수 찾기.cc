#include <iostream>
#include <algorithm>

using namespace std;

int arrN[100000];
int arrM[100000];
bool check[100000] = {0,};

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  
  int N, M;
  cin >> N;
  for(int i=0; i<N; i++){
    cin >> arrN[i];
  }
  sort(arrN, arrN+N);

  cin >> M;
  for(int i=0; i<M; i++){
    cin >> arrM[i];
  }
  
  for(int i=0; i<M; i++){
    int left = 0;
    int right = N-1;

    while(left <= right){
      int mid = (left + right) / 2;
      if(arrM[i]==arrN[mid]){
        check[i] = true;
        break;
      }
      else if(arrM[i]>arrN[mid]){
        left = mid + 1;
      }
      else if(arrM[i]<arrN[mid]){
        right = mid - 1;
      }
    }
  }
  for(int i=0; i<M; i++){
    cout << check[i] << ' ';
  }
}