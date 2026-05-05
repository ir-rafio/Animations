void printReverse(int ara[], int k)
{
    if(k == 0) return;
    print(ara[k]);
    printReverse(ara, k - 1);
}