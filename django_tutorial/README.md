https://docs.djangoproject.com/en/5.2/intro/tutorial01/
`
Install; poetry:`
If ide doesnt offer link:
# curl -sSL https://install.python-poetry.org | python3 -\n

# This command ensures that the directory where Poetry is installed ($HOME/.local/bin) is included in your system’s 
# executable path.
export PATH="$HOME/.local/bin:$PATH"

Install pyenv:
sudo pkg install pyenv - freebsd
sudo pacman -Sy pyenv - arch
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
Add this to shell config (~/.bashrc, ~/.zshrc, etc.):
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

Install the python version required in toml:
pyenv install 3.12.4     

Set that version for your project:
pyenv local 3.12.4

Then, to link Poetry to the correct Python version, run:
poetry env use $(pyenv which python)
Creating virtualenv django-tutorial-VXBGBbcu-py3.12 in /home/rich/.cache/pypoetry/virtualenvs
Using virtualenv: /home/rich/.cache/pypoetry/virtualenvs/django-tutorial-VXBGBbcu-py3.12

Read your pyproject.toml file
Look at the dependencies you've declared for your project.
Creates (or reuses) a virtual environment:
Installs all dependencies listed in:
    pyproject.toml (declared dependencies)
    poetry.lock (exact versions that were locked previously)
Installs your project in "editable" mode:
poetry install

Installing dependencies from lock file
Package operations: 3 installs, 0 updates, 0 removals
  - Installing asgiref (3.8.1)
  - Installing sqlparse (0.5.3)
  - Installing django (5.2)
Installing the current project: django-tutorial (0.1.0)

poetry env info
Virtualenv
Python:         3.12.4
Implementation: CPython
Path:           /home/rich/.cache/pypoetry/virtualenvs/django-tutorial-VXBGBbcu-py3.12
Executable:     /home/rich/.cache/pypoetry/virtualenvs/django-tutorial-VXBGBbcu-py3.12/bin/python
Valid:          True

Base
Platform:   freebsd14
OS:         posix
Python:     3.12.4
Path:       /home/rich/.pyenv/versions/3.12.4
Executable: /home/rich/.pyenv/versions/3.12.4/bin/python3.12

https://python-poetry.org/docs/managing-environments/#bash-csh-zsh

The poetry env activate command prints the activate command of the virtual environment to the console. You can run the output command manually or feed it to the eval command of your shell to activate the environment. This way you won’t leave the current shell.
poetry env activate

eval $(poetry env activate)
(test-project-for-test) $  # Virtualenv entered

Start virtual environment:
# poetry shell - depricated, now use:
source $(poetry env info --path)/bin/activate
(django-tutorial-py3.12) ┌─(/common-data/projects/python/django_tutorial)───────────────────────────────────────────────
────────────────────────────────────────────────────────────────(rich@r5-5600g-nvidia:pts/4)─┐


install poetry-plugin-shell to be able to use poetry shell again:
poetry self add poetry-plugin-shell
now poetry shell works

to start an interactive Python shell with Django's settings and environment loaded,
allowing you to interact with your Django project from the command line:
python manage.py shell

poetry run python manage.py runserver
poetry run python manage.py migrate

    Safe and always uses the right venv.

    No prompt change needed.

source $(poetry env info --path)/bin/activate

    Now your prompt shows the venv (optional).

    You don’t need to type poetry run anymore — just run commands normally:

python manage.py runserver
python manage.py migrate

    When done, exit with deactivate.

to start the server:
From:
~/projects/python/django_tutorial/django_tutorial>
poetry run python manage.py runserver  

django admin:
user: admin
email: rkba1@pm.me
rdjaQ#25

After css changes before push:
poetry run python manage.py collectstatic


render:
Copy the values from the Connections section:

Database
django_tutorial_8okl
Username
rich
Password
i0UQho5OenS0fXUyifGwPddhlBeEIiYJ
Hostname
dpg-d2uf89p5pdvs73ae1s00-a
Port
5432
Go to your Django app card, open Environment, and add these as environment variables:

DB_NAME=<Database>
DB_USER=<Username>
DB_PASSWORD=<Password>
DB_HOST=<Hostname>
DB_PORT=<Port>
ENV=production

supabase:
Project API

Your API is secured behind an API gateway which requires an API Key for every request.
You can use the parameters below to use Supabase client libraries.
Project URL

A RESTful endpoint for querying and managing your database.

API Key
anon
public

This key is safe to use in a browser if you have enabled Row Level Security (RLS) for your tables and configured policies. You may also use the service key which can be found here to bypass RLS.
Javascript
Dart

import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://njronzwcjrhbwljpbcit.supabase.co'
const supabaseKey = process.env.SUPABASE_KEY
const supabase = createClient(supabaseUrl, supabaseKey)

postgresql://postgres:[YOUR-PASSWORD]@db.njronzwcjrhbwljpbcit.supabase.co:5432/postgres

host: db.njronzwcjrhbwljpbcit.supabase.co
port: 5432
database: postgres
user: postgres
-------------------------------------------------------------
Aiven:
Service URI
    postgres://avnadmin:<pwd>@postgres-db-django-tutorial.d.aivencloud.com:27298/defaultdb?sslmode=require
Database name
    defaultdb
Host
    postgres-db-django-tutorial.d.aivencloud.com
Port
    27298
User
    avnadmin
Password
    

SSL mode
    require
CA certificate
Connection limit
    20

Aiven:
pg_dump -Fc -U rich django_tutorial -f django_tutorial.dump
pg_restore \
    -d "postgresql://avnadmin:<pwd>>@postgres-db-django-tutorial.d.aivencloud.com:27298/defaultdb?sslmode=require" \
    --no-owner \
    --clean \
    --if-exists \
    -v \
    django_tutorial.dump