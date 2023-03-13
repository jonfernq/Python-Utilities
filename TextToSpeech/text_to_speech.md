## Text-to-Speech (replacing non-alphanumeric characters before) 

> Write Python program to read English text from utf-8 file and create MP3 audio file using gTTS Python package. Remove non-alphanumeric characters such as found in Markdown from the text before passing it to gTTS:

```python
from gtts import gTTS

# Read the text from the file
with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Remove non-alphanumeric characters
text = ''.join(c for c in text if c.isalnum() or c.isspace())

# Create a gTTS object and save the audio file
tts = gTTS(text=text, lang='en')
tts.save('output.mp3')
``` 

In this example, we first open the UTF-8 file using open() and read the contents into the text variable. We replace any newline characters (\n) with spaces, as gTTS does not handle newlines well.

Next, we create a new gTTS object and pass in the text variable and the language code (en for English) as arguments. We then save the resulting audio to an MP3 file named output.mp3 using the save() method.

Yes, if there are non-alphanumeric characters such as Markdown in the file, they will be read by gTTS and included in the resulting MP3 audio file. However, it's worth noting that gTTS may not correctly pronounce or interpret certain Markdown or other non-alphanumeric characters. These characters can be removed from the text before passing it to gTTS.

The isalnum() method checks if a character is alphanumeric (i.e., a letter or a digit) and isspace() checks if a character is a whitespace character. Any characters that do not pass these checks are removed from the text using a list comprehension and the join() method.
