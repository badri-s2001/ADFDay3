def config_read():
    filename = "external.config"
    contents = open(filename).read()
    config = eval(contents)
    python_filename = config['python_filename']
    input_filename = config['input_filename']
    classes = config['classes']

    print(f"{python_filename}")
    print(f"{input_filename}")
    print(f"{classes}")


config_read()
