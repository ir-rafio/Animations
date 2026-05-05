int main()
{
    int l, w, a, b;
    scanf("%d %d %d %d", &l, &w, &a, &b);

    double area1 = 1.0 * l * w;
    double area2 = 0.5 * a * b;
    double area3 = 3.14 * (1.0 * a * a + 1.0 * b * b) / 4 / 2;
    double area = area1 - area2 - area3;

    printf("%.2lf", area);

    return 0;
}