# *-* coding:utf-8 -*
import textwrap

import panflute as pf
import re
import sys
from javaformatter import JavaFormatter

def action(elem, doc):
    isInstance = isinstance(elem, pf.Table)
    sys.stderr.write(f"isinstance {isInstance}\n")
    if isInstance:
        # If there is only one row in the table, len(elem.content) will be equal to 1
        rows = len(elem.content)
        sys.stderr.write(f"length {rows}\n")
        if rows == 1:
            cols = [len(row.content) == 1 for row in elem.content]
            sys.stderr.write(f"cols {cols}\n")
            if all(cols):
                sys.stderr.write(f"Debug: Table found with content {elem.content}\n")
                # 正则表达式匹配单元格内容
                table_row = elem.content[0].content[0]
                sys.stderr.write(f"table row:{table_row} \n")
                # 取出表格中的容
                # stringify = pf.stringify(cellContent)
                # raw_latex = pf.stringify_with_left_padding(table_row)
                # text = pf.stringify(table_row, newlines=True)
                # raw_latex = r"\begin{{lstlisting}}[language={0}] {0} \end{{lstlisting}}".format(table_row.classes[0],
                #                                                                                 table_row.text)
                # raw_latex=table_row.content[0].content[0]
                # raw_latex = pf.stringify(table_row)
                # raw_latex = pf.stringify(table_row.content[0], preserve_formatting=True)
                text = pf.stringify(table_row.content[0])
                # table_content = ''
                # for para in table_row.content:
                #     #para_str = pf.tools.format_pandoc(para).strip()
                #     para_str = pf.stringify(para,newlines=False,normalize_whitespace=False)
                #     if para_str:
                #         table_content += para_str + '\n'
                #
                # text=table_content
                # text = textwrap.indent(text, "    ")

                sys.stderr.write(f"text:{text} \n")
                text = javalang.format_code(text)
                if text:
                    # 将单元格内容转换为代码格式
                    code = pf.CodeBlock(text,classes=['java'])
                    sys.stderr.write(f"Generated code: {code} \n")
                    return code
    # else:
    #     sys.stderr.write(f"not match\n")


def main(doc=None):
    run_filter = pf.run_filter(action, doc=doc, input_stream=sys.stdin, output_stream=sys.stdout)
    return run_filter


if __name__ == '__main__':
    main()
