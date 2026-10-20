'''
* To add Delay in Python: It's done using importing an library of time & using the statement of time.sleep(seconds) whereever the delay is required.

syntax: import time
        time.sleep(1)       #delay of 1 second

* Configuring Python environment in any new laptop: It's mainly done installing the language run time environment & code editor (IDE).

--> Python: Language run time, that executes the code & acts as "interpreter".
--> Code editor: it gives the ability to write the code & execute the code. i.e: VS Code.

--> ctlr + shift + x    = To open extension tab in VS code.
--> ctrl + shift + p    = To open quick access window & search for any configurations.
--> Terminal profile    = To select default shell (terminal profile).


* Virtual environment creation & managing packages with pip:

--> what is virutual environment:- A virtual environment is an isolated folder that contains it's own copy of python & any packages you install. Think of it as a clean workspace for each project -- packages you install in one environment don't affect another.

* Virtual environment creation:

Syntax's: 

python -m venv .venv            # used to create a virtual environment
.venv\Scripts\activate          # used to activate or enter into that environment

pip install <package name>      # used to install a package
pip install requests            # used to install the requests of a environment

pip list                        # shows everything installed 

pip freeze > requirements.txt   # used to save your dependencies to a requirements file

pip install -r requirements.txt # lets anyone recreate your exact env on their machine


ctrl + shift + p        = select interpreter (to create & activate a venv)


*Reading error message's: Most important debugging skills of a programmer.

1. Error type       = what went wrong.
2. Line number      = exactly where it happened
3. Message          = what python expected instead

ctrl + shift + i        = to open chat view with copilot
Github copilot chat (extension: to work with the copilot we need this extension)

'''