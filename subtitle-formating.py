'''
A simple script to add some formatting (i.e. change the font color) of .srt subtitle files
Why did I do it?
Lots of free time and wanted to practice the use of RegEx

It assumes that the files are 'utf-8' encoded

By: Matheus Mendes dos Santos | matbaska@hotmail.com | matheus.mendes.santos@alumni.usp.br

'''

import os
import re
import argparse

from typing import Dict, List

from numpy import positive

def create_formated_subtitle(source_file: str, color: str, destination: str) -> None:
    
    with open(source_file, encoding='utf-8') as f:
        raw = f.read()



    
def dict_to_raw(dict_sub: Dict[str, List[str]]) -> str:
    '''
    Takes the formated dict and turn it back to the string subtitle
    '''
    pos = dict_sub['position']
    start = dict_sub['start_time']
    content = dict_sub['content']
    end = dict_sub['end_time']

    raw = str()
    for i in range(len(pos)):
        
        raw += '\n'.join([pos[i], start[i] + ' --> ' + end[i], content[i]])
        raw += '\n\n'
    print(raw)

def sub_to_dict(raw: str) -> Dict[str, List[str]]:
    
    '''
    Uses RegEx to separate the raw subtitle content into a dict with 4 keys:
    ´position´ : the position (or index?) of a particular subtitle
    ´start_time´ : when the sub will show up in the screen (HH:MM:SS,CCC)
    ´end_time´ : when the sub will disappear from the screen (HH:MM:SS,CCC)
    ´content´ : the content of that subtitle
    '''

    position = re.findall('(\d+)(?:\n\d\d:\d\d:\d\d,\d\d\d)', raw)
    start_time = re.findall('([\d:,]+)(?: -->)', raw)
    end_time = re.findall('(?:--> )([\d:,]+)', raw)
    content = re.findall('(?:\d\d:\d\d:\d\d,\d\d\d\n)([\s\S]+?(?=\n{2}|$))', raw, re.DOTALL)
    
    dict_sub = {'position' : position,
                'start_time' : start_time,
                'end_time' : end_time,
                'content' : content}

    return dict_sub


def paint_content(sub_content: List[str], color: str) -> List[str]:
    '''
    Uses ´color´ to change the format of each subtitle in ´sub_content´
    '''
    
    formated_content = ['<span style="color:{}">'.format(color) + c + '</span>' for c in sub_content]
    
    return formated_content



if __name__ == '__main__':
    # Create our argument parser
    parser = argparse.ArgumentParser(
        description='Script to change the font color of .srt subtitle files'
    )

    # Arguments
    #   - source_file: the source file to be formated
    #   - dest_file: the destination where the formated file should go
    #   - color: the new color of the subtitle

    parser.add_argument(
        'source_file',
        type=str,
        help='The location of the source'
    )

    parser.add_argument(
        '-c',
        '--color',
        type=str,
        help='',
        choices=['red', 'green', 'blue', 'yellow']
    )

    parser.add_argument(
        '-d',
        '--destination',
        type=str,
        help='Location of destination of file (default: source_file appended with ´_formated´)',
        default=None
    )

    args = parser.parse_args()
    
    s_file = args.source_file
    d_file = args.destination
    color = args.color
    
    # If the destination wasn't passed, then we assume we want
    # to create a new file based on the old one
    if d_file is None:
        file_path, file_extension = os.path.splitext(s_file)
        d_file = f'{file_path}_formated{file_extension}'
    

    #create_formated_subtitle(s_file, color, d_file)
s = '''
2045
02:15:35,878 --> 02:15:38,046
POR LEVANTAR FUNDOS lLEGAlS

2046
02:15:38,214 --> 02:15:42,050
6 DE ABRlL DE 1974
CHAPlN CONDENADO

2047
02:15:42,218 --> 02:15:47,055
12 DE ABRlL DE 1974
PORTER PEGA 30 DlAS

2048
02:15:47,223 --> 02:15:51,726
17 DE MAlO DE 1974
GEN. KLElNDlENST CONDENADO

2049
02:15:51,894 --> 02:15:54,729
4 DE JUNHO DE 1 974
COLSON CONDENADO

2050
02:15:54,897 --> 02:15:57,565


ADMlTE OBSTRUÇÃO À JUSTlÇA'''

dict_to_raw(sub_to_dict(s))