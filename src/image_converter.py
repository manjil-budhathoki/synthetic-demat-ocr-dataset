from pdf2image import convert_from_path
import os


def pdf_to_images(pdf_path, output_folder, name):

    images = convert_from_path(pdf_path)

    paths = []

    for i, img in enumerate(images):

        path = os.path.join(output_folder, f"{name}_{i}.png")

        img.save(path)

        paths.append(path)

    return paths