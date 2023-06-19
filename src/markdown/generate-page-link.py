def generate_page_link(book_name, start_with, start, end):
    output_text = ''
    for i in range(start, end + 1):
        output_text += f'{i} \n![{i}](../../book/{book_name}/{start_with}_{i}.png)\n'

    return output_text


# 1
# ![1](../../book/人教版高中数学A版选修1-1/人教版高中数学A版选修1-1_1.png)
book_name = '人教版高中数学A版选修4-5'
page_start = 1
page_end = 61
output_text = generate_page_link(book_name, book_name, page_start, page_end)
# Write the result to the output.txt file
with open('output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(output_text)
