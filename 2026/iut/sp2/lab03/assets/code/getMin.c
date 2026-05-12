int getMin(int ara[], int n)
{
    int smolValue = ara[0];

    for(int i = 1; i < n; i++)
        if(ara[i] < smolValue)
            smolValue = ara[i];
    
    return smolValue;
}