from flask import Flask

webapp = Flask(__name__)

from app import manager
from app import worker