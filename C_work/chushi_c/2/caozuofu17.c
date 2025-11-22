/* 
算术操作符：+ - * / %
移位操作符：>> <<  右移与左移
位操作符: & ^ |
赋值操作符: = += -= *= /= %= &= ^= |= >>= <<=
单目操作符: ! & sizeof ~ -- ++ * (类型)
    区别于双目操作符，他只有一个操作数，例：0为假，非0为真 
关系操作符: != ==
逻辑操作符: && ||(并，或)(类python and or)
条件操作符: exp1 ? exp2 : exp3(三目操作符)
             真    输出  
             假           输出
逗号表达式:exp1, exp2, exp3, ...expn
下标引用，函数调用，结构成员:[] () . ->
//从左向右依次计算，整个表达式的结果是最后一个表达式的结果
             
 */
#include <stdio.h>








/* int Add(int a,int b)
{
    return a + b;
}
 */


int main()
{
/*    1 float a = 7/2.0;
    printf("%.1f\n",a);//保证有一个浮点数 */

/*    2 int flag = 0;
    if (!flag)
    {
        printf("hello");
    }
 */

/*     int a = 10;
    printf("%d\n",sizeof(a));
    printf("%d\n",sizeof a);
    printf("%d\n",sizeof(int));
    //三者等同
    int arr[10] = { 0 };//字符串才以\0做结尾
    printf("%d\n",sizeof(arr));//40,即10*4
    printf("%d\n",sizeof(arr)/sizeof(arr[0]));//此为arr内元素个数
     */

/*     int a = 10;
    int b = a++;//后置++，先使用，后++
    //则b = 10，a = 11
    int c =  ++a;
    //前置++，先++，后使用，用完后有c = a = 12
    a = (int)3.14;//字面浮点数默认为double
    return 0; */
/* 
    int a = 10;
    int b = 20;
    if (a || b)
    {
        printf("hehe");
    } */


/*     int a = 10;
    int b =20;
    int r = a > b ? a : b;
    printf("%d\n",r);
 */

/*     int a = 10;
    int b = 20;
    int c = 30;
    int d = (c= a-2,b = a+2);
    printf("%d\n",c);
    printf("%d\n",b);
    printf("%d\n",d); */

/*     int arr[10] = {1,2,3,4,5,6};//指定大小以创建，则[]内不是变量
    int a = 3;
    arr[a] = 20;//无所谓变量注意区分，访问元素时如此
    printf("%d\n",arr[3]); */



  




    return 0;
}



