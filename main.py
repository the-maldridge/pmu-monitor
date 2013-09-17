import procRead
import wx

class windowed(wx.Frame):
  def __init__(self, parent, title):
    self.monitor = procRead.power()
    wx.Frame.__init__(self, parent, title=title, size=(200,100))
    self.timer = wx.Timer(self)
    self.Bind(wx.EVT_TIMER, self.updateData(), self.timer)
    self.timeVal = wx.TextCtrl(self, style = wx.TE_READONLY)
    self.Show(True)
    self.timer.Start(1000)

  def updateData(self):
    self.monitor.printdata()
    #data = self.monitor.update()
    self.timeVal = "foo"


app = wx.App(False)
frame = windowed(None, "Power Monitor")
app.MainLoop()
