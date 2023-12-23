# flaskurlfor

#소개 
FlaskUrlFor 변환기는 로컬에서 개발한 웹 프로젝트의 HTML 파일을 Flask 앱으로 이식할 때 자산 경로를 url_for 형식으로 자동 변환해주는 도구입니다. HTML 파일을 드래그 앤 드롭하여 클립보드에 변환된 HTML 코드를 복사할 수 있습니다.
로컬 개발에사용된 프론트작업물의 경로를 flask용으로 바꿔주기 귀찮아서 만들었어요 누군가는 필요할 것 같아서 공유해요~
# 간혹 닌자와 호환안됨

변환전
```html
<link rel="shortcut icon" href="assets/images/favicon.ico">
```
변환후
```html
<link href="{{ url_for('static', filename='images/favicon.ico') }}" rel="shortcut icon">
```


## Dependencies Installation

You can install all required libraries using `pip`. Just copy and paste the following commands into your terminal:

```bash
pip install beautifulsoup4
pip install pyperclip
pip install tkinterdnd2
pip install lxml  # Optional
```
