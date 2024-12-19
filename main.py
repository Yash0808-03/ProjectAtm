import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def pdf(text_file, output_pdf):
    pdf_canvas = canvas.Canvas(output_pdf, pagesize=letter)

    with open(text_file, "r") as file:
        y_coordinate = 750  # Starting y-coordinate for writing text
        for line in file:
            pdf_canvas.drawString(50, y_coordinate, line.strip())
            y_coordinate -= 15  # Move to the next line

    pdf_canvas.save()


def create_pdf_from_log(log_file, output_folder):
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    output_pdf = f"{output_folder}\\log_{current_date}.pdf"  # Construct output PDF file name

    if not os.path.exists(output_folder):  # Check if output folder exists
        os.makedirs(output_folder)  # Create the output folder if it doesn't exist

    if not os.path.exists(output_pdf):  # Check if PDF file for current date already exists
        pdf(log_file, output_pdf)

# read pin from user
upin = int(input("Enter your pin:\n"))

# Read pin from file
f = open("E:\\pin.txt", "r")
fpin = int(f.read())
f.close()

# Comparing pin
if (upin == fpin):
    f = open("E:\\balance.txt", "r")
    bal = int(f.read())
    f.close()
    print("Balance is :", bal)
    # users choice
    n = int(input("1.Withdraw 2.Deposit 3.Change pin 4.Show statement 5.Print statement to pdf\n"))

    if (n == 1):
        amt = int(input("Enter AMT to withdraw: "))
        bal = bal - amt
        print("Withdraw Successful\n")
        f = open("E:\\balance.txt", "w")
        f.write(str(bal))
        f.close()
        print("Balance is: ", bal)

        # Code for log
        f = open("E:\\log.txt", "a")
        s = "Withdraw of RS " + str(amt) + " on date " + str(datetime.datetime.now()) + "\n"
        f.write(str(s))
        f.close()

    elif (n == 2):
        amt = int(input("Enter AMT to Deposit: "))
        bal = bal + amt
        print("Deposit Successful\n")
        f = open("E:\\balance.txt", "w")
        f.write(str(bal))
        f.close()
        print("Balance is: ", bal)

        # Code for log
        f = open("E:\\log.txt", "a")
        s = "Deposit of RS " + str(amt) + " on date " + str(datetime.datetime.now()) + "\n"
        f.write(str(s))
        f.close()

    elif (n == 3):
        npin = int(input("Enter New pin: "))
        f = open("E:\\pin.txt", "w")
        f.write(str(npin))
        f.close()
        print("Pin change successful !")

        # Code for log
        f = open("E:\\log.txt", "a")
        s = "Pin changed on date " + str(datetime.datetime.now()) + "\n"
        f.write(str(s))
        f.close()

        # Code to print statement
    elif (n == 4):
        f = open("E:\\log.txt", "r")
        log = f.read()
        print(log)

    # Code to print statement into pdf
    elif (n == 5):
        log_file = "E:\\log.txt"
        output_folder = "E:\\pdf_logs"  # Output folder for PDF files
        create_pdf_from_log(log_file, output_folder)

else:
    print("Invalid pin...")