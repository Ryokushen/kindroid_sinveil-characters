#!/usr/bin/env python3
"""
OCR PDF Text Extraction Script for macOS
Extracts text from PDFs using embedded text (pdfplumber) or OCR (pytesseract)
"""

import sys
import os
import argparse
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are available"""
    try:
        import pdfplumber
        import pytesseract
        from pdf2image import convert_from_path
        from PIL import Image
        return True
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("\nTo install required packages:")
        print("pip3 install --user pdfplumber pytesseract pdf2image pillow")
        print("\nMake sure tesseract and poppler are installed via Homebrew:")
        print("brew install tesseract poppler")
        return False

def has_embedded_text(pdf_path, page_num=0):
    """Check if a PDF page has embedded/selectable text"""
    try:
        import pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            if page_num >= len(pdf.pages):
                return False
            page = pdf.pages[page_num]
            text = page.extract_text()
            # Consider it has embedded text if we get more than just whitespace
            return text and len(text.strip()) > 10
    except Exception as e:
        print(f"Error checking embedded text: {e}")
        return False

def extract_text_pdfplumber(pdf_path):
    """Extract text using pdfplumber (for PDFs with embedded text)"""
    import pdfplumber
    
    extracted_text = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                print(f"--- Page {i+1} ---")
                text = page.extract_text()
                if text:
                    print(text)
                    extracted_text.append(f"--- Page {i+1} ---\n{text}\n")
                else:
                    print("[No text found on this page]")
                    extracted_text.append(f"--- Page {i+1} ---\n[No text found on this page]\n")
    except Exception as e:
        print(f"Error with pdfplumber extraction: {e}")
        return None
    
    return "\n".join(extracted_text)

def extract_text_ocr(pdf_path):
    """Extract text using OCR (for image-based PDFs)"""
    from pdf2image import convert_from_path
    import pytesseract
    
    extracted_text = []
    try:
        # Convert PDF to images
        print("Converting PDF to images...")
        images = convert_from_path(pdf_path, dpi=300)
        
        for i, image in enumerate(images):
            print(f"--- Page {i+1} ---")
            print("Processing with OCR...")
            
            # Perform OCR on the image
            text = pytesseract.image_to_string(image, lang='eng')
            
            if text.strip():
                print(text)
                extracted_text.append(f"--- Page {i+1} ---\n{text}\n")
            else:
                print("[No text detected via OCR on this page]")
                extracted_text.append(f"--- Page {i+1} ---\n[No text detected via OCR on this page]\n")
                
    except Exception as e:
        print(f"Error with OCR extraction: {e}")
        return None
    
    return "\n".join(extracted_text)

def extract_pdf_text(pdf_path):
    """Main extraction function that chooses the best method"""
    if not os.path.exists(pdf_path):
        print(f"Error: File {pdf_path} does not exist")
        return None
    
    print(f"Processing PDF: {pdf_path}")
    
    # Check if PDF has embedded text by sampling first page
    if has_embedded_text(pdf_path, 0):
        print("PDF has embedded text - using pdfplumber")
        return extract_text_pdfplumber(pdf_path)
    else:
        print("PDF appears to be image-based - using OCR")
        return extract_text_ocr(pdf_path)

def main():
    parser = argparse.ArgumentParser(description='Extract text from PDF using OCR or embedded text extraction')
    parser.add_argument('pdf_file', help='Path to the PDF file')
    parser.add_argument('-o', '--output', help='Output file path (optional)')
    parser.add_argument('--force-ocr', action='store_true', help='Force OCR even if embedded text is detected')
    
    args = parser.parse_args()
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    pdf_path = args.pdf_file
    
    # Extract text
    if args.force_ocr:
        print("Forcing OCR extraction...")
        extracted_text = extract_text_ocr(pdf_path)
    else:
        extracted_text = extract_pdf_text(pdf_path)
    
    if extracted_text is None:
        print("Failed to extract text from PDF")
        sys.exit(1)
    
    # Save to file if output specified
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(extracted_text)
            print(f"\nText saved to: {args.output}")
        except Exception as e:
            print(f"Error saving to file: {e}")

if __name__ == "__main__":
    main()
