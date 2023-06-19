from cx_Freeze import setup, Executable

base = None    

executables = [Executable("finnn.py", base=base)]

packages = ["idna","os", "numpy", "pandas", "mayplotlib.pyplot", "seaborn", "geopandas", "shapefile", "shapely.geometry", "tkinter"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Crime pred/Sentiment analysis",
    options = options,
    version = "0.11",
    description = ' ',
    executables = executables
)