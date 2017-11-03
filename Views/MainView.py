from tkinter import Tk, Label, Entry, N, S, E, W

class MainView(Tk):
    class Constants:
        title = "Twilio"
        heigth = 400
        width = 600
        message_heigth = 300
        center = N + S + E + W
        left = W
        event = "<Button-1>"
        phone_text = "Teléfono"
        message_text = "Mensaje"
        send_text = "Enviar ▶"
        number_of_rows = 5

    def __init__(self, send_handler=None):
        super().__init__()
        self.__send_handler = send_handler
        self.title(self.Constants.title)
        self.maxsize(width=self.Constants.width, height=self.Constants.heigth)
        self.minsize(width=self.Constants.width, height=self.Constants.heigth)
        self.__configure_grid()
        self.__configure_UI()

    def __configure_UI(self):
        pass

    def __configure_grid(self):
        pass