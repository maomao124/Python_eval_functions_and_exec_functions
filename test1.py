"""
 * Project name(项目名称)：Python_eval函数和exec函数
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 14:44
 * Version(版本): 1.0
 * Description(描述)： eval() 和 exec() 函数的功能是相似的，都可以执行一个字符串形式的 Python 代码,
 相当于一个 Python 的解释器。二者不同之处在于，eval() 执行完要返回结果，而 exec() 执行完不返回结果

 eval() 函数的语法格式为：
eval(expression, globals=None, locals=None, /)

而 exec() 函数的语法格式如下：
exec(expression, globals=None, locals=None, /)

expression：这个参数是一个字符串，代表要执行的语句 。该语句受后面两个字典类型参数 globals 和 locals 的限制，
只有在 globals 字典和 locals 字典作用域内的函数和变量才能被执行。
globals：这个参数管控的是一个全局的命名空间，即 expression 可以使用全局命名空间中的函数。
如果只是提供了 globals 参数，而没有提供自定义的 __builtins__，则系统会将当前环境中的 __builtins__ 复制到自己提供的 globals 中，
然后才会进行计算；如果连 globals 这个参数都没有被提供，则使用 Python 的全局命名空间。
locals：这个参数管控的是一个局部的命名空间，和 globals 类似，当它和 globals 中有重复或冲突时，
以 locals 的为准。如果 locals 没有被提供，则默认为 globals。
 """

if __name__ == '__main__':
    dic = {}  # 定义一个字典
    dic['b'] = 3  # 在 dic 中加一条元素，key 为 b
    print(dic.keys())  # 先将 dic 的 key 打印出来，有一个元素 b
    exec("a = 4", dic)  # 在 exec 执行的语句后面跟一个作用域 dic
    print(dic.keys())  # exec 后，dic 的 key 多了一个
    for i in (dic["__builtins__"]):
        print(i)

    a = 10
    b = 20
    c = 30
    g = {'a': 6, 'b': 8}  # 定义一个字典
    t = {'b': 100, 'c': 10}  # 定义一个字典
    print(eval('a+b+c', g, t))  # 定义一个字典 116
    print(g)
    print(t)
