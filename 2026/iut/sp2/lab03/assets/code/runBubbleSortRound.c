void runBubbleSortRound(int ara[], int n)
{
    for(int i = 0; i < n - 1; i++)
    {
        if(ara[i + 1] < ara[i])
            swap(ara[i], ara[i + 1]);
    }
}