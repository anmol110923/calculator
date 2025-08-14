import os
from PyPDF2 import PdfReader, PdfWriter

# Paths — update if your folder is elsewhere
base_path = os.path.dirname(__file__)  # current script folder
cover_path = os.path.join(base_path, "cover.pdf")
input_folder = os.path.join(base_path, "input_pdfs")
output_folder = os.path.join(base_path, "output_pdfs")

# Make output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Load the cover page
cover_pdf = PdfReader(cover_path)
cover_page = cover_pdf.pages[0]

# Process all PDFs in input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".pdf"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        writer = PdfWriter()
        writer.add_page(cover_page)

        reader = PdfReader(input_path)
        for page in reader.pages:
            writer.add_page(page)

        with open(output_path, "wb") as f_out:
            writer.write(f_out)

print("✅ All PDFs processed! Check the 'output_pdfs' folder.")
