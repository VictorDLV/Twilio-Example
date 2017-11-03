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
        cellphone_label = Label(self)
        cellphone_label.grid(row=0, column=0, sticky=self.Constants.left)
        cellphone_label.configure(text=self.Constants.phone_text)

        self.__phone_input = Entry(self)
        self.__phone_input.grid(row=1, column=0, sticky=self.Constants.center)

        message_label = Label(self)
        message_label.grid(row=2, column=0, sticky=self.Constants.left)
        message_label.configure(text=self.Constants.message_text)

        self.__message_input = Entry(self)
        self.__message_input.grid(row=3, column=0, sticky=self.Constants.center)

        self.__send_button = Label(self)
        self.__send_button.grid(row=4, column=0, sticky=self.Constants.center)
        self.__send_button.configure(text=self.Constants.send_text)
        self.__send_button.bind(self.Constants.event, self.__did_tap_send)

    def __configure_grid(self):
        for index in range(self.Constants.number_of_rows):
            self.grid_rowconfigure(index, weight=True)

        self.grid_rowconfigure(3, minsize=self.Constants.message_heigth)
        self.grid_columnconfigure(0, weight=True)

    def __did_tap_send(self, event):
        if self.__send_handler is None:
            return

        if self.__phone_input.get() != "" and self.__message_input.get() != "":
            self.__send_handler(self.__phone_input.get(), self.__message_input.get())