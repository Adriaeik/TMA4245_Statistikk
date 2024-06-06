from PyPDF2 import PdfMerger
import os

# Get the path of the notebook directory
notebook_dir = os.path.dirname(os.path.abspath(__file__))

# Create a new PDF file object
merged_pdf = PdfMerger()

# Loop through all PDF files in the notebook directory
for file_name in os.listdir(notebook_dir):
    if file_name.endswith('.pdf'):
        # Add the PDF file to the merger object
        merged_pdf.append(open(os.path.join(notebook_dir, file_name), 'rb'))

# Save the merged PDF file
with open('merged.pdf', 'wb') as output_file:
    merged_pdf.write(output_file)