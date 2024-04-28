from customtkinter import Tk, ttk

def on_combobox_change(event):
    selected_value = combobox.get()
    print(f"The selected value is: {selected_value}")

root = Tk()

# Create a combobox
combobox = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])

# Bind the '<<ComboboxSelected>>' event to the callback function
combobox.bind("<<ComboboxSelected>>", on_combobox_change)

combobox.pack()
root.mainloop()
