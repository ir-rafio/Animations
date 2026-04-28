void abc(int d)
{
    if(d == 0) return;
    abc(d / 8);
    print(d % 8);
}