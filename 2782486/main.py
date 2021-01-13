# https://pypi.org/project/json2xml/
from json2xml import json2xml
from json2xml.utils import readfromstring

def parse_json2xml(string, name_file):
    file_to_write = open(name_file, 'w')
    data = readfromstring(string)
    print(json2xml.Json2xml(data).to_xml(), file=file_to_write)


# https://github.com/quandyfactory/dicttoxml
import json
import dicttoxml
from xml.dom.minidom import parseString

def parse_dicttoxml(string, name_file):
    file_to_write = open(name_file, 'w')
    data = json.loads(string)
    xml = dicttoxml.dicttoxml(data)
    dom = parseString(xml)
    print(dom.toprettyxml(), file=file_to_write)

import re

def sequence(*funcs):
    if len(funcs) == 0:
        def result(src):
            yield (), src
        return result
    def result(src):
        for arg1, src in funcs[0](src):
            for others, src in sequence(*funcs[1:])(src):
                yield (arg1,) + others, src
    return result

number_regex = re.compile(r"(-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?)\s*(.*)", re.DOTALL)

def parse_number(src):
    match = number_regex.match(src)
    if match is not None:
        number, src = match.groups()
        yield eval(number), src

string_regex = re.compile(r"('(?:[^\\']|\\['\\/bfnrt]|\\u[0-9a-fA-F]{4})*?')\s*(.*)", re.DOTALL)

def parse_string(src):
    match = string_regex.match(src)
    if match is not None:
        string, src = match.groups()
        yield eval(string), src

def parse_word(word, value=None):
    l = len(word)
    def result(src):
        if src.startswith(word):
            yield value, src[l:].lstrip()
    result.__name__ = "parse_%s" % word
    return result

parse_null = parse_word("null", None)

def parse_value(src):
    for match in parse_string(src):
        yield match
        return
    for match in parse_number(src):
        yield match
        return
    for match in parse_array(src):
        yield match
        return
    for match in parse_object(src):
        yield match
        return
    for match in parse_null(src):
        yield match
        return

parse_left_square_bracket = parse_word("[")
parse_right_square_bracket = parse_word("]")
parse_empty_array = sequence(parse_left_square_bracket, parse_right_square_bracket)

def parse_array(src):
    for _, src in parse_empty_array(src):
        yield [], src
        return

    for (_, items, _), src in sequence(
        parse_left_square_bracket,
        parse_comma_separated_values,
        parse_right_square_bracket,
    )(src):
        yield items, src

parse_comma = parse_word(",")

def parse_comma_separated_values(src):
    for (value, _, values), src in sequence(
        parse_value,
        parse_comma,
        parse_comma_separated_values
    )(src):
        yield [value] + values, src
        return

    for value, src in parse_value(src):
        yield [value], src

parse_left_curly_bracket = parse_word("{")
parse_right_curly_bracket = parse_word("}")
parse_empty_object = sequence(parse_left_curly_bracket, parse_right_curly_bracket)

def parse_object(src):
    for _, src in parse_empty_object(src):
        yield {}, src
        return
    for (_, items, _), src in sequence(
        parse_left_curly_bracket,
        parse_comma_separated_keyvalues,
        parse_right_curly_bracket,
    )(src):
        yield items, src

parse_colon = parse_word(":")

def parse_keyvalue(src):
    for (key, _, value), src in sequence(
        parse_string,
        parse_colon,
        parse_value
    )(src):
        yield {key: value}, src

def parse_comma_separated_keyvalues(src):
    for (keyvalue, _, keyvalues), src in sequence(
        parse_keyvalue,
        parse_comma,
        parse_comma_separated_keyvalues,
    )(src):
        keyvalue.update(keyvalues)
        yield keyvalue, src
        return

    for keyvalue, src in parse_keyvalue(src):
        yield keyvalue, src

def parse(s):
    s = s.strip()
    match = list(parse_value(s))
    if len(match) != 1:
        raise ValueError("not a valid JSON string")
    result, src = match[0]
    if src.strip():
        raise ValueError("not a valid JSON string")
    return result


# https://gist.github.com/reimund/5435343
def dict2xml(d, root_node=None):
    wrap = False if None == root_node or isinstance(d, list) else True
    root = 'objects' if None == root_node else root_node
    root_singular = root[:-1] if 's' == root[-1] and None == root_node else root
    xml = ''
    attr = ''
    children = []

    if isinstance(d, dict):
        # print(d)
        for key, value in dict.items(d):
            if isinstance(value, dict):
                children.append(dict2xml(value, key))
            elif isinstance(value, list):
                children.append(dict2xml(value, key))
            elif key[0] == '@':
                attr = attr + ' ' + key[1::] + '="' + str(value) + '"'
            else:
                xml = '<' + key + ">" + str(value) + '</' + key + '>'
                children.append(xml)

    else:
        # if list
        for value in d:
            children.append(dict2xml(value, root_singular))

    end_tag = '>' if 0 < len(children) else '/>'

    if wrap or isinstance(d, dict):
        xml = '<' + root + attr + end_tag

    if 0 < len(children):
        for child in children:
            xml = xml + child

        if wrap or isinstance(d, dict):
            xml = xml + '</' + root + '>'

    return xml


def adding_padding(string):
    result = '<?xml version="1.0" ?>\n'
    tabs = 0
    string = re.sub(r'<\/([^>]*)\(([^>]*)\)>', r'</key>', string)
    string = re.sub(r'<([^>]*)\(([^>]*)\)>', r'<key name="\1(\2)">', string)

    for index, elem in enumerate(string):
        result += elem

        if elem == '>' and index + 1 < len(string) and string[index + 1] == '<':

            if index + 2 < len(string) and string[index + 2] != '/':
                tabs += 1
            result += '\n'
            result += '\t' * tabs

        if elem == '<' and string[index + 1] == '/':
            tabs -= 1
    return result


# собственная функция вызова
def parse_my_function(string, name_file):
    file_to_write = open('parse_my.xml', 'w')
    string = string.replace('"', "'")
    dictionary = parse(string)
    result = dict2xml(dictionary)
    result = adding_padding(result)
    print(result, file=file_to_write)


import time


# открытие подготовленного файла json
file = open('Tuesday.text', 'r')
string = file.read()

circles = 100

start_time = time.time()
for i in range(circles):
    parse_json2xml(string, 'json2xml.xml')
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
for i in range(circles):
    parse_dicttoxml(string, 'dicttoxml.xml')
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
for i in range(circles):
    parse_my_function(string, 'parse_my.xml')
print("--- %s seconds ---" % (time.time() - start_time))