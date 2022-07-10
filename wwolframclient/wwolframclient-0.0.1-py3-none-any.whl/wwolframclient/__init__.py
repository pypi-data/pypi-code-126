from wolframclient.language.expression import WLFunction,WLSymbolFactory
from wolframclient.language import wl,wlexpr
from wolframclient.evaluation import WolframLanguageSession
import IPython,IPython.display

__all__ = ("wl", "wlexpr", "section", "wplot")

WLFunction.__add__=WLSymbolFactory.__add__=lambda*args:wl.Plus(*args)
WLFunction.__eq__=WLSymbolFactory.__eq__=lambda*args:wl.Equal(*args)
WLFunction.__floordiv__=WLSymbolFactory.__floordiv__=lambda*args:wl.Quotient(*args)
WLFunction.__ge__=WLSymbolFactory.__ge__=lambda*args:wl.GreaterEqual(*args)        
WLFunction.__gt__=WLSymbolFactory.__gt__=lambda*args:wl.Greater(*args)
WLFunction.__le__=WLSymbolFactory.__le__=lambda*args:wl.LessEqual(*args)
WLFunction.__lt__=WLSymbolFactory.__lt__=lambda*args:wl.LessThan(*args)
WLFunction.__mod__=WLSymbolFactory.__mod__=lambda*args:wl.Mod(*args)
WLFunction.__mul__=WLSymbolFactory.__mul__=lambda*args:wl.Times(*args)
WLFunction.__ne__=WLSymbolFactory.__ne__=lambda*args:wl.Unequal(*args)
WLFunction.__neg__=WLSymbolFactory.__neg__=lambda self:wl.Times(-1,self)
WLFunction.__pow__=WLSymbolFactory.__pow__=lambda*args:wl.Power(*args)
WLFunction.__radd__=WLSymbolFactory.__radd__=lambda*args:wl.Plus(*args)
WLFunction.__rfloordiv__=WLSymbolFactory.__rfloordiv__=lambda*args:wl.Quotient(*args)
WLFunction.__rmod__=WLSymbolFactory.__rmod__=lambda self,other:wl.Mod(other,self)
WLFunction.__rmul__=WLSymbolFactory.__rmul__=lambda*args:wl.Times(*args)
WLFunction.__rpow__=WLSymbolFactory.__rpow__=lambda self,other:wl.Power(other,self)
WLFunction.__rsub__=WLSymbolFactory.__rsub__=lambda self,other:wl.Plus(other,wl.Times(-1,self))
WLFunction.__rtruediv__=WLSymbolFactory.__rtruediv__=lambda self,other:wl.Times(other,wl.Power(self,-1))
WLFunction.__sub__=WLSymbolFactory.__sub__=lambda self,other:wl.Plus(self,wl.Times(-1,other))
WLFunction.__truediv__=WLSymbolFactory.__truediv__=lambda self,other:wl.Times(self,wl.Power(other,-1))
WLFunction.__getitem__=WLSymbolFactory.__getitem__=lambda*args:wl.Part(args[0],wl.Span(args[1].start if args[1].start!=None else wl.All,args[1].stop if args[1].stop!=None else wl.All,args[1].step if args[1].step!=None else wl.All) if type(args[1])==slice else args[1]) if type(args[1])!=tuple else wl.Part(args[0],*(wl.Span(i.start if i.start!=None else wl.All,i.stop if i.stop!=None else wl.All,i.step if i.step!=None else wl.All) if type(i)==slice else i for i in args[1]))

section=WolframLanguageSession()

if IPython.get_ipython()!=None:
    WLFunction._repr_latex_=WLSymbolFactory._repr_latex_=lambda self:"$"+section.evaluate(wl.ToString(self,wl.TeXForm))+"$"
    def wplot(expr,_type="SVG"):
        """_type=["SVG","JPEG","PNG"]"""
        if _type=="SVG":IPython.display.display_svg(section.evaluate(wl.ExportString(expr,_type)),raw=True)
        elif _type=="JPEG":IPython.display.display_jpeg(section.evaluate(wl.ExportByteArray(expr,_type)),raw=True)
        elif _type=="PNG":IPython.display.display_png(section.evaluate(wl.ExportByteArray(expr,_type)),raw=True)
else:
    _plotted=0
    def wplot(expr):
        global _plotted
        if not _plotted:section.evaluate(wlexpr("<< JavaGraphics`"))
        section.evaluate(expr)
        _plotted=1

if __name__=="__main__":
    import wolframclient.language.expression,os
    if not os.path.exists(wolframclient.language.expression.__file__+"i"):
        import tqdm
        tar={
            "RowBox[{":"}]",
            "StyleBox[":"]",
            "SubscriptBox[":"]",
            '"':'"'
        }
        def _func(x:str,outer=0):
            stack,s=[],0
            if not outer:x=x.replace(",","").replace(" ","")
            while s<len(x):
                xs=x[s:]
                if stack and xs.startswith(tar[stack[-1][1]]):
                    ps,pleft=stack.pop()
                    if pleft=='"':
                        tmp="".join([i if i!="," else "，" for i in x[ps+len(left):s]])
                    else:
                        if pleft=="StyleBox[":
                            tmp=_func(x[ps+len(pleft):s-6])
                            # ttmp=x[ps+len(pleft):s]
                            # ttmp=ttmp[:ttmp.rfind(',')]
                            # tmp=_func(ttmp)
                        else:    
                            tmp=_func(x[ps+len(pleft):s])
                    x=x[:ps]+tmp+"·"*(s+len(tar[pleft])-ps-len(tmp))+x[s+len(tar[pleft]):]
                else:
                    for left in tar:
                        if xs.startswith(left):
                            stack.append((s,left))
                            break
                s+=1
            return x
        def func(x:str):
            return _func(x.replace("\uf522","->"),1).replace("·","").replace("，",", ").replace("\\\\!\\(\\*\\",'"').replace("\\\\)\\ShowStringCharacters",'"').replace("\\)\\ShowStringCharacters",'"').replace("\\\\_","")
        with open(wolframclient.language.expression.__file__+"i","w",encoding="utf-8") as f:
            f.write("from typing import Any\nclass WLFunction:...\nclass WLSymbolFactory:\n")
            for i in tqdm.tqdm(section.evaluate(wlexpr('Names["System`*"]//Select[PrintableASCIIQ[#] && ! StringMatchQ[#, "$" ~~ ___] &]'))):
                if i!="True" and i!="False" and i!="None":
                    f.write("\tdef {}(*args: Any, **kwrags: Any):\n".format(i))
                    f.write('\t\t"""'+func(usage:=str(section.evaluate(wlexpr('Information[{}, "Usage"]'.format(i)))).replace("\uf7c1","").replace("\uf7c9","").replace("\uf7c8","").replace("\uf7c0","")).replace("\n","\\n\n\t\t")+'"""\n\n')
        section.stop()