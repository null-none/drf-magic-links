from distutils.core import setup

setup(
    name="drf-magic-links",
    packages=[
        "magic_links",
        "magic_links/migrations",
        "magic_links/urls",
        "magic_links/views",
    ],
    version="1.0.0",
    description="",
    author="Kalinin Mitko",
    author_email="kalinin.mitko@gmail.com",
    url="https://github.com/null-none/drf-magic-links",
    keywords=[],
    classifiers=[],
    install_requires=[
        "bcrypt",
        "django-rest-framework",
    ],
)
