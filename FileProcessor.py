import base64
import pdfplumber


class FileProcessor:

    @staticmethod
    def encode_file_to_base64(file_path):
        with open(file_path, "rb") as file:
            return base64.b64encode(file.read()).decode('utf-8')

    @staticmethod
    def read_text_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    @staticmethod
    def read_pdf_as_text(file_path):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n\n"
        return text

    @staticmethod
    def process_files(files_text, files_images, files_pdf):
        info_texts = [FileProcessor.read_text_file(file) for file in files_text]
        encoded_base64_data = [FileProcessor.encode_file_to_base64(file) for file in files_images]
        pdf_texts = [FileProcessor.read_pdf_as_text(file) for file in files_pdf]

        return info_texts, encoded_base64_data, pdf_texts
