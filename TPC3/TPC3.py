import re

def markdown_to_html(md_text):
    md_text = re.sub(r'^# (.+)', r'<h1>\1</h1>', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^## (.+)', r'<h2>\1</h2>', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^### (.+)', r'<h3>\1</h3>', md_text, flags=re.MULTILINE)
    
    md_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', md_text)
    
    md_text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', md_text)
    
    md_text = re.sub(r'(?m)^\d+\. (.+)', r'<li>\1</li>', md_text)
    md_text = re.sub(r'(<li>.*?</li>\n?)+', lambda m: f"<ol>\n{m.group(0)}</ol>", md_text, flags=re.DOTALL)
    
    md_text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', md_text)
    
    md_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', md_text)
    
    return md_text

test_markdown = """
# Título Principal
## Subtítulo
### Sub-subtítulo
Este é um **exemplo** de texto com *itálico* e **negrito**.

1. Primeiro item
2. Segundo item
3. Terceiro item

Como pode ser consultado em [página da UC](http://www.uc.pt)

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com)
"""

html_result = markdown_to_html(test_markdown)
print("INPUT")
print(test_markdown)
print("----------------------------------------------------------------------------")
print("OUTPUT")
print(html_result)
