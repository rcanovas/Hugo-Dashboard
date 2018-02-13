import json
import os.path
from datetime import datetime
import toml
from markdown import markdown
from pytz import timezone


project_location = '/mnt/e/Code/go/sites/testsite'


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
    last_updated_date = get_now()
    if os.path.isfile(source_file):
        toml_content, md_content = split_file(source_file)
        config = toml.loads(toml_content)
        return dict(
                status=200, message="OK",
                toml_fields=config, markdown_contents=md_content,
                timestamp=last_updated_date
            )
    else:
        return dict(
            status=404, message="NOT FOUND",
            toml_fields={}, markdown_contents=[],
            timestamp=last_updated_date
        )


def get_now():
    return datetime.now(timezone('Australia/Melbourne')).strftime("%Y-%m-%dT%H:%M:%S%z")


def set_contents(section, page, md_content, toml_content):
    source_file = '{}/content/{}/{}.md'.format(project_location, section, page)
    last_updated_date = get_now()
    if os.path.isfile(source_file):
        toml_content['last_updated'] = last_updated_date
        with open(source_file, 'w') as rewrite:
            rewrite.write('+++\n{}+++\n\n'.format(toml.dumps(toml_content)))
            rewrite.write('\n\n'.join(md_content))
            print('done')
        return {
                "status": 200, "message": "OK",
                "timestamp": last_updated_date
        }
    else:
        return dict(
            status=404, message="FILE NOT FOUND",
            toml_fields={}, markdown_contents=[],
            timestamp=last_updated_date
        )


def new_content(section, page, md_content, toml_content):
    source_file = '{}/content/{}/{}.md'.format(project_location, section, page)
    last_updated_date = get_now()
    if not os.path.isfile(source_file):
        toml_content['date'] = last_updated_date
        with open(source_file, 'w+') as rewrite:
            rewrite.write('+++\n{}+++\n\n'.format(toml.dumps(toml_content)))
            rewrite.write('\n\n'.join(md_content))
            print('done')
        return {
                "status": 200, "message": "OK",
                "timestamp": last_updated_date
        }
    else:
        return dict(
            status=400, message="FILE EXISTS",
            timestamp=last_updated_date
        )


def remove_content(section, page):
    source_file = '{}/content/{}/{}.md'.format(project_location, section, page)
    last_updated_date = get_now()
    if os.path.isfile(source_file):
        try:
            os.remove(source_file)
            return {
                    "status": 200, "message": "OK",
                    "timestamp": last_updated_date
            }
        except Exception as e:
            return {
                    "status": 500, "message": "UNEXPECTED ERROR",
                    "timestamp": last_updated_date
            }
    else:
        return dict(
            status=404, message="FILE NOT FOUND",
            timestamp=last_updated_date
        )
