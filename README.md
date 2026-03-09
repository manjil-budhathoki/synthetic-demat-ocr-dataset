# Synthetic DEMAT OCR Dataset Generator

A Python-based system that generates synthetic Nepali DEMAT account documents for training OCR and document AI systems.

## Tech Stack

- **Python 3.8+** - Core programming language
- **python-docx** - DOCX document generation and manipulation
- **pdf2image** - PDF to image conversion
- **Pillow** - Image processing and manipulation
- **python-dotenv** - Environment configuration management

## System Overview

This generator creates realistic DEMAT account statements with:
- Structured document layouts (DOCX, PDF, PNG formats)
- Ground-truth JSON labels for each document
- Realistic Nepali financial identifiers (BOID, Citizenship numbers, PAN, etc.)
- 50 synthetic documents by default (configurable)

The pipeline converts documents through multiple formats while maintaining data consistency:
```
Template DOCX → Customized DOCX → PDF → PNG Images + JSON Labels
```

## Requirements

Create a `requirements.txt` file with:

```txt
python-docx==1.1.0
pdf2image==1.16.3
Pillow==10.1.0
python-dotenv==1.0.0
```

### System Dependencies (Linux)
```bash
sudo apt install libreoffice poppler-utils
```

## Quick Start

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Install system dependencies (Linux only):
```bash
sudo apt install libreoffice poppler-utils
```

3. Run the generator:
```bash
cd src
python main.py
```

## Output Structure

```
output/
├── pdf/          # Generated PDF documents
├── images/       # PNG images for OCR
└── labels/       # JSON ground-truth data
```

## Use Cases

- OCR model training and evaluation
- Document AI pipeline development
- Table extraction experiments
- KYC document parsing research

---

**Note**: All generated data is synthetic and does not correspond to real individuals or accounts.