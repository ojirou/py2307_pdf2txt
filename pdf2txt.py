import os
import glob
import pdfplumber

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
        return text

def remove_empty_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if line.strip()]
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

def process_pdf_files():
    # フォルダのパスをユーザーに入力してもらう
    folder_path = input("指定フォルダのパスを入力してください: ")

    # 入力されたフォルダの存在を確認
    if not os.path.exists(folder_path):
        print("指定されたフォルダが存在しません。")
        return

    pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))
    if not pdf_files:
        print("指定されたフォルダに PDF ファイルが見つかりません。")
        return

    for file_path in pdf_files:
        # Extract text from pdf
        text = extract_text_from_pdf(file_path)

        # Generate output text file path
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        text_file_path = os.path.join(folder_path, file_name + ".txt")

        # Write text to file
        with open(text_file_path, "w", encoding="utf-8") as text_file:
            text_file.write(text)

        # Remove empty lines from text file
        remove_empty_lines(text_file_path)

# 処理を実行
process_pdf_files()
