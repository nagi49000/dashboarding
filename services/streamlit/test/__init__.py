import sys
from pathlib import Path


# have to add a linker path to the streamlit script for the app
# since all imports in that script are based on the script location
sys.path.append(str(Path(__file__).parents[1] / "app"))
