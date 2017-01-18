/*
 * w1c_timing.cpp
 *
 *  Created on: 10-Sep-2016
 *      Author: bharath
 */

// AUTHOR Bharath abharath@bu.edu
#include <iostream>
#include <ctime>
#include <math.h>
#include <limits.h>
using namespace std;

int main()
{

    clock_t start_clock,end_clock;

    start_clock = clock();  // Timing starts here

    int i = 0;

    short unsigned int a=1;

    while ( a > 0 )
    {
         a++;
    }

    end_clock = clock();    // Timing stops here


    double seconds = (double)(end_clock-start_clock) / CLOCKS_PER_SEC;


    cout << "short unsigned int time (microseconds):  " << seconds * pow(10,6) << endl;
    double x=seconds;


    unsigned int  b=1;
    start_clock = clock();
    		while (b > 0)
    		{
    			b++;
    		}
    end_clock = clock();    // Timing stops here
    double seconds_2 = (double)(end_clock-start_clock) / CLOCKS_PER_SEC;
    double y=seconds_2;
    cout << "unsigned int time (seconds):  " << seconds_2  << endl;

    long unsigned int c=1;
    //cout << "USHRT_MAX" << USHRT_MAX << endl;
    //cout << "UINT_MAX" << UINT_MAX << endl;
    //cout << "ULONG_MAX" << ULONG_MAX << endl;

    double z = double (ULONG_MAX/UINT_MAX) * double (seconds_2 * 3.17098 * pow(10,-8));

    //double seconds_3 = y/
    cout << "long unsigned int time (years):  " << z << endl ;

}




