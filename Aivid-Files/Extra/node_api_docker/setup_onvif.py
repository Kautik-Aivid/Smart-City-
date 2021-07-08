from setuptools import setup
import shutil

requires = [ 'suds >= 0.4', 'suds-passworddigest' ]

try:

    setup(
        name='onvif',
        version="0.2.0",
        install_requires=requires
        )
except Exception as err:
    try:
        shutil.rmtree("build")
        shutil.rmtree("dist")
        shutil.rmtree("onvif.egg-info")
    except:
        dl = None
    print("Done")


