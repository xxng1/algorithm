#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solution(vector<int> food) {
    string answer = "";
    // answer += "123";
    
    // int a = 3;
    // cout << answer << endl;
    
    for (int i=1; i < food.size(); i++){
        int cnt = food[i] / 2;
        // cout << cnt << endl;
        
        for (int j = 0; j < cnt; j ++){
            answer += to_string(i);
        }
    }
    answer += "0";
    
    for (int i=food.size()-1; i > 0; i--){
        int cnt = food[i] / 2;
        // cout << cnt << endl;
        
        for (int j = 0; j < cnt; j ++){
            answer += to_string(i);
        }
    }    
    
    
    return answer;
}