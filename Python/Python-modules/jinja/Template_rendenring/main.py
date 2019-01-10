from jinja2 import Template
import yaml
import os


def get_config(path, file_name='config.yml'):
    with open(os.path.join(path, file_name), 'r') as f:
        return yaml.load(f)


def get_template(path, template_name):
    with open(os.path.join(path, template_name), 'r') as f:
        return f.read()


def render_template(config: dict, template: str):
    data = dict()
    data['Name'] = config['Name']
    data['favorite_lang'] = config['Programming_Lang'][0]
    try:
        template = Template(template)
        return template.render(**data)
    except Exception as e:
        print('Error while rendering template: ',e)
        return None


if __name__ == '__main__':
    path = os.getcwd()
    try:
        config = get_config(os.path.join(path, 'configDir'), 'config.yml')
        my_template = get_template(os.path.join(path, 'template'), 'main_template.tf')
    except FileNotFoundError:
        print('File Not Found :', e)
    except Exception as e:
        print(e)

    print(render_template(config, my_template))




