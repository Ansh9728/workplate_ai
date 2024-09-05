import sys
import os
from streamlit.web import cli as stcli

file_path = os.path.join(os.getcwd(), 'frontend_ui/app.py')

# print(file_path)
if __name__ == '__main__':
    sys.argv = ["streamlit", "run", file_path]
    sys.exit(stcli.main())