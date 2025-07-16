# PDF Chinese OCR

A Python script to extract traditional Chinese text from PDF images using OCR (Optical Character Recognition).

## Features

- Converts PDF pages to high-resolution images
- Performs OCR with multiple language fallbacks (Traditional Chinese, Simplified Chinese, English)
- Saves extracted text to UTF-8 encoded text files
- Supports processing entire PDFs or specific page ranges
- Handles errors gracefully with fallback configurations

## Requirements

- Python 3.6+
- Tesseract OCR with Chinese language support
- Required Python packages (see requirements.txt)

## Installation

1. Install Tesseract OCR and Chinese language packs:
   ```bash
   # macOS
   brew install tesseract tesseract-lang
   
   # Ubuntu/Debian
   sudo apt-get install tesseract-ocr tesseract-ocr-chi-tra tesseract-ocr-chi-sim
   
   # Windows
   # Download from: https://github.com/UB-Mannheim/tesseract/wiki
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage
```bash
python3 pdf_chinese_ocr.py <pdf_file>
```

### With Custom Output File
```bash
python3 pdf_chinese_ocr.py <pdf_file> <output_file>
```

### Process Specific Number of Pages
```bash
python3 pdf_chinese_ocr.py <pdf_file> <output_file> <max_pages>
```

### Examples
```bash
# Extract entire PDF
python3 pdf_chinese_ocr.py document.pdf

# Extract to specific output file
python3 pdf_chinese_ocr.py document.pdf extracted_text.txt

# Extract first 20 pages only
python3 pdf_chinese_ocr.py document.pdf output.txt 20
```

## Output

The script creates a text file containing the extracted Chinese text. Each page's text is separated by line breaks.

## Language Support

The script tries multiple OCR configurations in order:
1. Traditional Chinese (`chi_tra`)
2. Simplified Chinese (`chi_sim`)
3. English + Traditional Chinese (`eng+chi_tra`)
4. English fallback (`eng`)

## Performance Notes

- Processing time depends on PDF size and complexity
- High DPI (300) is used for better OCR accuracy
- Large PDFs may take considerable time to process
- Consider using the page limit option for testing

## Dependencies

- `pdf2image`: Convert PDF pages to images
- `pytesseract`: Python wrapper for Tesseract OCR
- `Pillow`: Python Imaging Library

## Troubleshooting

1. **"No module named 'fitz'" error**: Install `pdf2image` instead of `PyMuPDF`
2. **Tesseract language errors**: Ensure Chinese language packs are installed
3. **Long processing times**: Use page limit option or process in smaller batches
4. **Poor OCR quality**: Ensure PDF has clear, readable text

## License

This project is open source and available under the MIT License.