int findFirst(int ara[], int l, int r)
{
    int i, smol = l;
    
    for(i = l + 1; i <= r; i++)
    {
        if(ara[i] < ara[smol])
            smol = i;
    }

    return smol;
}