import PyPDF4

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF4.PdfFileReader(file)
        
        # Initialize an empty string to store the extracted text
        extracted_text = ""
        
        # Iterate through each page in the PDF
        for page_num in range(pdf_reader.numPages):
            # Get a page object
            page = pdf_reader.getPage(page_num)
            # Extract text from the page
            extracted_text += page.extractText()
        
        return extracted_text

# Path to the PDF file
pdf_path = 'pdfw.pdf'

# Extract text from the PDF
text = extract_text_from_pdf(pdf_path)
print("type is: " , type(text))
# Print the extracted text
print(text)
