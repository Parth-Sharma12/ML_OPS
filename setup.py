from setuptools import find_packages,setup # This will find all the packages installed in the application
from typing import List
HYPHEN_E_DOT = '-e .'


def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup (
name = "mlops",
version = "0.0.1",
author = "parth",
author_email = "sharmaparth1208@gmail.com",
packages = find_packages(), # this will look for __init__.py file and build that folder ( we have this file in srs folder)
install_requires = get_requirements("requirements.txt"),



)