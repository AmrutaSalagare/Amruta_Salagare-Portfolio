import PyPDF2

def extract_urls(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            if '/Annots' in page:
                annots = page['/Annots']
                for annot in annots:
                    annot_obj = annot.get_object()
                    if '/A' in annot_obj and '/URI' in annot_obj['/A']:
                        print(f"Page {page_num + 1}: {annot_obj['/A']['/URI']}")

extract_urls('Amruta_Resume.pdf')
