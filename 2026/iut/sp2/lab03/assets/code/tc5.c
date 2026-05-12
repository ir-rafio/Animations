long long sumAllPairProducts(int ara[], int n)
{
    long long sum = 0;
    
    for(int i = 0; i < n; i++)
        for(int j = i + 1; j < n; j++)
            sum += 1LL * ara[i] * ara[j];
    
    return sum;
}