# -*- coding: utf-8 -*-

if __name__ == '__main__':
    print('main...')

    import app as webapp

    webapp.app.run(host='0.0.0.0', port=5025, debug=True)
