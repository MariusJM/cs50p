from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()
    pdf.set_left_margin(40)
    pdf.set_font("helvetica", "B", 40)
    pdf.cell(0, 60, text="CS50 Shirtificate", align="C")
    pdf.image("shirtificate.png", 10, 60, 190, 190)
    pdf.set_font_size(30)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=45, y=150, text=f"{name} took CS50")

    # pdf.set_left_margin(60)
    # pdf.set_right_margin(60)

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
