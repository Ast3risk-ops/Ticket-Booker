from guizero import App, TextBox, Text
app = App(title="Plane Ticket Booker")
Text(app, text="Destination:")
destination = TextBox(app)
app.display()
