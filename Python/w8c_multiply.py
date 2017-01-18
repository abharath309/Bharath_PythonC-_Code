// AUTHOR BharathAnanth abharath@bu.edu
#include <iostream>
#include <string>
#include <vector>
#include <fstream>



using namespace std;
int main(int argc, char const *argv[])
	{


	int one,two;
	ifstream firstfile;
	ifstream secondfile;
	ofstream outfile;
	int i,j;
	i=0;
	j=0;
		if(argc == 6)
		{
				int k;
				k=stoi(argv[3]);
				int firstmat[k][k];
				int secondmat[k][k];
				firstfile.open(argv[4]);


			while(firstfile>>one)
			{
				cout<<one<<" "<<"file1.txt"<<endl;
				firstmat[j][i] = one;
				i++;
				if(i==k)
					{
						i=0;
						j++;
					}
			}
			i=0;
			j=0;
			secondfile.open(argv[5]);
			while(secondfile>>two)
			{
				cout<<two<<" "<<"file2.txt"<<endl;
				secondmat[j][i] = two;
				i++;
				if(i==k)
					{
						i=0;
						j++;
					}
			}

			for(i=0;i<k;i++)
						{
							for(j=0;j<k;j++)
							{
								cout<<"first "<<i<<" "<<j<<" "<< firstmat[i][j]<<endl;
							}
						}
			for(i=0;i<k;i++)
						{
							for(j=0;j<k;j++)
							{
								cout<<"second "<<i<<" "<<j<<" "<<secondmat[i][j]<<endl;
							}
						}


			int outmat[k][k];

			cout<<"it's 6 "<<endl;

			for(i=0;i<k;i++)
					{
//						cout<<"in for 1"<<endl;
						for(j=0;j<k;j++)
						{
//							cout<<"in for 2"<<endl;
							outmat[i][j]=0;
							cout<<i<<" "<<j<<" "<<outmat[i][j]<<endl;
						}
					}
			i=0;
			j=0;
			 while(i<k)
			 {
			    for (int j=0;j<k;j++)
			        for (int l=0;l<k;l++)
			        {
			        	outmat[i][j] += firstmat[i][l] * secondmat[l][j];
			        	cout<<i<<" "<<j<<" "<<l<<" "<<" "<<firstmat[i][l]<<"*"<<secondmat[l][j]<<" = "<<outmat[i][j]<<endl;
			        }
			    i++;
			    cout<<i<<endl;
			 }

			for(i=0;i<k;i++)
			{
				for(j=0;j<k;j++)
				{
					cout<<outmat[i][j]<<endl;
				}
			}

			 outfile.open(argv[6]);
			 for(i=0;i<k;i++)
			 {
				 for(j=0;j<k;j++)
				 {
					 outfile << outmat[i][j]<<" ";
				 }
				 outfile<<endl;
			 }
			 outfile.close();
		}
		if(argc == 8)
				{
			int m,n,l;
			m = stoi(argv[3]);
			n = stoi(argv[4]);
			l = stoi(argv[5]);
			cout << m << " "<<n<<" "<<l<<endl;
			int firstmat[n][m];
			int secondmat[l][n];
		firstfile.open(argv[6]);

		while(firstfile>>one)
		{
				cout<<one<<" "<<j<<" "<<i<<"file1.txt"<<endl;
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
		while(secondfile>>two)
		{
				cout<<two<<" "<<i<<" "<<j<<" "<<"file2.txt"<<endl;
			secondmat[j][i] = two;
			i++;
			if(i==n)
				{
					i=0;
					j++;
				}
		}

		for(i=0;i<n;i++)
					{
						for(j=0;j<m;j++)
						{
							cout<<"first "<<i<<" "<<j<<" "<< firstmat[i][j]<<endl;
						}
					}
		for(i=0;i<l;i++)
					{
						for(j=0;j<n;j++)
						{
							cout<<"second "<<i<<" "<<j<<" "<<secondmat[i][j]<<endl;
						}
					}


		int outmat[m][l];

			cout<<"it's 6 "<<endl;
			cout<<"test"<<endl;
		for(i=0;i<m;i++)
				{
					cout<<"in for 1"<<endl;
					for(j=0;j<l;j++)
					{
							cout<<"in for 2"<<endl;
						outmat[i][j]=0;
							cout<<i<<" "<<j<<" "<<outmat[i][j]<<endl;
					}
				}
		i=0;
		j=0;
		 for (int i=0;i<m;i++)
		    for (int j=0;j<n;j++)
		        for (int k=0;k<l;k++)
		        {
		        	outmat[i][j] += firstmat[i][k] * secondmat[k][j];
		        	cout<<i<<" "<<j<<" "<<k<<" "<<firstmat[i][k]<<" * "<<secondmat[k][j]<<" "<<outmat[i][j]<<endl;
		        }
		for(i=0;i<l;i++)
		{
			for(j=0;j<m;j++)
			{
				cout<<outmat[i][j]<<endl;
			}
		}

		 outfile.open(argv[8]);
		 for(i=0;i<m;i++)
		 {
			 for(j=0;j<l;j++)
			 {
				 outfile << outmat[m][l]<<" ";
			 }
			 outfile<<endl;
		 }
		 outfile.close();				}

	}
