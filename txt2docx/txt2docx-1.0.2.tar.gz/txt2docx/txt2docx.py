from docx import Document
def txt2docx(txt_file_name,docx_file_name):
    text = open(txt_file_name, 'r+', encoding='utf-8').read()
    document = Document()

    document.add_paragraph(text)
    document.save(f'{docx_file_name}.docx')
