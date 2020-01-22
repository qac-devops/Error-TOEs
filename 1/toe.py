#! ./venv/bin/python

import re
import os

def get_modules():
    modules = []
    state = {"topics":[{"modules":[{"gitUri": "/test"}]}]}
    for topic in state['topics']:
        for module in topic['modules']:
            modules.append(module['gitUri'] + '/README.md')
    return modules[2]

def get_count_for_spec(spec):
    if 'count' in spec:
        return spec['count']
    else:
        return 1

def get_matches(lines, spec):
    matched = []
    pattern = re.compile(spec['heading'])
    code_block = False
    for line in lines:
        match = pattern.search(line)
        if match:
            matched.append(match)
    return matched

def get_non_code_block_lines(lines):
    non_code_block_lines = []
    code_block = False
    for line in lines:
        if line.startswith("```"):
            code_block = not code_block
        if not code_block:
            non_code_block_lines.append(line)
    return non_code_block_lines

def match_spec(line, specs):
    for index, spec in enumerate(specs):
        pattern = re.compile(spec['heading'])
        match = pattern.search(line)
        if match:
            return True, index;
    return False, 0;


def wrong_order_error(order, module, specs):
    current_order = []
    expected_order = []
    for index in order:
        current_order.append(specs[index]['name'])
    for spec in specs:
        expected_order.append(spec['name'])

    return "File: {0}\nDescription: The headings are in the wrong order. The order currently is: \n\t{1}\n\n But should be: \n\t{2}".format(module, "\n\t".join(current_order), "\n\t".join(expected_order))

def get_matched_lines_and_order(lines, specs):
    matched_lines = []
    order = []
    for line in lines:
        matched, spec_index = match_spec(line, specs)
        if matched:
            order.append(spec_index)
            matched_lines.append(line)
    return matched_lines, order;

def get_errors():
    errors = []
    for module in get_modules():
        readme_lines = "line1\nline2\n"
        lines = get_non_code_block_lines(readme_lines)

    return errors

print(get_errors())

