import wx
import wx.lib.dialogs
import wx.stc as stc
import keyword
import os
from xml.dom.minidom import parse
import xml.dom.minidom

# Font face data depending on OS
faces = { 'times': 'Times New Roman',
              'mono' : 'Courier New',
              'helv' : 'Arial',
              'other': 'Comic Sans MS',
              'size' : 10,
              'size2': 8,
             }
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        # variables for file i/o
        self.dirname = ''
        self.filename = ''
        self.normalStylesFore = dict()
        self.normalStylesBack = dict()
        self.pythonStylesFore = dict()
        self.pythonStylesBack = dict()

        # editor options
        self.foldSymbols = 2
        self.lineNumbersEnabled = True
        self.leftMarginWidth = 25

        # Initialize the application Frame and create the Styled Text Control
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        self.control = stc.StyledTextCtrl(self, style=wx.TE_MULTILINE | wx.TE_WORDWRAP)


        # Set up the Python keywords for syntax highlighting
        self.control.SetLexer(stc.STC_LEX_CPP)
        self.control.SetKeyWords(0, " ".join(keyword.kwlist))

        # Set margins
        self.control.SetMargins(5,0) # 5px margin on left inside of text control
        self.control.SetMarginType(1, stc.STC_MARGIN_NUMBER) # line numbers column
        self.control.SetMarginWidth(1, self.leftMarginWidth) # width of line numbers column
                # Create the status bar at the bottom
        self.CreateStatusBar()
        self.UpdateLineCol(self) # show the line #, row # in status bar
        self.StatusBar.SetBackgroundColour((220,220,220))

        # Setting up the file menu
        filemenu = wx.Menu()
        menuNew = filemenu.Append(wx.ID_NEW, "&New", " Create a new document (Ctrl+N)")
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", " Open an existing document (Ctrl+O)")
        menuSave = filemenu.Append(wx.ID_SAVE, "&Save", " Save the current document (Ctrl+S)")
        menuSaveAs = filemenu.Append(wx.ID_SAVEAS, "Save &As", " Save a new document (Alt+S)")
        filemenu.AppendSeparator()
        menuClose = filemenu.Append(wx.ID_EXIT, "&Close", " Close the application (Ctrl+W)")

        # Setting up the Edit menu
        editmenu = wx.Menu()
        menuUndo = editmenu.Append(wx.ID_UNDO, "&Undo", " Undo last action (Ctrl+Z)")
        menuRedo = editmenu.Append(wx.ID_REDO, "&Redo", " Redo last action (Ctrl+Y)")
        editmenu.AppendSeparator()
        menuSelectAll = editmenu.Append(wx.ID_SELECTALL, "&Select All", " Select the entire document (Ctrl+A)")
        menuCopy = editmenu.Append(wx.ID_COPY, "&Copy", " Copy selected text (Ctrl+C)")
        menuCut = editmenu.Append(wx.ID_CUT, "C&ut", " Cut selected text (Ctrl+X)")
        menuPaste = editmenu.Append(wx.ID_PASTE, "&Paste", " Pasted text from the clipboard (Ctrl+V)")

        # Setting up the help menu
        helpmenu = wx.Menu()
        menuHowTo = helpmenu.Append(wx.ID_ANY, "&How To...", " Get help using the text editor (F1)")
        helpmenu.AppendSeparator()
        menuAbout = helpmenu.Append(wx.ID_ABOUT, "&About", " Read about the text editor and it's making (F2)")

        # Creating the menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        menuBar.Append(editmenu, "&Edit")
        menuBar.Append(helpmenu, "&Help")
        self.SetMenuBar(menuBar)

        # File events
        self.Bind(wx.EVT_MENU, self.OnNew, menuNew)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, menuSaveAs)
        self.Bind(wx.EVT_MENU, self.OnClose, menuClose)

        # Edit events
        self.Bind(wx.EVT_MENU, self.OnUndo, menuUndo)
        self.Bind(wx.EVT_MENU, self.OnRedo, menuRedo)
        self.Bind(wx.EVT_MENU, self.OnSelectAll, menuSelectAll)
        self.Bind(wx.EVT_MENU, self.OnCopy, menuCopy)
        self.Bind(wx.EVT_MENU, self.OnCut, menuCut)
        self.Bind(wx.EVT_MENU, self.OnPaste, menuPaste)

        # Help events
        self.Bind(wx.EVT_MENU, self.OnHowTo, menuHowTo)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)

        # Key bindings
        
        self.control.Bind(wx.EVT_KEY_UP, self.UpdateLineCol)
        self.control.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)

        # go ahead and display the application
        self.Show()

        # defaulting the style
        self.control.StyleSetSpec(stc.STC_STYLE_DEFAULT, "face:%(helv)s,size:%(size)d" % faces)
        self.control.StyleClearAll() # reset all to be like default

        # global default styles for all languages
        self.control.StyleSetSpec(stc.STC_STYLE_DEFAULT, "face:%(helv)s,size:%(size)d" % faces)
        self.control.StyleSetSpec(stc.STC_STYLE_LINENUMBER, "back:#C0C0C0,face:%(helv)s,size:%(size2)d" % faces)
        self.control.StyleSetSpec(stc.STC_STYLE_CONTROLCHAR, "face:%(other)s" % faces)
        self.control.StyleSetSpec(stc.STC_STYLE_BRACELIGHT, "fore:#FFFFFF,back:#0000FF,bold")
        self.control.StyleSetSpec(stc.STC_STYLE_BRACEBAD, "fore:#000000,back:#FF0000,bold")

        # Set all the theme settings
        self.ParseSettings("setty1.xml")
        self.SetStyling()
        self.getvariable()
        
    def getvariable(self):
        with open("preet.txt","r") as f:
            lines=f.readlines()
            for line in lines:
                words=line.split()
                for i,word in enumerate(words):
                     if word=="int":
                         print(words[i+1])
                     
    # Setting the styles
    def SetStyling(self):
        # Set the general foreground and background for normal and python styles
        pSFore = self.pythonStylesFore
        pSBack = self.pythonStylesBack
        nSFore = self.normalStylesFore
        nSBack = self.normalStylesBack

    
                # Python styles
        self.control.StyleSetBackground(stc.STC_STYLE_DEFAULT, nSBack["Main"])
        self.control.SetSelBackground(True, "#333333")

        # Default
        self.control.StyleSetSpec(stc.STC_C_DEFAULT, "fore:%s,back:%s" % (nSFore["Default"], nSBack["Default"]))
        self.control.StyleSetSpec(stc.STC_C_DEFAULT, "face:%(helv)s,size:%(size)d" % faces)

        # Operators
        self.control.StyleSetSpec(stc.STC_C_OPERATOR, "fore:%s,back:%s" % (nSFore["Operator"], nSBack["Operator"]))
        self.control.StyleSetSpec(stc.STC_C_OPERATOR, "bold,size:%(size)d" % faces)

        self.control.StyleSetSpec(stc.STC_C_COMMENTLINE, "fore:%s,back:%s" % (nSFore["Comment"], nSBack["Comment"]))
        self.control.StyleSetSpec(stc.STC_C_COMMENTLINE, "face:%(other)s,size:%(size)d" % faces)

        # Number
        self.control.StyleSetSpec(stc.STC_C_NUMBER, "fore:%s,back:%s" % (nSFore["Number"], nSBack["Number"]))
        self.control.StyleSetSpec(stc.STC_C_NUMBER, "size:%(size)d" % faces)

        # String
        self.control.StyleSetSpec(stc.STC_C_STRING, "fore:%s,back:%s" % (nSFore["String"], nSBack["Number"]))
        self.control.StyleSetSpec(stc.STC_C_STRING, "face:%(helv)s,size:%(size)d" % faces)

        # Identifiers
        self.control.StyleSetSpec(stc.STC_C_IDENTIFIER, "fore:%s,back:%s" % (nSFore["Identifier"], nSBack["Identifier"]))
        self.control.StyleSetSpec(stc.STC_C_IDENTIFIER, "face:%(helv)s,size:%(size)d" % faces)

        # Class name definition
        self.control.StyleSetSpec(stc.STC_C_GLOBALCLASS, "fore:%s,back:%s" % (nSFore["ClassName"], nSBack["ClassName"]))
        self.control.StyleSetSpec(stc.STC_C_GLOBALCLASS, "bold,underline,size:%(size)d" % faces)

        self.control.StyleSetSpec(stc.STC_C_WORD, "fore:%s,back:%s" % (nSFore["WORD"], nSBack["WORD"]))
        self.control.StyleSetSpec(stc.STC_C_WORD, "face:%(helv)s,size:%(size)d" % faces)
        
    # New document menu action
    def OnNew(self, e):
        # Empty the instance variable for current filename, and the main text box's content
        self.filename = ""
        self.control.SetValue("")

    # Open existing document menu action
    def OnOpen(self, e):
        # First try opening the existing file; if it fails, the file doesn't exist most likely
        try:
            dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
            if (dlg.ShowModal() == wx.ID_OK):
                self.filename = dlg.GetFilename()
                self.dirname = dlg.GetDirectory()
                f = open(os.path.join(self.dirname, self.filename), 'r')
                self.control.SetValue(f.read())
                f.close()
            dlg.Destroy()
        except:
            dlg = wx.MessageDialog(self, " Couldn't open file", "Error 009", wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()

    # Save the document menu action
    def OnSave(self, e):
        # First try just saving the existing file, but if that file doesn't 
        # exist it will fail, and the except will launch the Save As.
        try:
            f = open(os.path.join(self.dirname, self.filename), 'w')
            f.write(self.control.GetValue())
            f.close()
        except:
            try:
                # If regular save fails, try the Save As method.
                dlg = wx.FileDialog(self, "Save file as", self.dirname, "Untitled", "*.*", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
                if (dlg.ShowModal() == wx.ID_OK):
                    self.filename = dlg.GetFilename()
                    self.dirname = dlg.GetDirectory()
                    f = open(os.path.join(self.dirname, self.filename), 'w')
                    f.write(self.control.GetValue())
                    f.close()
                dlg.Destroy()
            except:
                pass

    # Save a new document menu action
    def OnSaveAs(self, e):
        try:
            dlg = wx.FileDialog(self, "Save file as", self.dirname, self.filename, "*.*", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
            if (dlg.ShowModal() == wx.ID_OK):
                self.filename = dlg.GetFilename()
                self.dirname = dlg.GetDirectory()
                f = open(os.path.join(self.dirname, self.filename), 'w')
                f.write(self.control.GetValue())
                f.close()
            dlg.Destroy()
        except:
            pass

    # Terminate the program menu action
    def OnClose(self, e):
        self.Close(True)

    # Undo event menu action
    def OnUndo(self, e):
        self.control.Undo()

    # Redo event menu action
    def OnRedo(self, e):
        self.control.Redo()

    # Select All text menu action
    def OnSelectAll(self, e):
        self.control.SelectAll()

    # Copy selected text menu action
    def OnCopy(self, e):
        self.control.Copy()

    # Cut selected text menu action
    def OnCut(self, e):
        self.control.Cut()

    # Paste text from clipboard menu action
    def OnPaste(self, e):
        self.control.Paste()

    # Toggle Line numbers menu action
    def OnToggleLineNumbers(self, e):
        if (self.lineNumbersEnabled):
            self.control.SetMarginWidth(1,0)
            self.lineNumbersEnabled = False
        else:
            self.control.SetMarginWidth(1, self.leftMarginWidth)
            self.lineNumbersEnabled = True

    # Show How To menu action
    def OnHowTo(self, e):
        # Simple display the How To from HowTo.txt in a modal window
        f = open("HowTo.txt", "r")
        msg = f.read()
        f.close()
        dlg = wx.lib.dialogs.ScrolledMessageDialog(self, msg, "How To:", size=(400, 500))
        dlg.ShowModal()
        dlg.Destroy()

    # Show About menu action
    def OnAbout(self, e):
        # Simple display a modal window telling about the application
        dlg = wx.MessageDialog(self, "An elegant, yet simple, text editor made with Python and wxPython.\nCreated by Zachary King.\n02/1/2015\nVersion 1.0.5\n", "About My Text Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    # Update the Line/Col in status bar
    def UpdateLineCol(self, e):
        line = self.control.GetCurrentLine() + 1
        col = self.control.GetColumn(self.control.GetCurrentPos())
        stat = "Line %s, Column %s" % (line, col)
        self.StatusBar.SetStatusText(stat, 0)

    # Left mouse up
    def OnLeftUp(self, e):
        # This way if you click on another position in the text box
        # it will update the line/col number in the status bar (like it should)
        self.UpdateLineCol(self)
        e.Skip()

    # Parses an XML settings file for styling and configuring the text editor
    def ParseSettings(self, settings_file):
        # Open XML document using minidom parser
        DOMTree = xml.dom.minidom.parse(settings_file)
        collection = DOMTree.documentElement # Root element
        
        # Get all the styles in the collection
        styles = collection.getElementsByTagName("style")
        for s in styles:
            item = s.getElementsByTagName("item")[0].childNodes[0].data
            color = s.getElementsByTagName("color")[0].childNodes[0].data
            side = s.getElementsByTagName("side")[0].childNodes[0].data
            sType = s.getAttribute("type")
            if sType == "python":
                if side == "Back": # background
                    self.normalStylesBack[str(item)] = str(color)
                else:
                    self.normalStylesFore[str(item)] = str(color)
            
app = wx.App(False)
frame = MainWindow(None, "Pyrite (beta)")
app.MainLoop()
