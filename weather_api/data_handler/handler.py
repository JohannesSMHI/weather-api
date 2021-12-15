#!/usr/bin/env python3
"""
Created on 2021-11-27 09:52

@author: johannes
"""
import os
import yaml
import sqlite3
import pandas as pd
from weather_api import get_base_folder


def get_db_conn():
    """Doc."""
    return sqlite3.connect(os.getenv('TSTWEATHERDB'))


class DataHandler:
    """Doc."""

    def __init__(self):
        base = get_base_folder()
        with open(os.path.join(base, 'resources/parameters.yaml')) as fd:
            data = yaml.load(fd, Loader=yaml.FullLoader)
        self.db_fields = set(data.get('db_fields'))

    def post(self, **kwargs):
        """Doc."""
        print('NEW DATA')
        df = pd.DataFrame(
            {field: item for field, item in kwargs.items() if field in self.db_fields}
        )
        print(df)
        conn = get_db_conn()
        df.to_sql('weather', conn, if_exists='append', index=False)

    @staticmethod
    def get():
        """Doc."""
        conn = get_db_conn()
        return pd.read_sql('select * from weather', conn)

    @staticmethod
    def get_time_log():
        """Doc."""
        conn = get_db_conn()
        query = """select timestamp from weather"""
        return pd.read_sql(query, conn).timestamp.to_list()

    def get_recent_time_log(self):
        """Doc."""
        conn = get_db_conn()
        return pd.read_sql(
            """select timestamp from weather where (timestamp like '"""+self.date_today+"""%' 
            or timestamp like '"""+self.date_yesterday+"""%')""",
            conn
        ).timestamp.to_list()

    @property
    def today(self):
        """Return pandas TimeStamp for today."""
        return pd.Timestamp.today()

    @property
    def date_today(self):
        """Return date string of today."""
        return self.today.strftime('%Y-%m-%d')

    @property
    def date_yesterday(self):
        """Return date string of yesterday."""
        return (self.today - pd.Timedelta(days=1)).strftime('%Y-%m-%d')
