```python
# config.py

# Import necessary libraries
import os

# Define the base directory for the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the directory for templates
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# Define the default template file
DEFAULT_TEMPLATE = os.path.join(TEMPLATE_DIR, 'default_template.py')

# Define the directory for the generated project structure
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

# Define the default project name
DEFAULT_PROJECT_NAME = 'my_python_project'

# Define the default number of files to be created in the project
DEFAULT_NUM_FILES = 10

# Define the default number of directories to be created in the project
DEFAULT_NUM_DIRS = 5

# Define the default depth of the project structure
DEFAULT_DEPTH = 3

# Define the default version control system to be used
DEFAULT_VCS = 'git'

# Define the default version control repository URL
DEFAULT_VCS_URL = ''

# Define the default version control username
DEFAULT_VCS_USERNAME = ''

# Define the default version control password
DEFAULT_VCS_PASSWORD = ''

# Define the default version control branch
DEFAULT_VCS_BRANCH = 'main'
```
