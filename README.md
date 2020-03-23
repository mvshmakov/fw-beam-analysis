# fw-beam-analysis
Pulsed Processes Analysis in a Folded Waveguide with an Electron Beam

## To run an app on local machine:
##### 1) Install `virtualenv`:
* `~ python3 -m pip install virtualenv`
##### 2) Create virtual environment:
* `~ python3 -m venv env`
##### 3) Activate virtual environment:
* `~ source env/bin/activate`
##### 4) Install all necessary requirements:
* `~ pip install --upgrade pip && pip install -r requirements.txt && pre-commit install`
##### 5) Enjoy coding!

## To make a contribution:
##### 1) Freeze all new requirements:
* `~ pip freeze --local > requirements.txt`
##### 2) Ensure you have `pre-commit` installed and run:
* `~ git add . && git commit -m ${COMMIT_MESSAGE}`
##### 3) Ensure all pre-commit hooks are successfully passed and push commits to your branch:
* `~ git push`
##### 4) Quit virtual environment after the work is done:
* `~ deactivate`

## Develop with Qt Creator:
##### 1) Compile `*.ui` to `*.py`:
* `~ pyuic5 ${qt-src/*.ui} -o ${*.py}` (`pyuic5 qt-src/mainwindow.ui -o gui.py`)

https://www.youtube.com/watch?time_continue=394&v=lq7KCo0h2PE
генерим бинарники: https://likegeeks.com/pyqt5-tutorial/ (конец статьи)
