import rumps

class MyApp(rumps.App):
    def __init__(self):
        super(MyApp, self).__init__("MyApp", icon=None, menu=["选项 1", "选项 2"])

    @rumps.clicked("选项 1")
    def option_1(self, _):
        rumps.alert("你点击了选项 1")

    @rumps.clicked("选项 2")
    def option_2(self, _):
        rumps.alert("你点击了选项 2")

if __name__ == "__main__":
    MyApp().run()