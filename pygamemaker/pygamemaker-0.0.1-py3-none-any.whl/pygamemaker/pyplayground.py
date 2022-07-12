import os
_coli = []
_classs = []
class _class:
    def __init__(self,name, obj):
        self.objs = [obj]
        _classs.append(self)
        self.name = name
    def __str__(self):
        return self.name
class obj:
    def __init__(self, x, y, dimx, dimy, color="⬛", objClass = None) -> None:
        self._coli = []
        for i in range(dimy):
            for a in range(dimx):
                self._coli.append((i + y, a + x,color))
        self._update()
        if objClass != None:
            if objClass in _classs:
                for i in _classs:
                    if str(i) != objClass:
                        i.objs.append(self)
                        break
            else:
                _cls = _class(objClass, self)
        self.x,self.y,self.dimx,self.dimy,self.color,self.oClass = x,y,dimx,dimy,color,objClass
        self.hitx1,self.hity1,self.hitx2,self.hity2 = x, y, x + dimx, y + dimy
    def _fix(self):
        for i in self._coli:
            _coli.remove(i)
    def _update(self):
        for i in self._coli:
            _coli.append(i)
    def goto(self,x,y):
        self._fix()
        self._coli = []
        for i in range(self.dimy):
            for a in range(self.dimx):
                self._coli.append((i + y, a + x,self.color))
        self._update()
        self.x,self.y = x,y
    def touching(self,obj=None,objClass=None):
        if objClass != None:
            for i in _classs:
                if str(i) == objClass:
                    for a in i.objs:
                        if (self.hitx1 <= a.hitx1 and self.hitx2 >= a.hitx1) or (self.hitx1 <= a.hitx2 and self.hity2 >= a.hitx2):
                            if (self.hity1 <= a.hity1 and self.hity2 >= a.hity1) or (self.hity1 <= a.hity2 and self.hity2 >= a.hity2):
                                return True
                    return False
        try:
            if (self.hitx1 <= obj.hitx1 and self.hitx2 >= obj.hitx1) or (self.hitx1 <= obj.hitx2 and self.hity2 >= obj.hitx2):
                if (self.hity1 <= obj.hity1 and self.hity2 >= obj.hity1) or (self.hity1 <= obj.hity2 and self.hity2 >= obj.hity2):
                    return True
        except AttributeError:
            raise Exception("Must enter a valid object or class")
        
        
    def left(self,am=1):
        self.goto(self.x - am,self.y)
    def right(self,am=1):
        self.goto(self.x + am,self.y)
    def up(self,am=1):
        self.goto(self.x,self.y - am)
    def down(self,am=1):
        self.goto(self.x,self.y + am)
class window:
    def __init__(self,dimx,dimy,bgcolor="⬜", clear=False) -> None:
        self.dimx,self.dimy,self.bgcolor,self.cou=dimx,dimy, bgcolor, clear
    def clearScreen(self):
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')
    def update(self):
        if self.cou:
            self.clearScreen()
        ie = 0
        _coli.sort()
        try:
            cury = _coli[0][0]
            curx = _coli[0][1]
            color = _coli[0][2]
            ie += 1
        except:
            cury = 0
            curx = 0
        for ycor in range(self.dimy):
            for xcor in range(self.dimx):
                if xcor == curx and ycor == cury:
                    print(color,end="")
                    try:
                        cury = _coli[ie][0]
                        curx = _coli[ie][1]
                        color = _coli[ie][2]
                        ie += 1
                    except:
                        cury = -1
                        curx = -1
                else:
                    print(self.bgcolor,end="")
                while ycor > cury or (xcor >= curx and cury == ycor):
                    try:
                        cury = _coli[ie][0]
                        curx = _coli[ie][1]
                        color = _coli[ie][2]
                        ie += 1
                    except:
                        cury = 0
                        curx = 0
                        break
            print()
if __name__ == "__main__":
    obj2 = obj(0,0,3,3,"🟪", objClass="cls1")
    obj3 = obj(5,5,1,1,objClass="cls1")
    obj1 = obj(0,0,3,3)
    wn = window(10,10, clear=False)
    wn.update()
    if obj1.touching(objClass="cls1"):
        print("touching")
    else:
        print("not touching")