#!/usr/bin/env python
from flask import Flask, make_response, request, abort
import json

app = Flask(__name__)


def get_rpms_list(hostname='default'):
    filename = hostname + '_rpms.list'
    try:
        with open("./configs/" + filename, 'r') as f:
            rpms_list = {"rpms_list": f.read().splitlines()}
            return rpms_list
    except IOError:
        return False


@app.route('/api/v1/rpms', methods=['GET'])
def download_rpms_list():
    hostname = request.args.get('hostname')
    if not hostname:
        hostname = 'default'

    rpms_list = get_rpms_list(hostname)
    if not rpms_list:
        abort(404)
    response = make_response(json.dumps(rpms_list))

    # add filename to headers
    # wget --content-disposition http://localhost:5000/api/v1/rpms
    response.headers["Content-Disposition"] = "attachment; filename=%s.json" % hostname

    return response

if __name__ == '__main__':
    app.run()
