#!/bin/bash
pushd /home/drfrink/Documents/devProjects/automate_data
source venv/bin/activate
exec python /home/drfrink/Documents/devProjects/automate_data/poloniex_grabber/views.py
popd