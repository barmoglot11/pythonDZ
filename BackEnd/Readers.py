from docx import Document


def ReadDocx(file_path):
    document = Document(file_path)

    # Переменные для хранения результатов
    found_text = False
    found_table = False

    # Ищем в параграфах
    for para in document.paragraphs:
        if "Навыки" in para.text:
            found_text = True
            print(f"Найден текст: '{para.text}'")

    # Ищем в таблицах
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                if "Навыки" in cell.text:
                    found_table = True
                    print(f"Найдена таблица с текстом: '{cell.text}'")

    # Проверяем, что было найдено
    if not found_text and not found_table:
        print("Раздел 'Навыки' не найден.")
    elif found_text:
        print("Раздел 'Навыки' найден в тексте.")
    if found_table:
        print("Раздел 'Навыки' найден в таблице.")


def ReaderPDF(file_path):
    pass
