#include <iostream>
#include <string>

using namespace std;

int main(){
    int a;
    string b;

    cin >> a;
    cin >> b;

    int b_1 = stoi(string(1, b[2]));  
    int b_2 = stoi(string(1, b[1]));  
    int b_3 = stoi(string(1, b[0]));  

    int result1 = a * b_1;
    int result2 = a * b_2;
    int result3 = a * b_3;

    int result = result1 + result2 * 10 + result3 * 100;

    cout << result1 << endl;
    cout << result2 << endl;
    cout << result3 << endl;
    cout << result << endl;

    return 0;
}
