import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "ChickenDisease"
AUTHOR_USER_NAME = "mhussainahmad"
SRC_REPO = "ChickenDisease"
AUTHOR_EMAIL = "emhussain25@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Small python package for Chicken disease classification",
    long_description=long_description,
    long_description_content = "text/markdown",
    src = f"htt"
)