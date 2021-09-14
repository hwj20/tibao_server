import os

from flask import Flask, request, flash, url_for
import pprint

from werkzeug.utils import redirect, secure_filename

ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png']
UPLOAD_FOLDER = ''
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class LoggingMiddleware(object):
    def __init__(self, app):
        self._app = app

    def __call__(self, env, resp):
        errorlog = env['wsgi.errors']
        pprint.pprint(('REQUEST', env), stream=errorlog)

        def log_response(status, headers, *args):
            pprint.pprint(('RESPONSE', status, headers), stream=errorlog)
            return resp(status, headers, *args)

        return self._app(env, log_response)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['POST'])
def result():
    # print(request.data)  # raw data
    print(request.files)
    print(request.json)  # json (if content-type of application/json is sent with the request)
    # print(request.get_json(force=True))  # json (if content-type of application/json is not sent)

    if 'uploadfile' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['uploadfile']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        print(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(request.url)
        # return redirect(url_for('download_file', name=filename))


if __name__ == '__main__':
    app.wsgi_app = LoggingMiddleware(app.wsgi_app)
    # app.run(host='192.168.1.109', port=8000)
    app.run(host='113.54.216.96', port=8000)
