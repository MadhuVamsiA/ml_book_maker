import json
from pylatex import Document, Section, Command, NewPage, NoEscape
import subprocess

class PDFGenerator:
    def __init__(self, config_path, synopsis_path, chapters_content_path, review_path):
        try:
            with open(config_path, "r") as f:
                self.config = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error reading {config_path}: {e}")
            raise
        except FileNotFoundError as e:
            print(f"Configuration file not found: {e}")
            raise

        try:
            with open(synopsis_path, "r") as f:
                self.synopsis = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error reading {synopsis_path}: {e}")
            raise
        except FileNotFoundError as e:
            print(f"Synopsis file not found: {e}")
            raise
    

        try:
            with open(chapters_content_path, "r") as f:
                self.chapters_content = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error reading {chapters_content_path}: {e}")
            raise
        except FileNotFoundError as e:
            print(f"Chapters content file not found: {e}")
            raise

        try:
            with open(review_path, "r") as f:
                self.synopsis_review = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error reading {review_path}: {e}")
            raise
        except FileNotFoundError as e:
            print(f"Review file not found: {e}")
            raise

    def create_tex_file(self, filename='book.tex'):
        doc = Document()
        doc.preamble.append(Command('title', self.config['book_title']))
        doc.append(NoEscape(r'\maketitle'))
        doc.append(NewPage())
        doc.append(NoEscape(r'\pagestyle{empty}')) #Diable page numbering

        with doc.create(Section('Synopsis', numbering= False)):
            doc.append(self.synopsis['synopsis'])
            doc.append(NewPage())

        for chapter_title, content in self.chapters_content.items():
            with doc.create(Section(chapter_title, numbering=False)):
                doc.append(content)
                doc.append(NewPage()) #Start each chapter on a new page

        with doc.create(Section('Review', numbering= False)):
            doc.append(self.review['review'])
            doc.append(NewPage())

        doc.generate_tex(filename)

    def create_book(self):
        self.create_tex_file('book.tex')
        subprocess.run(["pdflatex","book.tex"], check=True)

def generate_pdf(config_path, synopsis_path, chapters_content_path, review_path):
    pdf_gen = PDFGenerator(config_path, synopsis_path, chapters_content_path, review_path)
    pdf_gen.create_book()



            


