面向对象最重要的概念就是Class和Instance，必须牢记类是抽象的模版，比如Student类，而实例是根据类创建出来的一个个具体的对象，每个对象都拥有相同的方法，但是各自的数据可能不同
Python
class Student(obejct):
    pass
class 后面紧跟的是类名，也就是Student，通常大写开头，紧跟的(object)参数，表示类从哪个类继承下来的，通常如果没有合适的继承类，那么就用object类，这是所有类最终都会继承的类
定义好了Student 
