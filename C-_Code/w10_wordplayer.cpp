// AUTHOR AkashMehta amehta22@bu.edu
// AUTHOR BharathAnanth abharath@bu.edu
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <map>
#include <set>
#include <algorithm>
using std::cout;
using std::string;
using std::cin;
using std::endl;
int main(int argc, char *argv[]) {
    std::ifstream thisfile;
    string usort, one, three, sortone;
    int t, two, four;
    std::vector<string> squares;
    std::vector<string> test;
    std::vector<string> inp;
    std::vector<int> inp_int;
    std::vector<string> sortvc;
    std::map<int, std::vector<string>> mymm;
    std::map<string, std::vector<string>> inmm;
    std::map<int, std::string> mymm_inp;
    thisfile.open(argv[1]);
    while (thisfile >> one) {
        usort = one;
        t = one.length();
        two = t;
        sort(one.begin(), one.end());
        inmm[one].push_back(usort);
        mymm[two].push_back(usort);
        sort(inmm[one].begin(), inmm[one].end());
        sort(mymm[two].begin(), mymm[two].end());
    }
    thisfile.close();
    string inpfile;
    while (cin >> three >> four) {
        if (three == "exit" && four == 0)
            return(0);
        sort(three.begin(), three.end());
    if (three.length() == four) {
        try {
            auto it = inmm.find(three);
            for (auto it2 = it->second.begin(); it2 != it->second.end(); it2++)
                cout<< (*it2) <<std::endl;
        }
        catch(...) {}
    }
    if (three.length() > four) {
        auto it = mymm.find(four);
        for (auto it2 = it->second.begin(); it2 != it->second.end(); it2++) {
            int o, flag, flag2;
            flag = 0;
            flag2 = 0;
            char * data = new char[(three).size() + 1];
            copy((three).begin(), (three).end(), data);
            char * data1 = new char[(*it2).size() + 1];
            copy((*it2).begin(), (*it2).end(), data1);
            for (int i = 0; i < four; i++) {
                o = 0;
                while ((*data != data1[i]) && *data != '\0') {
                data++;
                o++;
            }
            if (*data == '\0') {
                flag = 1;
            }
            data -= o;
            data[o] = ' ';
        }
            if (flag == 0) {
                cout << (*it2) << endl;
            }
        }
        }
        cout << "." << endl;
    }
    return 0;
    }
