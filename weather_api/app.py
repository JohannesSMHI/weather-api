#!/usr/bin/env python3
"""
Created on 2021-11-27 09:52

@author: johannes
"""
import os
import sys
import connexion
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from data_handler import DataHandler


app = connexion.FlaskApp(
    __name__,
    specification_dir='../',
    options={'swagger_url': '/'},
)


def get_time_log(*args, recent=False, **kwargs):
    """GET database time log."""
    if recent:
        return handler.get_recent_time_log()
    else:
        return handler.get_time_log()


def import_data(*args, **kwargs):
    """PUT data to database."""
    if 'body' in kwargs:
        if kwargs['body'].get('utmid'):
            handler.post(**kwargs['body'])


handler = DataHandler()

app.add_api(
    os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'openapi.yaml'
    )
)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
