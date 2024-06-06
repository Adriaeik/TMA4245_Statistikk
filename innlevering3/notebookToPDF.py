import nbformat
from nbconvert.exporters.pdf import PDFExporter
from traitlets.config import Config
from nbconvert import PDFExporter
from nbconvert.preprocessors import ExecutePreprocessor
import traceback

def convert_notebook(notebook_path, exporter):
    try:
        with open(notebook_path, 'r', encoding='utf-8') as file:
            nb = nbformat.read(file, as_version=4)

        # Kjører notebooken før konvertering (valgfritt)
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        ep.preprocess(nb)

        body, _ = exporter.from_notebook_node(nb)

        pdf_path = notebook_path.replace('.ipynb', '.pdf')
        with open(pdf_path, 'wb') as file:
            file.write(body)
        print(f"PDF-filen er lagret som: {pdf_path}")
        return True
    except Exception as e:
        print(f"Feil under konvertering: {e}")
        traceback.print_exc()
        return False

def convert_notebook_with_custom_template(notebook_path, template_file):
    try:
        # Konfigurerer PDFExporter med den tilpassede templaten
        c = Config()
        c.PDFExporter.template_file = template_file

        # Oppretter en PDFExporter med den tilpassede konfigurasjonen
        pdf_exporter = PDFExporter(config=c)

        with open(notebook_path, 'r', encoding='utf-8') as file:
            nb = nbformat.read(file, as_version=4)

        # Kjører notebooken før konvertering (valgfritt)
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        ep.preprocess(nb)

        body, _ = pdf_exporter.from_notebook_node(nb)

        pdf_path = notebook_path.replace('.ipynb', '_custom.pdf')
        with open(pdf_path, 'wb') as file:
            file.write(body)
        print(f"PDF-filen med tilpasset template er lagret som: {pdf_path}")
        return True
    except Exception as e:
        print(f"Feil under konvertering med tilpasset template: {e}")
        traceback.print_exc()
        return False

def main():
    notebook_fil = "innlevering1.ipynb"  # Endre dette til navnet på din .ipynb-fil

    # Prøver først standard PDFExporter
    if not convert_notebook(notebook_fil, PDFExporter()):
        print("Prøver med en alternativ metode...")
        # Prøver med en tilpasset template
        if not convert_notebook_with_custom_template(notebook_fil, 'custom_template.tplx'):
            print("Kunne ikke konvertere notebooken med noen av metodene.")

# Kjører hovedfunksjonen
if __name__ == "__main__":
    main()
