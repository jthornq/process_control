import wx
import settings
import functions as pf

ai_settings = settings.Settings()

USE_WIT = False

AppBaseClass = wx.App
if USE_WIT:
    from wx.lib.mixins.inspection import InspectableApp
    AppBaseClass = InspectableApp

class MyFrame(wx.Frame):
    """
    This is MyFrame.  It just shows a few controls on a wxPanel,
    and has a simple menu.
    """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title)

        # Create the menubar
        menuBar = wx.MenuBar()

        # and a menu
        menu = wx.Menu()

        # add an item to the menu, using \tKeyName automatically
        # creates an accelerator, the third param is some help text
        # that will show up in the statusbar
        menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Exit this simple sample")

        # bind the menu event to an event handler
        self.Bind(wx.EVT_MENU, self.OnTimeToClose, id=wx.ID_EXIT)

        # and put the menu on the menubar
        menuBar.Append(menu, "&File")
        self.SetMenuBar(menuBar)

        self.CreateStatusBar()

        panel = wx.Panel(self)

        text = wx.StaticText(panel, -1, "Hello World!  Welcome to wxPython.")
        text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        text.SetSize(text.GetBestSize())
        btn = wx.Button(panel, -1, "Close")
        funbtn = wx.Button(panel, -1, "Just for fun...")

        self.Bind(wx.EVT_BUTTON, self.OnTimeToClose, btn)
        self.Bind(wx.EVT_BUTTON, self.OnFunButton, funbtn)

        # Use a sizer to layout the controls, stacked vertically and with
        # a 10 pixel border around each
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text, 0, wx.ALL, 10)
        sizer.Add(btn, 0, wx.ALL, 10)
        sizer.Add(funbtn, 0, wx.ALL, 10)
        panel.SetSizer(sizer)
        panel.Layout()


        self.SetSize(ai_settings.window_height, ai_settings.window_width)
        self.Centre()
        self.SetTitle('For glory!')
        self.Show(True)

    def OnTimeToClose(self, evt):
        print("See ya later!")
        self.Close()

    def OnFunButton(self, evt):
        pf.create_new_table()



class MyApp(AppBaseClass):
    def OnInit(self):
        frame = MyFrame(None, "Simple wxPython App")
        self.SetTopWindow(frame)

        print("Print statements go to this stdout window by default.")
        if USE_WIT:
            print("Press Ctrl-Alt-I (Cmd-Opt-I on Mac) to launch the WIT.")
            self.InitInspection()

        frame.Show(True)
        return True