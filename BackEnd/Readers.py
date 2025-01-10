import PyPDF2
from docx import Document


def ReadDocx(file_path):
    document = Document(file_path)
    jobName = ""
    skills = ""
    for paragraph in document.paragraphs:
        if "Навыки" in paragraph.text:
            # Предполагаем, что навыки находятся в следующем параграфе
            skills_paragraph = paragraph.next_sibling
            if skills_paragraph and skills_paragraph.text:
                skills = skills_paragraph.text
                print(f"Навыки: {skills}")

        if "должность" in paragraph.text:
            # Предполагаем, что должность находится в следующем параграфе
            job_paragraph = paragraph.next_sibling
            if job_paragraph and job_paragraph.text:
                jobName = job_paragraph.text.splitlines()[0]
                print(f"Должность: {jobName}")

    # Ищем в таблицах
    for table in document.tables:
        for row_index, row in enumerate(table.rows):
            for cell in row.cells:
                if "Навыки" in cell.text:
                    if cell.text != row.cells[1].text:
                        skills = row.cells[1].text

                if "должность" in cell.text:
                    if row_index + 1 < len(table.rows):
                        next_row = table.rows[row_index + 1]
                        if next_row.cells:
                            jobName = next_row.cells[0].text.splitlines()[0]

    return jobName


def ReadPDF(file_path):
    jobName = ""
    skills = ""

    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text = page.extract_text()
            paragraphs = text.split('\n')

            for i, paragraph in enumerate(paragraphs):
                if "Навыки" in paragraph:
                    # Предполагаем, что навыки находятся в следующем параграфе
                    if i + 1 < len(paragraphs):
                        skills = paragraphs[i + 1]
                        print(f"Навыки: {skills}")

                if "должность" in paragraph:
                    # Предполагаем, что должность находится в следующем параграфе
                    if i + 1 < len(paragraphs):
                        jobName = paragraphs[i + 1].splitlines()[0]
                        print(f"Должность: {jobName}")

    return jobName
