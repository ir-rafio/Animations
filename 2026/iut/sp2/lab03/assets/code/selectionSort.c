void selectionSort(int ara[], int n)
{
    int i, smol;
    
    for(i = 0; i < n; i++)
    {
        smol = findFirst(ara, i, n - 1);
        swap(ara[i], ara[smol]);
    }
}