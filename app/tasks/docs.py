import PIL
import pytesseract

def extract_text_from_image(image_path: str) -> str:
    """
    Extracts text from an image using Tesseract OCR.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The extracted text from the image.
    """
    try:
        # Open the image file
        with PIL.Image.open(image_path) as img:
            # Use pytesseract to do OCR on the image
            text = pytesseract.image_to_string(img)
            return text
    except Exception as e:
        return f"Error extracting text: {e}"