from setuptools import setup

setup(
    name='sample',
    version='0.0.1',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='author name',
    author_email='auther adress',
    url='https://github.com/account/',
    license=license,
    install_requires=["scrapy"],
    extras_require={
        "develop": ["dev-packageA", "dev-packageB"]
    },
    entry_points={
        "console_scripts": [
            "foo = package_name.module_name:func_name",
            "foo_dev = package_name.module_name:func_name [develop]"
        ],
        "gui_scripts": [
            "bar = gui_package_name.gui_module_name:gui_func_name"
        ]
    }
)