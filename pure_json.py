from collections import abc
from datetime import datetime
from dateutil import parser
import json, sys, uuid

from pyrsistent import field, thaw
from pyrsistent_ext import PRecordExt

def valid_date(maybe_valid_date: str) -> tuple:
    return (isinstance(parser.isoparse(maybe_valid_date), datetime), 'valid date')

class PureJsonInfo(PRecordExt):
    createdDate = field(type=str, invariant=valid_date)
    modifiedDate = field(type=str, invariant=valid_date)

def valid_uuid(maybe_valid_uuid: str) -> tuple:
    return (isinstance(uuid.UUID(maybe_valid_uuid), uuid.UUID), 'valid uuid')

class PureJson(PRecordExt):
    uuid = field(type=str, invariant=valid_uuid)
    info = field(type=PureJsonInfo)

def examine_pure_json_record(pure_json: PureJson):
    assert isinstance(pure_json, (PureJson, abc.Mapping))

    print(f'{pure_json.uuid=}')
    print(f'{pure_json.info=}')
    print('pure json info:')
    for k, v in pure_json.info.items():
        print(f'  {k=}, {v=}')

    print('all pure json keys:')
    for key in pure_json.keys():
        print(' ', key)

    pure_json['uuid'] = 'bogus'

    pure_json_string = json.dumps(thaw(pure_json))

json_filename = sys.argv[1]

with open(json_filename) as json_file:
    pure_json_dict = json.load(json_file)
    pure_json = PureJson.create(pure_json_dict)
    examine_pure_json_record(pure_json)
