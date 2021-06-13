import os
import sys

filename = sys.argv[1]

print(f"Extracting CSS out of {filename}...")
file = open(filename, 'r')

output_css = open("output_style.css", 'w')
output_html = open("output_html.html", 'w')

in_css = False

for line in file:
    if "</style" in line:
        in_css = False

    if in_css:
        output_css.write(line)
    else:
        output_html.write(line)

    if "<style" in line:
        in_css = True

output_css.flush()
output_css.close()

output_html.flush()
output_html.close()

file.close()

print("Done!")
