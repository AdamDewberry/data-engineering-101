# Pip - The Package Manager

Software typically depends on many support packages and libraries, each package has a specific release version.  One way to version is using a semantic version, [SEMVER](https://semver.org/), of Major.Minor.Patch.

### A note on SEMVER

- The Patch version includes backwards compatible changes and bug fixes.
- The Minor version adds functionality which is backwards compatible, for example new methods (functions).
- The Major version includes changes and additions which are not backwards compatible.

Python 2 was first developed in the 1980s and used through to 2020.  The core language and functionality developed over time which would be reflected in new releases, which include a new SEMVER.

Such significant changes and improvements lead to a new major release of the language, this is when Python 3 was born.

The last stable releases of Python 2 are 2.7.x; currently Python 3 is up to 3.10.0 and Python 2 is being [sunsetted](https://www.python.org/doc/sunset-python-2/).

If any applications run on Python 2 (which some of the core systems of Mac OS, including Catalina, do), they will need to be updated to Python 3 in order to continue functioning, receive security updates, bug fixes and forwards compatibility to modules and libraries.

## Packages

In Python there are a number of package managers which can download and install modules for us, even specific versions. One popular package manager is Pip, Pip comes bundled with a Python distribution and can be installed during the initial setup.

To install a library, such as pandas, we run:

    pip install pandas

Depending on your system, you may need to run `pip3` if there is already a Python 2 distribution installed.

To install a specific version, use the following syntax:

    pip install pandas==1.0.1

Pip looks to the [PyPi](https://pypi.org/) package repository where developers can list their packages and libraries for others to consume. Running `pip` points to this repository, checks the package exists and then downloads it. If you're really lucky the developer will have included the information in their library to download an dependancies for example, downloading `pandas` _should_ download `numpy` too.

## Viewing your Python packages

Running:

    pip freeze

Will list out all of the packages you have installed.

## requirements.txt

A good project contains a `requirements.txt` file which contains all of the Python libraries the project depends on and their version. You can manually create this or export all of your packages using:

    pip freeze >> requirements.txt

## Installing packages using requirements.txt

If you provide or are provided with a requirements file, you can install them using:

    pip install --requirement requirements.txt

## Conflicts

You may encounter packages whose versions conflict with each other, especially if the package is an older version.

Some engineers use programs like [`Anaconda`](https://www.anaconda.com/) to mange packages for them. I believe there is merit in understanding how to install and manage packages yourself as this is needed when setting up a runtime on a server or in a container, you want to achieve a lightweight installation only using the software that
you need.
