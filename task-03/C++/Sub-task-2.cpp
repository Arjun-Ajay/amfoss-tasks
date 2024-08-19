#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
    ifstream inputFile("input.txt");
    ofstream outputFile("output.txt");
    if (inputFile.fail())
    {
        cout<<"There was an error opening the input.txt file."<<endl;
    }
    if (outputFile.fail())
    {
        cout<<"Error opening the output.txt file."<<endl;
    }
    string content;
    getline(inputFile,content);
    outputFile<<content;
    inputFile.close();
    outputFile.close();
    return 0;
}