import os
import fitz  # PyMuPDF
from PIL import Image


def convert_pdf_to_images(pdf_directory, output_directory, image_format='png'):
    # Function code should be indented here
    # For example:
    print("This is the start of the function block.")

    # List all PDF files in the specified directory
    pdf_files = [f for f in os.listdir(pdf_directory) if f.lower().endswith('.pdf')]

    for pdf_file in pdf_files:
        # Open the PDF file
        pdf_path = os.path.join(pdf_directory, pdf_file)
        pdf = fitz.open(pdf_path)
        
        for page_num in range(len(pdf)):
            # Get the page
            page = pdf[page_num]

            # Render page to an image
            pix = page.get_pixmap()

            # Construct the output image filename
            output_image_filename = f'{os.path.splitext(pdf_file)[0]}_page_{page_num + 1}.{image_format}'

            # Save the image
            pix.save(os.path.join(output_directory, output_image_filename))

        # Close the PDF after processing
        pdf.close()

# Usage
pdf_directory = '/Users/jahanzeb/Desktop/Blueprint_code/s'
output_directory = '/Users/jahanzeb/Desktop/Blueprint_code/labels'
convert_pdf_to_images(pdf_directory, output_directory)

