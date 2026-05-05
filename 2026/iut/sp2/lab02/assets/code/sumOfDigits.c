int sumOfDigits(int x)
{
    if(x == 0) return 0;
    return sumOfDigits(x / 10) + (x % 10);
}