import setuptools

setuptools.setup(
    name="elevator_simulator",
    version="0.0.1",
    description="Elevator Simulator",
    url="https://github.com/bogdanblagait/elevator_simulator",
    author="Bogdan Blaga",
    author_email="bogdanblagait@yahoo.com",
    packages=setuptools.find_packages(exclude=["tests*"]),
    # package_data={'snowballstrategy': ['utils/data/*.csv']},
    # include_package_data=True,
    zip_safe=False,
)
