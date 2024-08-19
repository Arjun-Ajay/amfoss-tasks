#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    int num,i,j,k;
    ifstream inputFile("input.txt");
    ofstream outputFile("output.txt");
    inputFile>>num;
    if(inputFile.fail())
    {
        cout<<"ERROR: Failed to load input.txt file";
    }
    if(outputFile.fail())
    {
        cout<<"ERROR: Failed to load output.txt file";
    }
    for(i=1;i<=num;i++)
    {
        for(j=0;j<(num-i);j++)
        {
           outputFile<<" ";
        }
        for(k=0;k<i;k++)
        {
            outputFile<<"*"<<" ";
        }
        outputFile<<endl;
    }
    for(i=(num-1);i>0;i--)
    {
        for(j=0;j<(num-i);j++)
        {
            outputFile<<" ";
        }
        for(k=1;k<=i;k++)
        {
            outputFile<<"*"<<" ";
        }
        outputFile<<endl;
    }
    inputFile.close();
    outputFile.close();
return 0;
}