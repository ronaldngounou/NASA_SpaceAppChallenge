from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
from app import views