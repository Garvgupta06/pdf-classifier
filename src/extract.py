from pathlib import Path
import random
import pymupdf
import re
def normalize_text(text: str):
    text = text.replace('\t',' ')
    text = re.sub(r' +',' ',text)
    text = re.sub(r'\n+', '\n', text)
    return text.strip()

def extract_books():
    # extracts text from the books present in the books directory 
    input_dir = Path("D:\\pdf-classifier\\data\\books")
    output_dir = Path("D:\\pdf-classifier\\data_extracted\\books")
    output_dir.mkdir(parents=True, exist_ok=True)
    for pdf_path in input_dir.iterdir():
        if not pdf_path.is_file() or pdf_path.suffix.lower() != ".pdf":
            continue

        output_path = output_dir / f"{pdf_path.stem}.txt"
        if output_path.exists():
            print(f"skipping {pdf_path.name} (already extracted)")
            continue

        try:
            doc =  pymupdf.open(pdf_path)
            total_pages = doc.page_count
            
            pages_to_extract = min(50,total_pages)
            middle = total_pages // 2
            start_pages = max(0,middle - pages_to_extract //2)
            end_pages = min(total_pages,start_pages+pages_to_extract)
            extracted_text = []
            for page_num in range(start_pages, end_pages):
                page = doc[page_num]
                text = page.get_text()
                extracted_text.append(f"=== PAGE {page_num + 1} ===")
                extracted_text.append(text)
            doc.close()
            full_text = '\n'.join(extracted_text)
            normalized = normalize_text(full_text)

            output_path = output_dir / f"{pdf_path.stem}.txt"
            output_path.write_text(normalized, encoding = 'utf-8')
            print(f"extracted {pdf_path.name} -> {output_path.name}")
        except Exception as e:
            print(f"Error processing {pdf_path.name}: {e}")

def extract_papers():
    section_patterns = [
        r'^(Abstract)\s*$',
        r'^(Introduction)\s*$',
        r'^(Related Work|Background|Literature Review)\s*$',
        r'^(Approach|Method|Methods|Methodology)\s*$',
        r'^(Experiments?|Experimental Setup)\s*$',
        r'^(Results?|Findings)\s*$',
        r'^(Discussion)\s*$',
        r'^(Conclusion|Conclusions|Summary)\s*$',
        r'^(References|Bibliography)\s*$',
        r'^(Acknowledgments?)\s*$'
    ]
    combined_patterns = '|'.join(section_patterns)
    input_dir = Path("D:\\pdf-classifier\\data\\research-paper")
    output_dir = Path("D:\\pdf-classifier\\data_extracted\\papers")
    output_dir.mkdir(parents = True, exist_ok = True)
    for pdf_path in input_dir.iterdir():
        if not pdf_path.is_file() or pdf_path.suffix.lower()!=".pdf":
            continue
        output_path = output_dir / f"{pdf_path.stem}.txt"
        if output_path.exists():
            print(f"skipping {pdf_path.name} (already exists) ")
            continue

        try:
            total_text = []
            doc = pymupdf.open(pdf_path)
            total_pages = doc.page_count

            for pages in range(total_pages):
                page = doc[pages]
                text = page.get_text()

                lines= text.split('\n')
                processed_lines = []
                for line in lines:
                    stripped = line.strip()

                    if re.match(combined_patterns,stripped,re.IGNORECASE):
                        section_name = stripped.upper()
                        processed_lines.append(f"\n==={section_name}===")
                    else:
                        processed_lines.append(line)

                total_text.append('\n'.join(processed_lines))

            doc.close()

            full_text= '\n'.join(total_text)
            normalized = normalize_text(full_text)

            output_path.write_text(normalized,encoding = 'utf-8')
            print(f"Extracted {pdf_path.name} --> {output_path.name}")
        except Exception as e:
            print(f"Error processing {pdf_path.name}: {e}")


def extract_notes():
    input_dir = Path("D:\\pdf-classifier\\data\\notes")
    output_dir = Path("D:\\pdf-classifier\\data_extracted\\notes")
    output_dir.mkdir(parents = True,exist_ok  = True)
    for pdf_path in input_dir.iterdir():
        if not pdf_path.is_file() or pdf_path.suffix.lower() != ".pdf":
            continue
        output_path = output_dir / f"{pdf_path.stem}.txt"
        if output_path.exists():
            print(f"skipping {pdf_path.name} (already extracted)")
            continue

        try:
            doc = pymupdf.open(pdf_path)
            extracted_text = []
            total_pages = doc.page_count
            for pages in range(total_pages):
                page = doc[pages]
                text = page.get_text()
                extracted_text.append(f"=== Page {pages+1} ===")
                extracted_text.append(text)
            doc.close()

            full_text = '\n'.join(extracted_text)
            normalized = normalize_text(full_text)

            output_path.write_text(normalized,encoding = 'utf-8')
            print(f"Extracted {pdf_path.name} --> {output_path.name}")


        except Exception as e:
            print(f"Error processing {pdf_path.name}: {e}")


def extract_docs():
    input_dir = Path("D:\\pdf-classifier\\data\\official-docs")
    output_dir = Path("D:\\pdf-classifier\\data_extracted\\docs")
    output_dir.mkdir(parents = True,exist_ok  = True)
    for pdf_path in input_dir.iterdir():
        if not pdf_path.is_file() or pdf_path.suffix.lower() != ".pdf":
            continue
        output_path = output_dir / f"{pdf_path.stem}.txt"
        if output_path.exists():
            print(f"skipping {pdf_path.name} (already extracted)")
            continue

        try:
            doc = pymupdf.open(pdf_path)
            extracted_text = []
            total_pages = doc.page_count
            for pages in range(total_pages):
                page = doc[pages]
                text = page.get_text()
                extracted_text.append(f"=== Page {pages+1} ===")
                extracted_text.append(text)
            doc.close()

            full_text = '\n'.join(extracted_text)
            normalized = normalize_text(full_text)

            output_path.write_text(normalized,encoding = 'utf-8')
            print(f"Extracted {pdf_path.name} --> {output_path.name}")


        except Exception as e:
            print(f"Error processing {pdf_path.name}: {e}")


extract_books()
extract_papers()
extract_docs()
extract_notes()



        

