import tkinter as tk
from tkinter import filedialog
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_image_to_pdf():
    # Ask the user to select an image file
    image_file = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])

    if image_file:
        # Create a PDF file with the same name as the image but with a .pdf extension
        pdf_file = image_file.split(".")[0] + ".pdf"

        # Open the image using Pillow
        image = Image.open(image_file)

        # Create a PDF canvas
        c = canvas.Canvas(pdf_file, pagesize=letter)

        # Calculate the dimensions of the image to fit the PDF page
        img_width, img_height = image.size
        pdf_width, pdf_height = letter
        scale = min(pdf_width / img_width, pdf_height / img_height)
        img_width *= scale
        img_height *= scale

        # Draw the image on the PDF canvas
        c.drawImage(image_file, 100, 100, width=img_width, height=img_height)

        # Save the PDF
        c.save()

        # Display a success message
        result_label.config(text=f"PDF saved as {pdf_file}")
    else:
        result_label.config(text="Image selection canceled")

# Create a GUI window
root = tk.Tk()
root.title("Image to PDF Converter")

# Create and configure GUI elements
convert_button = tk.Button(root, text="Convert Image to PDF", command=convert_image_to_pdf)
convert_button.pack(pady=20)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Start the GUI event loop
root.mainloop()
