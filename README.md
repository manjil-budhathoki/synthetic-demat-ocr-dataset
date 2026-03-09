# Synthetic DEMAT OCR Dataset Generator

This project generates **synthetic DEMAT account documents** that resemble real Nepali Demat account statements.

The generator creates realistic structured documents that can be used to **train and test OCR or document AI systems**.

The pipeline produces:

* DOCX documents
* PDF documents
* PNG images (for OCR input)
* JSON ground-truth labels

This allows developers to build **table extraction and structured document recognition systems**.

---

## Example Document

The generated document contains fields such as:

* BOID
* Name
* Account Status
* Gender
* Date of Birth
* Citizenship Number
* PAN Number
* Contact Number
* Address
* Bank Name
* Account Number

All identifiers follow realistic formats used in Nepal’s capital market system.

---

## Project Structure

```
synthetic-demat-ocr-dataset/

template/
    demat_template.docx

output/
    docx/
    pdf/
    images/
    labels/

src/
    generator.py
    template_writer.py
    pdf_converter.py
    image_converter.py
    main.py
```

---

## Installation

Install dependencies:

```
pip install -r requirements.txt
```

On Linux you must install LibreOffice and Poppler:

```
sudo apt install libreoffice poppler-utils
```

---

## Running the Generator

Navigate to the source directory:

```
cd src
```

Run the generator:

```
python main.py
```

The system will generate **50 synthetic Demat account documents** by default.

---

## Output

The generated dataset will look like this:

```
output/

pdf/
    demat_0.pdf
    demat_1.pdf

images/
    demat_0_0.png
    demat_1_0.png

labels/
    demat_0.json
    demat_1.json
```

Each document includes a **matching JSON label file**, making the dataset ready for OCR training and evaluation.

---

## Use Cases

This dataset can be used for:

* OCR model training
* Table extraction experiments
* Document AI pipelines
* KYC document parsing research
* Layout-based NLP models such as LayoutLM

---

## Disclaimer

All generated data is synthetic and does not correspond to any real individuals or financial accounts.

---

## Author

Created for experimentation in **OCR and document AI systems**.
