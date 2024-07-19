## Overview
The objective of this project is to automate the book using the OpenAI GPT-4 model. The project aims to generate a structured book based on a series of predefined prompts, ultimately producing a formatted PDF document that includes a title page, synopsis, detailed chapter content and a review.

## Prerequisites
- **Python**
Download and Install latest version of Python on your system
https://www.python.org

- **Tex Live**
TeX Live is a cross-platform, free software distribution for the TeX typesetting system that includes major TeX-related programs, macro packages, and fonts.TeX Live is intended to be a straightforward way to get up and running with the TeX document production system. It provides a comprehensive TeX system with binaries for most flavors of Unix, including GNU/Linux and macOS, and also Windows.
Ensure you have TeX Live installed to compile LaTeX documents.
# Windows
Download and install TeX Live from the TeX Live website.
https://tug.org/texlive/doc/texlive-en/texlive-en.html

# MacOS:
Use MacTeX, which is a TeX Live distribution for Mac:
brew install --cask mactex

# Linux:
Install TeX Live using your package manager. For example, on Ubuntu:
sudo apt-get install texlive-full

## Install Dependencies
Install the necessary Python packages using the `requirements.txt` file:
pip install openai
pip install pylatex

- **openai** 
To interact with Open AI API for generating text content.
Need to sign up for the OPENAI account and subscribe to access GPT-4 model.

- **pylatex**
To generate LaTeX documents, which are then compiled into PDF files.

## set up the environment variable 
create a file in the root directory and add link of your OPENAI_API_KEY

## Features
- **Automated Content Generation**: Utilizes the OpenAI GPT-4 model to generate text content for the book based on predefined prompts.
- **Structured Content Creation**: Defines a clear structure for the book with chapters, each with specific titles and prompts.
- **Systematic Writing**: Implements a system message to guide the AI in generating empathetic and insightful content.
- **Supporting Content**: Generates a detailed synopsis and a comprehensive review of the book.
- **PDF Formatting**: Formats the generated content into a well-structured PDF document with a title page, synopsis section, chapter divisions, and a review section.
- **Reproducibility**: Provides configuration files and setup instructions to ensure the project can be easily set up and run by other users.


## Configuration

### config.json

Defines the structure and prompts for the book.

'''json
{
    "book_title": "Title_of_the_Book",
    "Synopsis": "Gives the brief info",
    "Chapters":[
        {
            "title": "Chapter 1",
            "prompts":[
                "Describe the childhood.....",
                "Introduce the family...."
            ]
        },
        //Additional Chapters
    ],
    "review": "Review of the book"
}

## How It Works 
- **Setup** 
Load environment variables and set up the OpenAI API key.
Define the structure and prompts for the book in config.json.

- **Generate Content**
Use content_generator.py to generate the text for each chapter based on predefined prompts.
Generate the book's synopsis using synopsis.py.
Create a review of the book using review.py.

- **Format PDF**
Use pdf_generator.py to compile the generated content into a PDF with a title page, chapters, and review.

- **Run and Automate**
Execute main.py to automate the entire process from content generation to PDF creation.


## Acknowledgements
OpenAI for providing the GPT-4 model.
- **OPEN AI DOCUMENTATION**
https://platform.openai.com/docs/guides/text-generation

The VS Code team for the development environment.

TeX Live for the LaTeX distribution used to compile the PDF.
