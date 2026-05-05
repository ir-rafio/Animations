int main()
{
    int l, w, a, b;
    scanf("%d %d %d %d", &l, &w, &a, &b);

    double rectangleArea = getRectangleArea(l, w);
    double triangleArea = getTriangleArea(a, b);
    double c = getHypotenuse(a, b);
    double r = c / 2;
    double halfCircleArea = getCircleArea(r) / 2;
    double blueArea = rectangleArea - triangleArea - halfCircleArea;

    printf("%.2lf", blueArea);

    return 0;
}