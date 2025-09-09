from setuptools import find_packages, setup

setup(
    name="film-greenlight-recommender",
    version="0.1.0",
    description=(
        "Data-science challenge on film data: EDA and basic ML to guide "
        "which movie to greenlight, with hypotheses, overview-based insights, "
        "and IMDB rating prediction."
    ),
    author="Ana Luiza Gomes Vieira",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    python_requires=">=3.10",
)
