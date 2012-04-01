# -*- coding: utf-8 -*-

import json

def serialize_to_stream(method, objects, stream, **options):
    json.dumps(objects, stream)
