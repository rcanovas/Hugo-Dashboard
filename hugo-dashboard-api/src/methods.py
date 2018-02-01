import json
import os.path
from datetime import datetime
import toml
from markdown import markdown


project_location = '/mnt/e/Code/go/sites/deilanexe.github.com'


def read_toml_md_file(input_toml_md_file):
    with open(input_toml_md_file, 'r') as conffile:
        for line in conffile:
            yield line


def split_file(input_file):
    """
    Normally `toml` files are split into two sections: one contains structured,
    toml data, (wrapped between '+++') and the other is markdown. This method
    returns both contents, toml as a string, markdown as a list of strings.
    :param input_file: a markdown file with toml and markdown contents
    :return: string with toml contents; list with contents in Markdown format
    """
    toml_contents = ''
    markdown_contents = []
    is_toml = False
    md_line_tmp = ''
    for line in read_toml_md_file(input_file):
        if line.startswith('+++'):
            is_toml = not is_toml
        elif is_toml:
            toml_contents += line
        else:
            line = line.rstrip()
            if line == '':
                if len(md_line_tmp) > 0:
                    markdown_contents.append(md_line_tmp)
                    md_line_tmp = ''
            else:
                md_line_tmp += '{} '.format(line)
    if len(md_line_tmp) > 0:
        markdown_contents.append(md_line_tmp)
    return toml_contents, markdown_contents


def get_contents(section, page):
    source_file = '{}/content/{}/{}.md'.format(project_location, section, page)
    if os.path.isfile(source_file):
        toml_content, md_content = split_file(source_file)
        config = toml.loads(toml_content)
        return json.dumps(
            dict(
                status=200, message="OK",
                toml_fields=config, markdown_contents=md_content,
                timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            )
        )
    else:
        return json.dumps(dict(
            status=404, message="NOT FOUND",
            toml_fields={}, markdown_contents=[],
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        ))
