/*  1.字面常量
 2.const修饰的常变量
 3.define定义的标识符常量
 4.枚举常量 */
 
 #include <stdio.h>
/*int main()
{
    const int a = 10;//常变量const
    printf("%d\n",a);
    return 0;
} */


/* #define m 100
#define sd "as"
int main()
{
    printf("%d\n",m);
    int a = m;
    printf("%d\n",a);
    printf("%s\n",sd);

    return 0;
} */


/* enum color
{   
    red,
    green,
    blue

};

enum gender
{
    male,
    female,
    secret
};


int main()
{
    enum color c = red;
    enum gender d = female;
    printf("%d\n",d);
    printf("%d\n",c);//输出为序号0，1...
    return 0;
} */
/* #include <string.h>
int main()
{
    //char ch = 'w';//char为字符;
    //''内引起为字符，""内引起为字符串；
    char arr1[10] = "abc";
    char arr2[10] = {'a','b','c','d','\0'};
    
    //printf("%s\n",arr1);
    //printf("%s\n",arr2); 
    
    int len1 = strlen("abc");
    int len2 = strlen(arr1);
    int len3 = strlen(arr2);
    //strlen为库函数，头文件为string.h
    printf("%d\n",len3);
    return 0;

} */


//转义字符
//??) --> ] 可能部分编译器转义，可用\?
//表示打印符号的有\加? \ ' "
// \r表示回车 有些换行和回车有所区别
// \ddd表示8进制数，如：\130
// \xdd表示16进制数,如：\x60
//输出为ASCIL编码

//%d - 打印整形
//%c - 打印字符
//%s - 打印字符串
//%f - 打印float类型
//%lf - 打印double
//%zu - 打印sizeoff返回值

/* int main()
{
    printf("ab\\0c\tdef");
    printf("\a\a\a\a");
    printf("%c\n",'\130');
    printf("%c\n",'\x60');
    return 0;
    printf("%d\n",strlen("weee e"))输出为6.空格也算字符
} */

//if else语句 swich语句
/* int main()
{   
    int input = 0;
    printf("好好学习(1/0)？");
    scanf("%d",&input);
    if (input == 1)
    {
        printf("good");
    
    }
    else
    {
        printf("bad");
    }
    return 0;
} */

//while 循环
//for 循环
//do...while 循环

int main()
{
    int line = 0;
    printf("写代码");
    line++;

    while(line < 20000)
    {
        printf("xie%d\n",line);
        line++;
    }
    if (line >= 20000)
    {
        printf("good");
    }
    else
    {
        printf("come on");
    }
    return 0;
}