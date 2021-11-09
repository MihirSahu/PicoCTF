We can assume that the flag is hidden somewhere inside the image.
If we use a text editor and search for the flag, we won't find anything.
If we use exiftool we don't find anything interesting other than a few pieces of metadata.
After doing some research, it seems that files can be hidden inside other files by copying byte by byte instead of copying simply as lines of text.
We find a tool called 'binwalk' that allows us to extract these hidden files.
By repeatedly using 'binwalk -e <file>' on the file and the output, we get the text file with the flag picoCTF{ac0072c423ee13bfc0b166af72e25b61}
