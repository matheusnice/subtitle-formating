
import re
import subtitle_formating

def test_regex():
    with open('sub2.srt', encoding='utf-8') as f:
        raw = f.read()

    position = re.findall('(\d+)(?:\n[\d:,]+)', raw)
    start_time = re.findall('([\d:,]+)(?: -->)', raw)
    end_time = re.findall('(?:--> )([\d:,]+)', raw)
    content = re.findall('(?:\d\d:\d\d:\d\d,\d\d\d\n)([\s\S]+?(?=\n{2}|$))', raw, re.DOTALL)

    return content

def test_writing():
    with open('test.txt', 'w') as f:
        f.write('TEST')