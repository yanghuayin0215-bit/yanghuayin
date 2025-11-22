/* 
auto、break、case、char、const、continue、default、do、double、
else、enum、extern、float、for、goto、if、int、long、register、
return、short、signed、sizeof、static、struct、switch、typedef、
union、unsigned、void、volatile、while
关键字为内置的，不能自己创建
for         swith       const       enum--枚举          extern              
while       case        常属性      struct--结构体      声明外部符号
do while    一起                    union--联合体
break
一起

register    return    signed  unsigne     
寄存器      函数返回值  有符号的 无符号的
static      sizeof    typedof   void        
静态的      计算大小   类型重命名  无

变量的命名：1有意义 2字母数字下划线，无其他特殊字符，不能以数字开头
*/

#include <stdio.h>

int main()
{

    auto int a = 10;//被省略了，局部变量都是，自动跳出，销毁


    return 0;
}