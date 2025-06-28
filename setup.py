from setuptools import setup, find_packages

setup(
    name="mp3meta",
    version="1.0.0",
    description="Command-line tool for MP3 metadata export/import via CSV",
    author="Andreas Karampasis",
    packages=find_packages(),
    install_requires=[
        "mutagen"
    ],
    entry_points={
        "console_scripts": [
            "mp3tagger = mp3tagger.__main__:main"
        ]
    },
    python_requires=">=3.7",
)

