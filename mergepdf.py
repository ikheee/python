# PyPDF2 라이브러리를 불러옵니다.
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(pdf_list, output_filename):
    # PDF 파일을 쓰기 위한 객체를 생성합니다.
    pdf_writer = PdfWriter()

    # 각 PDF 파일에 대해 반복합니다.
    for pdf in pdf_list:
        # PDF 파일을 읽기 위한 객체를 생성합니다.
        with open(pdf, 'rb') as file:
            pdf_reader = PdfReader(file)

            # PDF 파일의 각 페이지를 가져와서 새로운 PDF 파일에 추가합니다.
            for page_num in range(len(pdf_reader.pages)):
                # 페이지를 가져옵니다.
                page = pdf_reader.pages[page_num]
                # 페이지를 새로운 PDF 파일에 추가합니다.
                pdf_writer.add_page(page)

    # 모든 페이지를 추가한 후 새로운 PDF 파일을 저장합니다.
    with open(output_filename, 'wb') as output:
        pdf_writer.write(output)

# 사용 예시
pdf_files = ['sample1.pdf', 'sample2.pdf']
merge_pdfs(pdf_files, 'merged.pdf')
