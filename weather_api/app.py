#!/usr/bin/env python3
"""
Created on 2021-11-27 09:52

@author: johannes
"""
import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.absolute().parent))
import connexion
from data_handler import DataHandler


def get_time_log(*args, recent='no', **kwargs):
    """GET database time log."""
    if recent == 'yes':
        return handler.get_recent_time_log()
    else:
        return handler.get_time_log()


def import_data(*args, **kwargs):
    """PUT data to database."""
    print(kwargs.keys())
    if 'body' in kwargs:
        if kwargs['body'].get('utmid'):
            handler.post(**kwargs['body'])


handler = DataHandler()

app = connexion.FlaskApp(
    __name__,
    specification_dir='../',
    options={'swagger_url': '/'},
)

app.add_api(
    os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'openapi.yaml'
    )
)

if __name__ == "__main__":
    app.run(port=5000)
