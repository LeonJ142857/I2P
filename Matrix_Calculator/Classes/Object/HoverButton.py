from tkinter import Button

# class to wrap Tkinter button so that it changes color dynamically according to cursor


class HoverButton(Button):
    # initialize object
    def __init__(self, master, **kw):
        # initialize super class
        Button.__init__(self, master=master, **kw)
        # set default background to background
        self.defaultBackground = self["background"]
        # bind self.on_enter with "<Enter>" event
        self.bind("<Enter>", self.on_enter)
        # bind self.on_leave with "<Leave>" event
        self.bind("<Leave>", self.on_leave)

    # change button background to active background when cursor is hovering on top of button
    def on_enter(self, e):
        self['background'] = self['activebackground']

    # reverts button background to default when cursor is leaving button
    def on_leave(self, e):
        self['background'] = self.defaultBackground

    # withdraw button from display
    def forget(self):
        Button.grid_forget(self)
