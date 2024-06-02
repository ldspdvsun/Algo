#include<stdio.h>
#include<stdlib.h>

int main()
{
    int i=10,j;
    for (int i = 1; i < 10; i++)
    {
        for (int j = 1; j <= i; ++j)
        {
            printf("%d x %d = %d ",j,i,i*j);
            if (i==j)
            {
                printf("\n");
            }
        }
    }
    printf("forLoop:%d\n",forLoop(100));
    printf("whileLoop:%d\n",whileLoop(100));
    printf("recur:%d\n",recur(100));
    return 0;
}

/* for 循环 */
int forLoop(int n)
{
    int res = 0;
    for (int i = 0; i <= n; i++)
    {
        res += i;
    }
    return res;
}

/* while 循环 */
int whileLoop(int n)
{
    int res =0;
    int i = 1;
    while (i <= n)
    {
        res += i;
        i++;
    }
    return res;
}

/* 递归 */
int recur(int n)
{
    // 终止条件
    if(n == 1)
    {
        return 1;
    }
    // 递：递归调用
    int res = recur(n-1);
    // 归：返回结果
    return n+res;
}