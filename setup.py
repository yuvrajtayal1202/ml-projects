from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '')for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Yuvraj',
author_email='yuvrajtayal1202@gmail.com',
packages=find_packages(),
install_requires= get_requirements('requirements.txt')
)