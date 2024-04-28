from configparser import ConfigParser #Модуль config.py использует встроенный модуль для чтения данных из database.ini файла.configparser

def load_config(filename='C:\MyPythonProjects\TSIS\Lab10\database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config

if __name__ == '__main__':
    config = load_config()
    print(config)
    
#Во-вторых, создайте новый файл, вызываемый в каталоге проекта, и определите функцию, которая считывает конфигурационные данные из файла:config.pyload_config()database.ini