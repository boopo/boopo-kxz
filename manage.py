import os

from flask_migrate import MigrateCommand
from flask_script import Manager
from App import create_app

env = os.environ.get("FLASK_ENV") or 'default'

app = create_app(env)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()


# apidoc -i src/ -o apidoc/
# docker build -t cumt-kxz:1.0 --restart=always
# docker run -p 12000:12000 -d -it cumt-kxz:1.0 --restrat=always
# docker exec -it cumt-kxz:1.0 /bin/bash
# redis-server






