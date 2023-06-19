def generate_links(input_text):
    lines = input_text.split('\n')  # split the input text into lines
    book = lines[0]  # take the first line as the book title
    lines = lines[1:]  # update lines to contain the rest
    output_text = f'* [{book}]({book}/readme/README.md)\n'  # add the book title to the output text
    chapter = ''
    for line in lines:
        line = line.strip()
        # ignore lines that should not be included in the links
        if any(keyword in line for keyword in ['探究与发现', '阅读与思考', '信息技术应用']):
            continue
        if line.startswith('第') or line.startswith('学习总结报告') or line.startswith('附录') or line.startswith('引言'):  # this is a chapter title
            chapter = line
            output_text += f'    * [{line}]({book}/{line}/{line}.md)\n'
        elif line.strip() != '':  # this is a section title
            output_text += f'        * [{line}]({book}/{chapter}/{line}.md)\n'
    return output_text


# Open and read from the input.txt file
with open('input.txt', 'r', encoding='utf-8') as input_file:
    input_text = input_file.read()

# Generate the links
output_text = generate_links(input_text)

# Write the result to the output.txt file
with open('output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(output_text)
