from distutils.core import setup
import py2exe


# setup(console=["hello.py"])
py2exe_options = dict({
    "includes":['sip', 'encodings', 'encodings.ascii', 'encodings.utf_8', 'encodings.cp866'],
    "dll_excludes":["MSVCP90.dll"]})

setup(version="1.0",
      description="Bearing Monitor",
      name="bmon",
      zipfile=None,
      dist_dir="bmon",
      windows=["bmon.py"],
      options={'py2exe': py2exe_options},
      icon_resources=[(1, "res/survey.ico")],
      data_files=[("", ["check_all.ico"])] 
    )