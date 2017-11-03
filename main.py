from Views.MainView import MainView

class MainApp():
    def __init__(self):
        self.__master = MainView(send_handler = self.__send)

    def run(self):
        self.__master.mainloop()

    def __send(self):
        pass

if __name__ == "__main__":
    app = MainApp()
    app.run()