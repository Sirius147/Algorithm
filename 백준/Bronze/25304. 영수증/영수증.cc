#include <iostream>
using namespace std;
int main()
{
    int sum,num;
    int n1,n2;
    cin >> sum >> num;
    while(num>=1)
    {
        cin >> n1 >> n2;
        sum-=n1*n2;
        num--;
    }
    if(sum == 0) cout << "Yes";
    else cout << "No";
    return 0;
}