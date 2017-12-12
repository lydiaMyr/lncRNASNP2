import os
from lncRNASNP2 import app


def runserver():
    port = int(os.environ.get('PORT', 3000))
    app.run(host='localhost', port=port)
    app.run()

if __name__ == '__main__':
    runserver()