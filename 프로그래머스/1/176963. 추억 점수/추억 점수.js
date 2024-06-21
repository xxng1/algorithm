function solution(name, yearning, photo) {
    var answer = [];
    // console.log(name.indexOf("may"))
    for(let i = 0; i < photo.length; i++){
        // console.log(photo[i]);
        cnt = 0;
        for (let j = 0; j < photo[i].length; j++){
            // console.log(photo[i][j]);
            // console.log(name.indexOf(photo[i][j]));
            if (name.indexOf(photo[i][j]) === -1){
                continue;
            }
            else{
                cnt = cnt + yearning[name.indexOf(photo[i][j])]
            }
        }
        // console.log(cnt);
        answer.push(cnt)
        
    }
    
    
    return answer;
}