'''
A simple script to add some formatting (i.e. change the font color) of .srt subtitle files
Why did I do it?
Just wanted to practice the use of RegEx to parse the subtitle content into a dictionary

It assumes that the files are 'utf-8' encoded

By: Matheus Mendes dos Santos | matbaska@hotmail.com | matheus.mendes.santos@alumni.usp.br

'''

import os
import re
import argparse
from typing import Dict, List


def create_formated_subtitle(source_file: str, color: str, destination: str) -> None:
    
    with open(source_file, encoding='utf-8') as f:
        old_sub = f.read()

    dict_sub = sub_to_dict(raw=old_sub)
    dict_sub['content'] = paint_content(dict_sub['content'], color=color)
    new_sub = dict_to_string(dict_sub=dict_sub)
    
    with open(destination, mode='w', encoding='utf-8') as f:
        f.write(new_sub)


def dict_to_string(dict_sub: Dict[str, List[str]]) -> str:
    '''
    Takes the formated dict and turn it back to the string subtitle
    '''
    pos = dict_sub['position']
    start = dict_sub['start_time']
    content = dict_sub['content']
    end = dict_sub['end_time']

    new_sub = str()
    for i in range(len(pos)):
        
        new_sub += '\n'.join([pos[i], start[i] + ' --> ' + end[i], content[i]])
        new_sub += '\n\n'
    
    return new_sub

def sub_to_dict(raw: str) -> Dict[str, List[str]]:
    '''
    Uses RegEx to separate the raw subtitle content into a dict with 4 keys:
    ´position´ : the position (or index) of a particular subtitle
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
        help='The name of the source file'
    )

    parser.add_argument(
        '-c',
        '--color',
        type=str,
        help='',
        choices=['red', 'green', 'blue', 'yellow']
    )

    args = parser.parse_args()
    
    source_file = args.source_file
    color = args.color
    file_path, file_extension = os.path.splitext(source_file)
    dest_file = f'{file_path}_formated{file_extension}'
    
    create_formated_subtitle(source_file, color, dest_file)