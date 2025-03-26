# https://github.com/UB-Mannheim/tesseract/wiki     <- Install Tesseract on windows if not installed already
# pip install pytesseract
# https://pypi.org/project/pytesseract/

import io
import pytesseract
from PIL import Image
from fastapi import FastAPI, File, UploadFile, HTTPException

# Specify the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = FastAPI()


@app.post("/ocr/")
async def ocr(file: UploadFile = File(...)):
    try:
        # Read the uploaded file
        content = await file.read()

        # Open the image file
        image = Image.open(io.BytesIO(content))

        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(image)

        # Write the extracted text to a file
        output_file_path = "extracted_text.txt"
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(text)

        return {"text": text, "file_path": output_file_path}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing the file: {str(e)}")
