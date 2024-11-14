#include<iostream>
#include<vector>
using namespace std;


bool isValid(int row, int col, vector<string> &inputMatrix){
    if(row<0 || col<0){
        return false;
    }
    if(row>=inputMatrix.size() || col>=inputMatrix[0].length()){
        return false;
    }
    return true;
}

bool isDigit(int row, int col, vector<string> &inputMatrix){
    // return character >= '0' && character <= '9';
    if(!isValid(row, col, inputMatrix)){
        return false;
    }
    return inputMatrix[row][col]>='0' && inputMatrix[row][col]<='9';
}

int main(){
    vector<string> inputMatrix;
    string temp;
    while(true){
        cin>>temp;
        if(temp == "")
            break;
        inputMatrix.push_back(temp);
    }
    bool isNumber=false, isPart=false;
    for(int i=0; i<inputMatrix.size(); i++){
        for(int j=0; j<inputMatrix[0].length(); j++){
            // if(isDigit(i, j, inputMatrix))
            if(isNumber){
                
            }
        }
    }
    return 0;
}