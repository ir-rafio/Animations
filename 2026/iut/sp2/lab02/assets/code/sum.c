int sum(int ara[], int k)
{
    if(k == 0) return 0;
    return sum(ara, k - 1) + ara[k - 1];
}