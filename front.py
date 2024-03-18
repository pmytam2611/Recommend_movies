from PIL import Image, ImageTk
import tkinter as tk


# Tạo cửa sổ chính
window = tk.Tk()
window.title("A Movie Recommender System")
window.geometry("1200x650")
entry = tk.Entry(width=10)

data = entry.get()
def on_enter_press(event):
    # Lấy dữ liệu từ ô nhập
    global data
    data = entry.get()
    print(f"Dữ liệu nhập là: {data}")


def on_ok_button_click():
    # Lấy dữ liệu từ ô nhập
    global data
    data = entry.get()
    print(f"Dữ liệu nhập là: {data}")

#Khu vực nhập dữ liệu

label = tk.Label(text="Vui lòng nhập vào mã người dùng:", font=("Arial", 12))

entry.pack()

# Bắt sự kiện nút Enter
entry.bind("<Return>", on_enter_press)

button = tk.Button(window, text="OK", command=on_ok_button_click)
button.pack()


uname = tk.Label(text="Người dùng 0", font=("Arial", 12))
#uimg = Image.open("user.png")
#resized_img = uimg.resize((50, 50), Image.LANCZOS)
#image = ImageTk.PhotoImage(resized_img)
#ulabel = tk.Label(window, image=image)

label.place(x=10, y=30)
entry.place(x=270, y=30)
button.place(x=350, y=30)
uname.place(x=1050, y=30)
#ulabel.place(x=1150, y=10)
#ulabel.place(x=1150, y=10)
#Banner
#bimg = Image.open("BG.png")
#resized_bimg = bimg.resize((1200, 275), Image.LANCZOS)
#bimage = ImageTk.PhotoImage(resized_bimg)
# blabel = tk.Label(window, image=bimage)

# blabel.place(x=0, y=100)

#canvas_width = bimage.width()
#canvas_height = bimage.height()
#canvas = Canvas(window, width=canvas_width, height=canvas_height)
#canvas.place(x=0, y=100)
# canvas.tkraise(blabel)
# canvas.create_image(0, 100, anchor="center",image=bimage)
#canvas.create_image(canvas_width // 2, canvas_height // 2, anchor="center", image=bimage)  # Or image_scaled

#rect_width = bimage.width()
#rect_height = bimage.height()

#rectangle = canvas.create_rectangle(0, 0, rect_width, rect_height, fill="#031839")  # Adjust fill color as needed
#canvas.itemconfig(rectangle, stipple="gray50")






# def print_data(self):
#     global data
#     print('Recommendation: ')
#     recommended_items = self.recommend(data)
#     if self.uuCF:
#         print('    Recommend item(s):', recommended_items, 'to user', data)
#     else:
#         print('    Recommend item', data, 'to user(s) : ', recommended_items)


# rs = CF(rate_train, k = 30, uuCF = 1)
# rs.fit()
# rs.print_data(self)

window.mainloop()