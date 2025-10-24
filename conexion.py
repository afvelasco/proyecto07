from datetime import timedelta
import os
from random import randint
from flask import Flask, redirect, render_template, request, send_from_directory, session
import mysql.connector
import hashlib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app = Flask(__name__)
app.secret_key = str(randint(100000,999999))
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=15)
miDB = mysql.connector.connect(host="localhost",
                               port="3306",
                               user="root",
                               password="",
                               database="proyecto07")
mi_cursor = miDB.cursor()
app.config['CARPETAUP'] = os.path.join('uploads')
