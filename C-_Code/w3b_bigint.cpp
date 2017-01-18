// AUTHOR Bharath abharath@bu.edu

#include <vector>
#include <iostream>
#include <string>
typedef std::string Big_Int;
typedef std::vector<int> Poly;

Big_Int multiply_int(const Big_Int &a,const Big_Int &b)
{
    int i, j, k;
    Poly y;
    std::string output;
    int num1[a.size()],num2[b.size()];
    
    for ( i=0 ; i<a.size() ; i++ )
    {
        num1[i]=a[i]-'0';
    }
    
    for ( i=0 ; i<b.size() ; i++ )
    {
        num2[i]=b[i]-'0';
    }
    
    unsigned long int c, r;
    c = a.size()+b.size()-1;
    r = a.size();
    int t[c][r], add[c+1];
    
    for ( j=0 ; j<r ; j++ )
    {
        for ( k=0 ; k<j ; k++ )
        {
            t[k][j]=0;
        }
        
        for ( i=k ; i<c ; i++ )
        {
            if ( i<(b.size()+k) )
                t[i][j] = num2[i-k]*num1[j];
            else
                t[i][j] = 0;
        }
    }
    
    for (i=0; i<c+1; i++)
    {
        add[i]=0;
    }
    
    for ( i=(c-1) ; i>=0 ; i-- )
    {
        for ( j=(r-1) ; j>=0 ; j--)
        {
            add[i+1]+=t[i][j];
        }
        int div=add[i+1]/10;
        if (div>0)
        {
            add[i+1]-=div*10;
            add[i]+=div;
        }
    }
    
    if (add[0]!=0)
    {
        for ( i=0 ; i<=c ; i++ )
        {
            y.push_back(add[i]);
        }
        
        for ( i=0 ; i<=c ; i++ )
        {
            output.push_back(char(y[i]+'0'));
        }
    }
    else
    {
        for ( i=0 ; i<c ; i++ )
        {
            y.push_back(add[i+1]);
        }
    
        for ( i=0 ; i<c ; i++ )
        {
            output.push_back(char(y[i]+'0'));
        }
    }
    return output;
}


