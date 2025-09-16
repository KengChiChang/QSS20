from setuptools import setup, find_packages


setup(
    name="mkdocs-custom-plugins",
    version="0.1.0",
    description="Custom plugins for the CSE 373 website template",
    long_description="",
    keywords="mkdocs",
    url="",
    license="MIT",
    python_requires=">=3.8",
    install_requires=["mkdocs>=1.1.2"],
    packages=find_packages(),
    entry_points={
        "mkdocs.plugins": [
            "collections = plugins.collections:CollectionsPlugin",
            "sass = plugins.sass:SassPlugin",
            "url-validation = plugins.more_url_validation:MoreUrlValidationPlugin",
            "auto-nav = plugins.auto_nav:AutoNavPlugin",
        ],
    },
)
