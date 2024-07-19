import content_generator
import synopsis
import review
import pdfgenerator
from configuration import CONFIG_PATH, SYNOPSIS_PATH, CHAPTERS_CONTENT_PATH, REVIEW_PATH



if __name__ == "__main__":
    #Generate synopsis
    synopsis.save_synopsis(CONFIG_PATH, SYNOPSIS_PATH)

    #Generate chapters content
    content_generator.save_chapters_content(CONFIG_PATH, CHAPTERS_CONTENT_PATH)

    #Generate  review
    review.save_review(CONFIG_PATH, REVIEW_PATH)

    #Genereate PDF
    pdfgenerator.generate_pdf(CONFIG_PATH, SYNOPSIS_PATH, CHAPTERS_CONTENT_PATH, REVIEW_PATH)
    