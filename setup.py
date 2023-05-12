import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="selenium_helpers",
    version="0.0.1",
    author="Ivan Mičetić",
    author_email="ivan.micetic@gmail.com",
    description="Helper functions for selenium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ivanmicetic/selenium-helpers",
    project_urls={
        "Bug Tracker": "https://github.com/ivanmicetic/selenium-helpers/issues"
    },
    license="MIT",
    packages=["selenium_helpers"],
    install_requires=["selenium<4", "webdriver_manager"],
)
