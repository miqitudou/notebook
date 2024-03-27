#### import

##### module和package

- module算是一个组织单位，独立构成一个命名空间，常见的形式是.py文件
- python级别的概念，文件是操作系统层级的概念
- package是特殊的module，多了__path__
- 无论有没有__init__.py文件，一个文件夹都可以被python当作package使用

import是把文件系统里面的文件或者文件夹变成python的module或者package的过程



```python
import test

#1.他先会找python有没有叫test的内置module
#2.然后在sys.path里面的文件夹内寻找名叫test的module，按顺序找，sys.path一般是第一个就是当前文件夹，可以手动改。
#做完import test 之后 test可以作为一个变量使用，test是一个命名空间。
#只load一次，把module给缓存起来。
#根据test的名字拿到了一个module，再把这个module保存到了名叫test的变量里

#test有两个责任，1个是找到module，1个是变量名，可以把两个责任分开：
import test as t
#1.test负责找module 2.t为保存module的变量名

from test import A
#这里不会把test的module赋值给任何一个变量

import mypackage
#先回查看mypackage文件夹下有没有__init__.py文件，如果没有的话他就不会运行额外的代码，有就运行__init__.py

import mypackage.mymodule
#mypackage.mymodule被当作字符串在mypackage下寻找mymodule
#这是mypackage这个变量就会多一个mymodule的属性，并且mypackage这个变量会指向这个package

import mypackage.mymodule as m
#这时候m指向的是mypackage.mymodule这个module

```



**相对路径导入**

```python
from .util import f

class C:
    pass
#每一个相对路径导入，都是先找到它的绝对路径再import
```

