// AUTHOR AkashMehta amehta22@bu.edu
// AUTHOR MuhammadZuhayrRaghib mzraghib@bu.edu
// AUTHOR Bharath abharath@bu.edu
// AUTHOR MuhammadKasimPatel kasimp93@bu.edu
#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;
int main(int argc, char const *argv[])
	{

	ifstream firstfile; // declare input file stream object 'firstfile'
	ifstream secondfile;
	ofstream outfile;
	int i,j;
	i=0;
	j=0;
	int k=stod(argv[3]);
	double firstmat[k][k];  // initialize empty matrix
	double secondmat[k][k]; // initialize empty matrix
	double one,two;
	string a = "";
	string b = "";

		if(argc == 6)  // square matrix mode
		{

			if ((string(argv[1]) != "double") && (string(argv[1]) != "int")) // if dtype != double or int
				{
				 return(1);
				 cout<< "dtype error" << endl;
				}

			firstfile.open(argv[4]); // open file1
			if (!(firstfile.is_open())) // if file1 does not open, give error
				{
				return(2);
				}


			while(firstfile >> a)  // read int/double one by one from firstfile and put it in 'one'
			  {
				try
				{
					one = stod(a);

				}
				catch(...)
				{
					return(3);
				}

//				cout<<one<<" "<<"file1.txt"<<endl;  //printing...
				firstmat[j][i] = one;  // index j,i = double 'one'
				i++;  // next
				if(i==k)  // if i = N
					{
						i=0;
						j++;// next row
					}

			}

			i=0;  // reinitialize
			j=0;
			secondfile.open(argv[5]);
			if (!(secondfile.is_open())) // if file2 does not open, give error
				{
				return(2);
				}
			while(secondfile>>b)
			{
				try
				{
					two = stod(b);

				}
				catch(...)
				{
					return(3);
				}

//				cout<<two<<" "<<"file2.txt"<<endl;
				secondmat[j][i] = two;
				i++;
				if(i==k)
					{
						i=0;
						j++;
					}
			}

//			for(i=0;i<k;i++)   // printing...
//						{
//							for(j=0;j<k;j++)
//							{
//								cout<<"first "<<i<<" "<<j<<" "<< firstmat[i][j]<<endl;
//							}
//						}
//			for(i=0;i<k;i++) // printing...
//						{
//							for(j=0;j<k;j++)
//							{
//								cout<<"second "<<i<<" "<<j<<" "<<secondmat[i][j]<<endl;
//							}
//						}


			double outmat[k][k];   // initialize the product matrix

//			cout<<"it's 6 "<<endl;      // printing...

			for(i=0;i<k;i++)
					{
						for(j=0;j<k;j++)
						{

							outmat[i][j]=0;
							cout<<i<<" "<<j<<" "<<outmat[i][j]<<endl;
						}
					}
			i=0;
			j=0;
			 for (int i=0;i<k;i++)
			    for (int j=0;j<k;j++)
			        for (int l=0;l<k;l++)
			        {
			        	outmat[i][j] += firstmat[i][l] * secondmat[l][j];
			        	cout<<i<<" "<<j<<" "<<l<<" "<<" "<<firstmat[i][l]<<"*"<<secondmat[l][j]<<" = "<<outmat[i][j]<<endl;
			        }

			for(i=0;i<k;i++)
			{
				for(j=0;j<k;j++)
				{
					cout<<outmat[i][j]<<endl;
				}
			}
			outfile.open(argv[6]); // open file3

			if (string(argv[2]) == "int") // if int, then convert product matrix to int
				{
				cout <<"type int" << endl;
				for(i=0;i<k;i++)
							 {
								 for(j=0;j<k;j++)
								 {
									 outfile << int(outmat[i][j])<<" ";
								 }
								     outfile<< endl ;
							 }

				}
	    	else if (string(argv[2]) == "double")
				{
	    		cout <<"type double" << endl;
	    		for(i=0;i<k;i++)
	    					 {
	    						 for(j=0;j<k;j++)
	    						 {
	    							 outfile << double(outmat[i][j])<<" ";
	    						 }
	    						 outfile<< endl ;
	    					 }

				}

			 outfile.close();
		}


		if(argc == 8)  // GENERAL MATRIX MODE
		{
			int m,n,l;
			m = stoi(argv[3]);
			n = stoi(argv[4]);
			l = stoi(argv[5]);
			cout << m << " "<<n<<" "<<l<<endl;
			double firstmat[n][m];
			double secondmat[l][n];
		firstfile.open(argv[6]);
		if (!(firstfile.is_open())) // if file1 does not open, give error
			{
			return(2);
			}

		while(firstfile >> a)  // read int/double one by one from firstfile and put it in 'one'
			{
			try
			{
				one = stod(a);
			}
			catch(...)
			{
			return(3);
			}
//				cout<<one<<" "<<j<<" "<<i<<"file1.txt";
//				cout << endl;
			firstmat[j][i] = one;
			i++;
			if(i==m)
				{
					i=0;
					j++;
				}
		}
		i=0;
		j=0;
		secondfile.open(argv[7]);
		if (!(secondfile.is_open())) // if file2 does not open, give error
			{
			return(2);
			}

		while(secondfile>>b)
		{
			try
			{
				two = stod(b);

			}
			catch(...)
			{
				return(3);
			}
//		    cout<<two<<" "<<i<<" "<<j<<" "<<"file2.txt"<<endl;
			secondmat[j][i] = two;
			i++;
			if(i==l)
				{
					i=0;
					j++;
				}
		}

//		for(i=0;i<n;i++)
//					{
//						for(j=0;j<m;j++)
//						{
//							cout<<"first "<<i<<" "<<j<<" "<< firstmat[i][j]<<endl;
//						}
//					}
//		for(i=0;i<l;i++)
//					{
//						for(j=0;j<n;j++)
//						{
//							cout<<"second "<<i<<" "<<j<<" "<<secondmat[i][j]<<endl;
//						}
//					}


		int outmat[m][l];

		for(i=0;i<m;i++)
				{
					cout<<"in for 1"<<endl;
					for(j=0;j<l;j++)
					{

						outmat[i][j]=0;
//							cout<<i<<" "<<j<<" "<<outmat[i][j]<<endl;
					}
				}
		i=0;
		j=0;
		 for (int i=0;i<m;i++)
		    for (int j=0;j<l;j++)
		        for (int k=0;k<n;k++)
		        {
		        	outmat[i][j] += firstmat[i][k] * secondmat[k][j];
//		        	cout<<i<<" "<<j<<" "<<k<<" "<<firstmat[i][k]<<" * "<<secondmat[k][j]<<" "<<outmat[i][j]<<endl;
		        }


		for(i=0;i<m;i++)
		{
			for(j=0;j<l;j++)
			{
				cout<<outmat[i][j]<<endl;
			}
		}

		 outfile.open(argv[8]);
		 for(i=0;i<m;i++)
		 {
			 for(j=0;j<l;j++)
			 {
				 outfile << outmat[i][j]<<" ";
			 }
			 outfile<<endl;
		 }
		 outfile.close();
				}
		if(argc!=6 && argc!=8)
		{
			return(1);
		}


	}


