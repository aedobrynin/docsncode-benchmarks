# This script transforms exisiting projects' comments to docsncode
# comment blocks.
# It ignores some comments on purpose and the result project might
# not build.
# It processes only .c files.

import os
import sys

total_comments_processed = 0
total_files = 0
total_files_processed = 0
total_directories_processed = 0


def process_file(file_path):
    global total_comments_processed

    with open(file_path, 'r') as file:
        lines = file.readlines()

    processed_lines = []
    in_single_line_comment_block = False
    in_multiline_comment_block = False

    for i, line in enumerate(lines):
        if '/*' in line and '*/' in line:
            # Ignore multiline comments that take only one line
            processed_lines.append(line)
            continue

        if '//' in line and not in_multiline_comment_block:
            indx = line.find('//')
            is_comment = indx == 0 or line[:indx].isspace()
            if is_comment:
                if not in_single_line_comment_block:
                    processed_lines.append('// @docsncode\n')
                    in_single_line_comment_block = True
                    total_comments_processed += 1
                processed_lines.append(line)
                if i == len(lines) - 1:
                    processed_lines.append('// @docsncode\n')
                continue

        if '/*' in line:
            in_multiline_comment_block = True
            total_comments_processed += 1
            processed_lines.append(line[:line.find('/*')])
            processed_lines.append('/* @docsncode\n')
            processed_lines.append(line[line.find('/*'):].replace('/*', ''))
            continue

        if '*/' in line:
            in_multiline_comment_block = False
            processed_lines.append(line.replace('*/', ''))
            processed_lines.append('@docsncode */\n')
            continue

        if in_single_line_comment_block:
            processed_lines.append('// @docsncode\n')
            in_single_line_comment_block = False
            current_single_line_comment_block_indent = None

        if in_single_line_comment_block or in_multiline_comment_block:
            # Remove indent on purpose.
            # In order to make comment a simple Markdown paragraph
            processed_lines.append(line.lstrip())
        else:
            processed_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(processed_lines)


def process_directory(directory_path):
    global total_files_processed
    global total_files
    global total_directories_processed

    for dirpath, _, filenames in os.walk(directory_path):
        for filename in filenames:
            if filename.endswith('.c') or filename.endswith('.h'):
                file_path = os.path.join(dirpath, filename)
                process_file(file_path)
                total_files_processed += 1
            total_files += 1
        total_directories_processed += 1


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 docsncode_project_generator.py <path-to-project-dir>")
        sys.exit(1)

    path_to_project_dir = sys.argv[1]
    process_directory(path_to_project_dir)

    print('total comments processed:', total_comments_processed)
    print('total files processed:', total_files_processed)
    print('total files:', total_files)
    print('total directories processed:', total_directories_processed)
