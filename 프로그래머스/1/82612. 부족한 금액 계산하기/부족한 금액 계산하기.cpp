#include <iostream>

using namespace std;

long long solution(int price, int money, int count)
{
    long long answer = -1;
    
    long long total = 0;
    for (int i = 0; i < count; i ++){
        total += (i+1) * price;
    }
    
    long long result = total - money;
    if (result > 0){
        answer = result;
    } else {
        answer = 0;
    }
    
    return answer;
}