// AUTHOR BHARATH abharath@bu.edu

#include <vector>
#include <iostream>
typedef std::vector<double> Poly;

Poly add_poly(const Poly &a,const Poly &b)
{
    Poly sum, p1, p2;
    unsigned long int c;
    int i;
    if ( a.size() <= b.size() )
    {
        c = b.size();
        p1 = b;
        p2 = a;
    }
    else
    {
        c = a.size();
        p1 = a;
        p2 = b;
    }
    for ( i=0 ; i<c ; i++ )
    {
        if (i < p2.size())
            sum.push_back(double(p2[i])+double(p1[i]));
        else if (i >= p2.size())
        {
            sum.push_back(double(p1[i]));
        }
    }
    return sum;
}

Poly multiply_poly(const Poly &a,const Poly &b)
{
    Poly Prod;
    unsigned long int column, row;
    column = a.size()+b.size()-1;
    row = a.size();
    double term[column][row], add[column];
    int i, j, k;
    
    for ( j=0 ; j<row ; j++ )
    {
        for ( k=0 ; k<j ; k++ )
        {
            term[k][j]=0;
        }
        
        for ( i=k ; i<column ; i++ )
        {
            if ( i<(b.size()+k) )
                term[i][j] = double(b[i-k])*double(a[j]);
            else
                term[i][j] = 0;
        }
    }
    
    for ( i=0 ; i<column ; i++ )
    {
        for ( j=0 ; j<row ; j++)
        {
            add[i]+=term[i][j];
        }
        Prod.push_back(double(add[i]));
    }
    return Prod;
}

//int main()
//{
//    
//    int Alen,Blen;
//    
//    std::cin >> Alen >> Blen;
//    
//    Poly A(Alen,0),B(Blen,0);
//    
//    for (auto& e : A)
//        std::cin >> e;
//    
//    for (auto& e : B)
//        std::cin >> e;
//    
//    for (auto e : add_poly(A,B))
//        std::cout << e << " ";
//    std::cout << std::endl;
//    
//    
//    for (auto e : multiply_poly(A,B))
//        std::cout << e << " ";
//    std::cout << std::endl;
//    
//    
//}
