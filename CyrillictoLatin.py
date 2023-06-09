import codecs
import sys

file_name = sys.argv[1]

# Open the input file in read mode and output file in write mode
with codecs.open(file_name, 'r', encoding='utf-8') as input_file, codecs.open(file_name[:-4]+".lat.txt", 'w', encoding='utf-8') as output_file:
  # Read the entire contents of the input file
  text = input_file.read()

  # Use a dictionary to map Cyrillic characters to their Latin counterparts
  cyrillic_to_latin = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Ђ': 'Đ', 'Е': 'E', 'Ж': 'Ž', 'З': 'Z', 'И': 'I',
    'Ј': 'J', 'К': 'K', 'Л': 'L', 'Љ': 'Lj', 'М': 'M', 'Н': 'N', 'Њ': 'Nj', 'О': 'O', 'П': 'P', 'Р': 'R',
    'С': 'S', 'Т': 'T', 'Ћ': 'Ć', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'Č', 'Џ': 'Dž', 'Ш': 'Š',
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'ђ': 'đ', 'е': 'e', 'ж': 'ž', 'з': 'z', 'и': 'i',
    'ј': 'j', 'к': 'k', 'л': 'l', 'љ': 'lj', 'м': 'm', 'н': 'n', 'њ': 'nj', 'о': 'o', 'п': 'p', 'р': 'r',
    'с': 's', 'т': 't', 'ћ': 'ć', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'č', 'џ': 'dž', 'ш': 'š'

  }

  # Loop through the text and replace each Cyrillic character with its Latin counterpart
  translated_text = ''
  for char in text:
    if char in cyrillic_to_latin:
      translated_text += cyrillic_to_latin[char]
    else:
      translated_text += char

  # Write the translated text to the output file
  output_file.write(translated_text)
