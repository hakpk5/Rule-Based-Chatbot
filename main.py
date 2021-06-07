import tkinter as tk
import window

app = tk.Tk()
user = tk.StringVar(app, value='', name='user')
loggedin = tk.BooleanVar(app, value=False, name='loggedin')


app.title("ChatBot")
app.config(height=400)
app.geometry("300x400")
app.resizable(False, False)

cnf = {'width': 20, 'underline': 0}

frame = tk.Frame(app)

l_btn = tk.Button(frame, text="LOGIN", **cnf,
                  command=lambda: window.login(app))
l_btn.pack()

r_btn = tk.Button(frame, text="SIGNUP", **cnf,
                  command=lambda: window.register(app))
r_btn.pack()

top_margin = app.winfo_reqheight() // 2 - l_btn.winfo_reqheight()
frame.pack(pady=(top_margin, 0))


from chatwindow import ChatWindow

win = None


def open_chatwindow():
    if loggedin.get():
        global win
        win = ChatWindow(app)
        win.grab_set()
        win.mainloop()


loggedin.trace('w', lambda a, b, c, e=None: open_chatwindow())

app.bind('<Alt-L>', lambda e: l_btn.invoke())
app.bind('<Alt-l>', lambda e: l_btn.invoke())
app.bind('<Alt-R>', lambda e: r_btn.invoke())
app.bind('<Alt-r>', lambda e: r_btn.invoke())

app.bind_class('Button', '<Return>', lambda e: e.widget.invoke())

app.mainloop()
