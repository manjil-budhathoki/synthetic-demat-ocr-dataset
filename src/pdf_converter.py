import subprocess


def convert_to_pdf(docx_path, output_dir):

    command = [
        "libreoffice",
        "--headless",
        "--convert-to",
        "pdf",
        docx_path,
        "--outdir",
        output_dir
    ]

    subprocess.run(command, check=True)