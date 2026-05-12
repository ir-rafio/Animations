int findMin(int ara[], int n)
{
    int smol = 0;
    
    for(int i = 1; i < n; i++)
        if(ara[i] < ara[smol])
            smol = i;
    
    return smol;
}