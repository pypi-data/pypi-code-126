#! python3
# -*- coding: utf-8 -*-
import wx
import mwx
from mwx.graphman import Layer, Frame

"""
Note: Use class Panel(Layer):
      or, use @Frame.register to support DnD
"""
@Frame.register
class Panel(wx.Panel):
    def __init__(self, *args, **kwargs):
        print("kwargs =", kwargs)
        super().__init__(*args, **kwargs)
        ## wx.Panel.__init__(self, *args, **kwargs)
        
        b1 = wx.Button(self, wx.ID_OK, "OK")
        b2 = wx.Button(self, wx.ID_CANCEL, "Exit")
        btn = wx.Button(self, label="Hello, wxPython")
        
        self.SetSizer(
            mwx.pack(self,
                (b1, b2, btn),
                label="test",
                orient=wx.VERTICAL,
                style=(0, wx.ALIGN_CENTER | wx.ALL, 4),
            )
        )

if __name__ == "__main__":
    app = wx.App()
    frm = Frame(None)
    frm.load_plug(Panel, show=1, size=(100,100))
    plug = frm.get_plug('test_plug')
    try:
        import inspect
        print("plug =", plug)
        print("where(plug) =", where(plug))
    except:
        raise
    frm.shellframe.debugger.skip.remove(mwx.FSM.__module__)
    frm.Show()
    app.MainLoop()
