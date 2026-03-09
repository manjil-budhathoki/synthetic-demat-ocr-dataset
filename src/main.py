import os
import json

from generator import generate_record
from template_writer import fill_template
from pdf_converter import convert_to_pdf
from image_converter import pdf_to_images


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE = os.path.join(BASE_DIR,"template","demat_template.docx")

DOCX_DIR = os.path.join(BASE_DIR,"output","docx")
PDF_DIR = os.path.join(BASE_DIR,"output","pdf")
IMG_DIR = os.path.join(BASE_DIR,"output","images")
LABEL_DIR = os.path.join(BASE_DIR,"output","labels")

os.makedirs(DOCX_DIR,exist_ok=True)
os.makedirs(PDF_DIR,exist_ok=True)
os.makedirs(IMG_DIR,exist_ok=True)
os.makedirs(LABEL_DIR,exist_ok=True)


TOTAL_DOCS = 50


for i in range(TOTAL_DOCS):

    data = generate_record()

    name = f"demat_{i}"

    docx_path = os.path.join(DOCX_DIR,f"{name}.docx")

    fill_template(TEMPLATE,docx_path,data)

    convert_to_pdf(docx_path,PDF_DIR)

    pdf_path = os.path.join(PDF_DIR,f"{name}.pdf")

    with open(os.path.join(LABEL_DIR,f"{name}.json"),"w") as f:
        json.dump(data,f,indent=4)

    print("Generated:",name)