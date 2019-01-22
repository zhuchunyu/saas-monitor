# -*- coding: utf-8 -*-

if __name__ == '__main__':
    import app as webapp
    import envconfig

    config = envconfig.getConfig()

    webapp.app.run(host='0.0.0.0', port=5025, debug=(config['DEBUG'] == 'true'))
