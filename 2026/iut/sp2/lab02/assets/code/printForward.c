void printForward(int ara[], int k)
{
    if(k == 0) return;
    printForward(ara, k - 1);
    print(ara[k]);
}