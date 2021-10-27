
from subtitle_formating import *


def test_sub_to_dict():
    '''
    Testing if the script is parsing the subtitle into a dict correctly
    i.e. if all the lists are the same length
    '''
    for i in range(1,6):
        with open('sub_test_{:02}.srt'.format(i), encoding='utf-8') as f:
            sub = f.read()
        d = sub_to_dict(sub)
        
        assert len(d['position']) == len(d['start_time'])
        assert len(d['start_time']) == len(d['end_time'])
        assert len(d['end_time']) == len(d['content'])
        
        
def test_dict_to_string():
    '''
    Testing if the script is splitting and then reassembeling the original subtitle correctly
    '''
    for i in range(1,6):
        with open('sub_test_{:02}.srt'.format(i), encoding='utf-8') as f:
            sub = f.read()
        
        new_sub = dict_to_string(sub_to_dict(sub))

        assert new_sub == sub
    

def test_create_formated_subtitle():
    '''
    Testing if the whole damn thing works
    '''
    for i in range(1,6):
        sub_name = 'sub_test_{:02}.srt'.format(i)
        dest_name = 'sub_test_{:02}_formated.srt'.format(i)
        
        with open(sub_name, encoding='utf-8') as f:
            sub = f.read()
        
        create_formated_subtitle(sub_name, 'yellow', dest_name)