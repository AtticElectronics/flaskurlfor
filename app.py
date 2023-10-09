import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import ttk, StringVar
from bs4 import BeautifulSoup
import pyperclip
import os


def drop(event):
    file_path = event.data.strip()
    assets_prefix = assets_var.get()

    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')
        tags = soup.find_all(['script', 'link', 'img'])
        total_tags = len(tags)
        progress_bar['maximum'] = total_tags

        for i, tag in enumerate(tags):
            attribute = None

            if tag.has_attr('src'):
                attribute = 'src'
            elif tag.has_attr('href'):
                attribute = 'href'
            else:
                continue

            asset_path = tag[attribute]
            if assets_prefix in asset_path:
                tag[attribute] = f"{{{{ url_for('static', filename='{asset_path.split(assets_prefix)[1]}') }}}}"

            progress_bar['value'] = i + 1
            progress_bar.update()

        pyperclip.copy(str(soup))
        copied_label.config(text='HTML이 클립보드에 복사되었습니다!')
        root.after(4000, clear_message)


def clear_message():
    copied_label.config(text='')
    progress_bar['value'] = 0


root = TkinterDnD.Tk()
root.title("FlaskUrlFor 변환기")

assets_var = StringVar()
assets_var.set('assets/')
assets_entry = tk.Entry(root, textvariable=assets_var, width=50)
assets_entry.pack(padx=20, pady=5, side='top')

drag_label = tk.Label(root, text='여기에 HTML 파일을 드래그 앤 드롭하세요.',
                      padx=20, pady=40, bg='lightgrey')
drag_label.pack(padx=20, pady=20, side='top', fill='both', expand='yes')

copied_label = tk.Label(root, text='', padx=20, pady=20)
copied_label.pack(padx=20, pady=0, side='top', fill='both', expand='yes')

progress_bar = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')
progress_bar.pack(padx=20, pady=20, side='top')

# 사용 설명 레이블 수정 (왼쪽 정렬, 검정 바탕, 흰색 글자)
instruction_label = tk.Label(
    root,
    text="대충설명\n"+
        '''
        변환 전 : <link rel="shortcut icon" href="assets/images/favicon.ico">
        '''+
        '''
        변환 후 : <link href="{{ url_for('static', filename='images/favicon.ico') }}" rel="shortcut icon" />
        '''+
         "\nLocalProject/\n....assets/\n........css/\n............style.css\n........js/\n............script.js\n....index.html\n\n"+
        "TO\n\n"+
         "FlaskProject/\n"+"....static/\n"+"........css/\n"+"............style.css\n"+"........js/\n"+"............script.js\n"+"....templates/\n"+"........index.html"
         ,
    padx=20, pady=20,
    bg='black', fg='white',  # 배경색, 글자색 설정
    justify='left'  # 왼쪽 정렬
)
instruction_label.pack(padx=20, pady=20, side='bottom', fill='both', expand='yes')

drag_label.drop_target_register(DND_FILES)
drag_label.dnd_bind('<<Drop>>', drop)

root.mainloop()
