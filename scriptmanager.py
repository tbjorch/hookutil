# Standard library
from configparser import ConfigParser
from os import path, system
import logging

# 3rd party modules
from werkzeug.exceptions import BadRequest

config = ConfigParser()
config.read("scripts.ini")


def run_script(script_name: str) -> None:
    file_name, log_message = __script_exists(script_name.upper())
    logging.info(f"Script {script_name} located. {log_message}")
    __execute_script(file_name)


def __script_exists(script_name: str) -> str:
    if not script_name.upper() in config.sections():
        raise BadRequest("No such script")
    return (
        config[script_name]["file_name"],
        config[script_name]["log_message"]
        )


def __execute_script(file_name: str):
    scripts_dir_path = path.realpath("scripts")
    file_path = path.join(scripts_dir_path, file_name)
    system("sh " + file_path)
