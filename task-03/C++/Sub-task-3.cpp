#include <iostream>
using namespace std;
int main()
{
    int num,i,j,k;
    cout<<"Enter a number: ";
    cin>>num;
    for(i=1;i<=num;i++)
    {
        for(j=0;j<(num-i);j++)
        {
           cout<<" ";
        }
        for(k=0;k<i;k++)
        {
            cout<<"*"<<" ";
        }
        cout<<endl;
    }
    for(i=(num-1);i>0;i--)
    {
        for(j=0;j<(num-i);j++)
        {
            cout<<" ";
        }
        for(k=1;k<=i;k++)
        {
            cout<<"*"<<" ";
        }
        cout<<endl;
    }
return 0;
}