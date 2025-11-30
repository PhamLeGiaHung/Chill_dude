from guizero import App, Text, Box, PushButton, Slider, ButtonGroup, TextBox, Combo

def dangky():
    # Lấy dữ liệu từ giao diện
    hoten = txtbox1.value
    caphoc = chon.value
    cao = chieucao.value
    email = txtbox2.value
    sdt = txtbox3.value
    gioitinh = btngroup.value

    # Ghi vào file
    with open("Thongtin.txt", "w", encoding="utf-8") as f:
        f.write(f"Họ và tên: {hoten}\n")
        f.write(f"Cấp học: {caphoc}\n")
        f.write(f"Chiều cao: {cao} cm\n")
        f.write(f"Email: {email}\n")
        f.write(f"Số điện thoại: {sdt}\n")
        f.write(f"Giới tính: {gioitinh}\n")

app = App(title="Thẻ Hội Viên", bg="lightblue")
boxdaica = Box(app, align="top")
box1 = Box(boxdaica)
box2 = Box(boxdaica)
box3 = Box(boxdaica)
box4 = Box(boxdaica)
box5 = Box(boxdaica)
box6 = Box(boxdaica)

txt1 = Text(box1, text="Họ và tên:", align="left", color="blue")
txtbox1 = TextBox(box1, align="right", multiline=True, width=30)

txt2 = Text(box2, text="Chọn cấp học:", align="left", color="blue")
chon = Combo(box2, options=["Tiểu học", "THCS", "THPT", "ĐH"])

txt3 = Text(box3, text="Chọn chiều cao (cm):", align="left", color="blue")
chieucao = Slider(box3, start=120, end=180)

txt4 = Text(box4, text="Email:", align="left", color="blue")
txtbox2 = TextBox(box4, align="right", multiline=True, width=30)

txt5 = Text(box5, text="SĐT:", align="left", color="blue")
txtbox3 = TextBox(box5, align="right", multiline=True, width=30)


txt6 = Text(box6, text="Chọn giới tính:", align="left", color="blue")
btngroup = ButtonGroup(box6, options=["Nam", "Nữ", "Khác"], horizontal=True, align="right")

btn = PushButton(app, text="Đăng ký", command=dangky)
btn.bg = "Blue"
btn.text_color = "White"

app.display()