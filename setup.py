from setuptools import find_packages, setup

with open("README.md", encoding="UTF-8") as f:
    long_desc = f.read()

setup(
    name='vitrix_engine',
    description='A fork of Ursina Engine designed for Vitrix!',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    version='1.1',
    url='https://github.com/ShadityZ/Vitrix-Engine',
    license='MIT',
    keywords='game development vitrix',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'panda3d',
        'panda3d-gltf',
        'panda3d-simplepbr',
        'pillow',
        'screeninfo',
        'pyperclip',
        'imageio',
        'psutil',
    ],
    python_requires='>=3.6',
)
