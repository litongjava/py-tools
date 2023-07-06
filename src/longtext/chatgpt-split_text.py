def split_text(text, group_length):
    groups = []
    for i in range(0, len(text), group_length):
        group = text[i:i + group_length]
        groups.append(group)
    return groups


group_length = 4000
with open('input.txt', 'r', encoding='utf-8') as input_file:
    input_text = input_file.read()

# Generate the links
text_groups = split_text(input_text, group_length)
split_prompt = "I will split the content below there are several groups for you, the grouping rules are\n\
Group {i}: {content}\n\
Reply 'received' after receiving,No need to print text\n\
The text I provided may be incomplete or cut off \n"
# Write the result to the output.txt file
with open('output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(split_prompt)
    for i, group in enumerate(text_groups):
        print(i)
        output_file.write(f"Group {i + 1}: {group} \r\n")
