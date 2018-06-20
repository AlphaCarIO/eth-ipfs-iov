# -*- coding: utf-8 -*-
import connexion
app = connexion.App(__name__, specification_dir='../swagger/')

def post_greeting(name: str) -> str:
    return 'Hello {name}'.format(name=name)

app.add_api('swagger.yaml', arguments={'title': 'AlphaCar Blockchain API Service'})

if __name__ == '__main__':
    app.run(port = 8080, debug = True)
