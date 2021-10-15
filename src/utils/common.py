import yaml
def config_read(config_path):
    with open (config_path) as config:
      content = yaml.safe_load(config)
    return content
    