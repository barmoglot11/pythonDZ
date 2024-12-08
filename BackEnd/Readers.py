from docx import Document


def ReadDocx(file_path):
    document = Document(file_path)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text

    print("Find text : "+text)
