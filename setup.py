from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            requirements=[req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    except FileNotFoundError:
        print(f"File{file_path} don't find")
    except Exception as e:
        print(f"Happen error: {e}")
    return requirements            
setup(
    name="XrayClassification",
    version="0.0.1",
    author="Sun-AI",
    author_email="286sunsun@gmail.com",
    install_requires=get_requirements(),
    packages=find_packages()

)