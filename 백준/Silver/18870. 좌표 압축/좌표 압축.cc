// // //class, namespace, filesystem
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;
int n;
int main(){
    cin >> n;
    vector<int> v(n); vector<int> c(n);
    map<int,int> m; int idx = 0;
    for(int i = 0; i < n; i++){
        cin >> v[i]; c[i] = v[i];
    }
     
    sort(c.begin(), c.end());
    m[c[0]] = 0; idx++;

    for(int i = 1; i < n; i++){
        if(c[i]!=c[i-1]){
            m[c[i]] = idx; idx++;
        } 
    }
    for(int i = 0; i < n; i++){
        cout << m[v[i]] << ' ';
    }


    return 0;
}
