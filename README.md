## Subtitle Formating

A simple script to add some formatting (i.e. change the font color) of .srt subtitle files <br>

Why did I do it?<br>
First, I just wanted to practice the use of <b>RegEx</b> to parse the subtitle content into a dictionary<br>
Then I thought that it would be fun to make something with the content of the dict and then turn it back to a subtitle string.

(It assumes that the files are 'utf-8' encoded)


## Usage
<pre><code>$ python subtitle_formating.py [-h] [-c {red,green,blue,yellow}] source_file</pre></code>

For example: <code>$ python subtitle_formating.py sub_01.srt -c yellow</code> will result in a <code>sub_01_formated.srt</code> file with a new font color.



