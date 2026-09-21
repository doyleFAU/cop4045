def line_number(input_name: str, output_name: str) -> None:
    """Read input_name and write lines to output_name with line numbers."""
    try:
        infile = open(input_name, 'r')
        outfile = open(output_name, 'w')
        num = 1
##this writes the line number and then the first line
        for line in infile:
            outfile.write(str(num) + '. ' + line)
            num += 1
        infile.close()
        outfile.close()
    except Exception as err:
        print('Could not read or write the file.')
        print('Details:', err)
        raise

def parse_functions(filename: str) -> tuple:
    """Read a Python file and return info about each top-level function."""
    try:
        infile = open(filename, 'r')
        lines = infile.readlines()
        infile.close()
        result =[]
        i = 0
        while i < len(lines):
##uses the top level function only
            if lines [i].startswith('def '):
                start = i
                def_line_num = i + 1
                def_line = lines[i].split('#')[0].strip()
                header = def_line[4:].strip()
                right_paren = header.find(')')
                left_paren = header.find('(')
                func_name = header[:left_paren].strip()
                arg_list = header[left_paren + 1:right_paren].strip()
                i += 1
                end = i
                while end < len(lines):
                    if lines[end].startswith('def '):
                        break
                    if lines[end].strip() != '':

                        if not lines[end].startswith(' ') and not lines[end].startswith('\t'):
                            break
                    end += 1
                i = end
                code_parts = [def_line + '\n']
                j = start + 1
                while j < end:
                    body = lines[j]
                    stripped = body.strip()
                    if stripped != '' and not stripped.startswith('#'):
                        code_parts.append(body)
                    j += 1
                code_text = ''.join(code_parts)
##uses it by alphabetical names
                result.append((def_line_num, func_name, arg_list, code_text))
            else:
                i += 1
        result = tuple(sorted(result, key = lambda item: item[1]))
        return result
    except Exception as err:
        print('Problem parsing functions in file:', filename)
        print('Details:', err)
        raise


def main() -> None:
      """Test line_number and parse_functions on this file."""
      source = __file__
##makes sure ont to overwrite file
      numbered_file = source + '.numbered.txt'
      print('Part a)')
      line_number(source, numbered_file)
      print('Wrote', numbered_file)
      print()
      print('Part b)')
      funcs = parse_functions(source)
      print(funcs)
if __name__ == '__main__':
      main()

                
  
