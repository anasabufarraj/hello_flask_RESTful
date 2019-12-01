#!/usr/bin/env python
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj
# ------------------------------------------------------------------------------

USERNAME_MAPPING = {
    'john': {
        'id': 1,
        'username': 'john',
        'password': '123'
    },
    'sarah': {
        'id': 2,
        'username': 'sarah',
        'password': '456'
    }
}

user = USERNAME_MAPPING.get('johns', None)

print(user)
