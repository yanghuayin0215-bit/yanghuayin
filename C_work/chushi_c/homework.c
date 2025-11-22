#include <stdio.h>
#include <string.h>
/* int sum1(int a,int c)
{
    return (-8 +22)*a - 10 +c / 2;
}
int main()
{
    printf("%d\n",sum1(40,212));
    return 0;
}
 */


 //int max(int a,int b)
 //{
    //if (a > b)
    //
        //return a;
   // 
  //  else
  //  
  //      return b;
  //  
 //}
 //int main()
 //{
/*     char arr[] = {'d','f','j'};
   // printf("%d\n",strlen(arr));
    //return 0; */
/* 
    //int a = 10;
    //int arr[a]; */
    //printf("%d\n",max(10,20));

    //return 0;
//}
int func(int a)
{
    if (a > 0)
        return 1;
    else if(a == 0)
        return 0;
    else
        return -1;
}
int main()
{
    int x = 0;
    scanf("请输入%d",&x);
    printf("结果为%d",func(x));
    return 0;
}