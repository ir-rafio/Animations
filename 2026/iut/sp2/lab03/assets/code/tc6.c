int getRange(int ara[], int n)
{
    int minValue = ara[0], maxValue = ara[0];

    for(int i = 1; i < n; i++)
        if(ara[i] < minValue) minValue = ara[i];

    for(int i = 1; i < n; i++)
        if(ara[i] > maxValue) maxValue = ara[i];
    
    return maxValue - minValue;
}