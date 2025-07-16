#!/usr/bin/env python3
"""
PDF Chinese OCR Tool
Extracts traditional Chinese text from PDF images and saves to text file.
"""

import sys
import os
from pathlib import Path
from pdf2image import convert_from_path
import pytesseract
from PIL import Image

def extract_images_from_pdf(pdf_path):
    """Convert PDF pages to images."""
    try:
        images = convert_from_path(pdf_path, dpi=300)
        return [(i + 1, img) for i, img in enumerate(images)]
    except Exception as e:
        print(f"Error converting PDF to images: {e}")
        return []

def ocr_chinese_text(image):
    """Extract traditional Chinese text from image using OCR."""
    # Try different language configurations
    configs = [
        r'--oem 3 --psm 6 -l chi_tra',  # Traditional Chinese
        r'--oem 3 --psm 6 -l chi_sim',  # Simplified Chinese
        r'--oem 3 --psm 6 -l eng+chi_tra',  # English + Traditional Chinese
        r'--oem 3 --psm 6 -l eng'  # Fallback to English
    ]
    
    for config in configs:
        try:
            text = pytesseract.image_to_string(image, config=config)
            if text.strip():
                return text.strip()
        except Exception as e:
            print(f"OCR config '{config}' failed: {e}")
            continue
    
    return ""

def process_pdf_to_text(pdf_path, output_path=None, max_pages=None):
    """Main function to process PDF and extract Chinese text."""
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file '{pdf_path}' not found.")
        return False
    
    if output_path is None:
        output_path = Path(pdf_path).stem + "_extracted.txt"
    
    print(f"Processing PDF: {pdf_path}")
    print(f"Output file: {output_path}")
    
    # Extract images from PDF
    images = extract_images_from_pdf(pdf_path)
    
    if not images:
        print("No images found in PDF.")
        return False
    
    print(f"Found {len(images)} images to process.")
    
    # Process each image with OCR
    all_text = []
    
    # Determine how many pages to process
    pages_to_process = len(images) if max_pages is None else min(max_pages, len(images))
    print(f"Processing {pages_to_process} pages...")
    
    for i in range(pages_to_process):
        page_num, image = images[i]
        print(f"Processing page {page_num}...")
        text = ocr_chinese_text(image)
        
        if text:
            all_text.append(f"\n{text}\n")
       #     all_text.append(f"=== Page {page_num} ===\n{text}\n")
       # else:
       #     all_text.append(f"=== Page {page_num} ===\n[No text detected]\n")
    
    # Save extracted text
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(all_text))
        
        print(f"Text extraction completed. Saved to: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

def main():
    """Command line interface."""
    if len(sys.argv) < 2:
        print("Usage: python pdf_chinese_ocr.py <pdf_file> [output_file] [max_pages]")
        print("Example: python pdf_chinese_ocr.py document.pdf extracted_text.txt")
        print("Example: python pdf_chinese_ocr.py document.pdf extracted_text.txt 20")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    max_pages = int(sys.argv[3]) if len(sys.argv) > 3 else None
    
    success = process_pdf_to_text(pdf_file, output_file, max_pages)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()