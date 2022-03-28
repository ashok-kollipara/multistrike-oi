#!/usr/bin/python3
import db_actions as db
import ui

if __name__=='__main__':

    #check database exists, create if not
    db.check_db()

    #start UI
    ui.ui_workspace()

    #clear database before close
    db.reset_table_data()
