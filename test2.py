"""
 * Project name(项目名称)：Python_eval函数和exec函数
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 14:52
 * Version(版本): 1.0
 * Description(描述)： 
 """

if __name__ == '__main__':
    a = 1
    exec("a = 2")  # 相当于直接执行 a=2
    print(a)
    a = exec("2+3")  # 相当于直接执行 2+3，但是并没有返回值，a 应为 None
    print(a)
    a = eval('2+3')  # 执行 2+3，并把结果返回给 a
    print(a)
