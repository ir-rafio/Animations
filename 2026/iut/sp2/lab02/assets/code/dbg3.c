long long powr(int a, int p)
{
    if(p == 0) return 1;
    return powr(a, p + 1) / a;
}