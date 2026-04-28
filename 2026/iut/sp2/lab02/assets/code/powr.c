long long powr(int a, int p)
{
    if(p == 0) return 1;
    return a * powr(a, p - 1);
}