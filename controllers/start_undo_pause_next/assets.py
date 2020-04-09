from app import  db, session, Node_Base, Column, relationship, ansible
from datetime import  datetime
import  models
import os
import json


def get_service_setups_from_deployment(deployment):
    def sort_function(e):
        return e.setup_index

    service_setups = deployment.service_setups
    service_setups.sort(key=sort_function)
    return service_setups