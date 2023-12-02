#!/bin/bash
waitress-serve --port=8000  watchmate.wsgi:application
