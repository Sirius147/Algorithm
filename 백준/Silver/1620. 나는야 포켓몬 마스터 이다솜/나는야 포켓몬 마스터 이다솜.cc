#include <iostream>
#include <string>
#include <map>
using namespace std;
int n;
int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int m; cin >> n >> m;
    map<string,string> ptemp;
    string temp; string s_idx; int idx = 1;
    while(n>0){
        cin >> temp; s_idx = to_string(idx); idx++;
        ptemp[temp] = s_idx; ptemp[s_idx] = temp;
        n--;
    }
    while(m>0){
        cin >> temp; m--;
        cout << ptemp[temp] << '\n';
    }
    return 0;
}
