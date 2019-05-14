import os
import re
from shutil import copyfile

import frontmatter
import toml


def main():
    extensions = {}
    with open('config.toml', 'r') as f:
        config = toml.loads(f.read())
        default_lang = config['DefaultContentLanguage']
        site_name = config['title'].replace(' ', '_')
        site_name = site_name.replace("'", "")
        site_name = site_name.replace('"', '')
        site_name = site_name.replace(',', '')
        site_name = site_name.replace('.', '')
        if 'languages' in config:
            for key in config['languages']:
                extensions[config['languages'][key]['contentDir'].split('/')[-1]] = key
                if key != default_lang:
                    os.mkdir(os.path.join('pdf-build', key))
    guides = []
    if 'pages' in os.listdir('content'):
        # single language 
        contents = []
        for item in os.listdir('content'):
            if os.path.isfile(os.path.join('content',item)):
                ext = os.path.splitext(item)[1]
                if ext != '.md':
                    copyfile(os.path.join('content', item), os.path.join('pdf-build',item))
        for path, _, files in os.walk('content/pages'):
            for filename in files:
                ext = os.path.splitext(filename)[1]
                if ext == '.md':
                    content = clean_markdown(path, filename)
                    if content:
                        contents.append({'name':filename, 'content': content})
                else:
                    copyfile(os.path.join(path,filename), os.path.join('pdf-build',filename))
        full_pdf_content = ""
        content = clean_markdown("content", "_index.md")
        if content:
            full_pdf_content += content
            full_pdf_content += "\n\n\pagebreak\n\n"
        for item in sorted(contents, key=lambda k: k['name']):
            full_pdf_content += item['content']
            full_pdf_content += "\n\n\pagebreak\n\n"
        with open('pdf-build/' + site_name + ".md", 'w') as f:
            f.write(full_pdf_content)
        
    else:
        # multiple languages
        for lang in os.listdir('content'):
            contents = []
            lang_key = extensions[lang]
            lang_path = os.path.join('content', lang)
            for path, _, files in os.walk(lang_path):
                if lang_key == default_lang:
                    lang_key = ''
                for filename in files:
                    ext = os.path.splitext(filename)[1]
                    if ext == '.md':
                        content = clean_markdown(path, filename)
                        if content:
                            contents.append({'name':filename, 'content': content})
                    else:
                        copyfile(os.path.join(path,filename), os.path.join('pdf-build',lang_key,filename))
            full_pdf_content = ""
            for item in sorted(contents, key=lambda k: k['name']):
                full_pdf_content += item['content']
                full_pdf_content += "\n\n\pagebreak\n\n"
            with open('pdf-build/' + site_name + ".md", 'w') as f:
                f.write(full_pdf_content)


def clean_markdown(path, filename, lang=""):
    post = frontmatter.load(os.path.join(path, filename))
    if post.content:
        title = post.metadata.get('title', '')
        guide = {}
        guide['filename'] = filename
        content = re.sub(r'(\!\[.*\]\()(\/)(\w+\.\w+\))', r'\1\3', post.content)
        guide['content'] = ''
        if title:
            guide['content'] += '# {0} \n\n'.format(title)
        guide['content'] += content
        if lang and lang != default_lang:
            out_file = os.path.join('pdf-build',lang, guide['filename'])
        else: 
            out_file = os.path.join('pdf-build', guide['filename'])
        with open(out_file, 'w') as f:
            f.write(guide['content'])
        return guide['content']
    return ''

if __name__ == "__main__":
    main()