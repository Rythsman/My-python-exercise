class Screen(object):

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        self._width = value

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._height*self._width

    
1. Python中属性的获取是按照从下到上的顺序来查找属性；
2. Python中的类和实例是两个完全独立的对象；
3. Python中的属性设置是针对对象本身进行的；
