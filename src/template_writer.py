from docx import Document


def fill_template(template_path, output_path, data):

    doc = Document(template_path)

    table = doc.tables[0]

    for row in table.rows:

        key = row.cells[0].text.strip()

        if key in data:
            row.cells[1].text = str(data[key])

    doc.save(output_path)