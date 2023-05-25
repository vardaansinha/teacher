import glob
from nbconvert import MarkdownExporter
from nbconvert.utils.exceptions import ConversionException
import os

# Specify the directory where your Jupyter Notebook files are located
notebook_directory = "_notebooks"

# Specify the destination directory for the converted Markdown files
destination_directory = "_posts"

def convert_notebooks():
    notebook_files = glob.glob(f"{notebook_directory}/*.ipynb")
    markdown_exporter = MarkdownExporter()

    for notebook_file in notebook_files:
        try:
            # Convert each notebook file to Markdown
            (body, resources) = markdown_exporter.from_filename(notebook_file)
            # Generate the destination Markdown file name by replacing the extension
            destination_file = os.path.basename(notebook_file).replace(".ipynb", ".md")
            # Move the converted Markdown file to the destination directory
            destination_path = f"{destination_directory}/{destination_file}"
            with open(destination_path, "w") as file:
                file.write(body)
        except ConversionException as e:
            print(f"Conversion error for {notebook_file}: {str(e)}")

convert_notebooks()
