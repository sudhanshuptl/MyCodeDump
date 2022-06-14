#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import logging
import os
from flask import render_template, Blueprint, request, make_response, Flask
from werkzeug.utils import secure_filename

import redis

# step 2: define our connection information for Redis
# Replaces with your configuration information
redis_host = "localhost"
redis_port = 6379
redis_password = ""
r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

app = Flask(__name__)

log = logging.getLogger(__name__)


@app.route('/')
@app.route('/index')
def index():
    # Route to serve the upload form
    return render_template('index.html',
                           page_name='Main',
                           project_name="pydrop")


@app.route('/upload/save', methods=['POST'])
def upload():
    # Route to deal with the uploaded chunks
    print('_------------->>>>>>')
    print('_------------->>>>>>', request.form)
    print('_------------->>>>>>', request.files)
    print(request.form['dzuuid'])
    print(request.files['file'].filename)

    file = request.files['file']

    # secure_filename makes sure the filename isn't unsafe to save
    save_path = os.path.join('./', secure_filename(file.filename))

    # We need to append to the file, and write as bytes
    with open(save_path, 'ab') as f:
        # Goto the offset, aka after the chunks we already wrote
        f.seek(int(request.form['dzchunkbyteoffset']))
        data = file.stream.read()
        print(type(data))
        f.write(data)

    # Giving it a 200 means it knows everything is ok
    return make_response(('Uploaded Chunk', 200))


@app.route('/upload', methods=['POST'])
def upload_redis():
    # Route to deal with the uploaded chunks
    print('_------------->>>>>>')
    print('_------------->>>>>>', request.form)
    print('_------------->>>>>>', request.files)
    print(request.form['dzuuid'])
    print(request.files['file'].filename)

    file = request.files['file']
    total_chunnk =  int(request.form['dztotalchunkcount'])
    current_chunk = int(request.form['dzchunkindex'])

    name_prefix, name_suffix = file.filename.split('.')
    key = f'{name_prefix}_{request.form["dzuuid"]}.{name_suffix}'

    if current_chunk == 0:
        r.set(key, file.stream.read().decode('utf-8'))
    else:
        existing_chunk = r.get(key)
        existing_chunk += str(file.stream.read().decode('utf-8'))
        r.set(key, existing_chunk)

        if total_chunnk - 1 == current_chunk:  # when last chunk recived
            print('Header -> ', existing_chunk[:100])

    # Giving it a 200 means it knows everything is ok
    print('key -> ', key)
    return make_response((f'Uploaded Chunk -> {key}', 200))


if __name__ == '__main__':
    app.run(debug=True)


# ImmutableMultiDict([('dzuuid', 'b8c052ef-c227-4462-aaf0-048cacc54e79'), ('dzchunkindex', '30'), ('dztotalfilesize', '30600015'), ('dzchunksize', '1000000'), ('dztotalchunkcount', '31'), ('dzchunkbyteoffset', '30000000')])
# ImmutableMultiDict([('file', <FileStorage: 'csv_test2.csv' ('application/octet-stream')>)])