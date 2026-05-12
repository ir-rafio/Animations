void pushLeft(int ara[], int k)
{
    for(int i = k; i > 0; i--)
    {
        if(ara[i] < ara[i - 1])
            swap(ara[i], ara[i - 1]);
        
        else break;
    }
}