import tkinter as tk

class SharedPower(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #Here starts the interesting part.
        user_entry_text = tk.StringVar()
        search = tk.Entry(self, textvariable=user_entry_text)
        search.pack()

        def getText():
            user_text_stored = user_entry_text.get()
            user_text_show = tk.Label(self, text=user_text_stored)
            user_text_show.pack()
        button = tk.Button(self, text="Copy text to memory", command=getText)
        button.pack()
        #And here it ends.

if __name__ == "__main__":
    app = SharedPower()
    app.mainloop()