game_config = {
    'ui_width': 60,
    'splash_text': ''' 
 _____   _       ____    _    _   _____ 
|  _  | | |     |  _ \  | |  | | |  _  |
| |_| | | |     | |_| | | |__| | | |_| |
|  _  | | |___  |  __/  |  __  | |  _  |
|_| |_| |_____| |_|     |_|  |_| |_| |_|
 ____    _____    _    __   _   _______ 
|  _ \  |  _  |  | |  |  \ | | |__   __|
| |_| | | | | |  | |  |   \| |    | |   
|  __/  | |_| |  | |  | |\   |    | |   
|_|     |_____|  |_|  |_| \__|    |_|   

''',
    'story_text_1': 'Marcus could sense the stillness of his environment -- vacuous and oppressive. Intense sunlight cut sharp-edged lines across the dusty, red rocks at his feet. Above, a high, streaky haze blurred the tawny blue and grey of the sky. In every direction there was more of the same: rocks, dust, and light; repeating, shrinking, and finally vanishing at the horizon.  In this place time itself was like a distant memory and the imperceptibly slow turn of shadows across the landscape was the only reminder that it still existed. There was no movement; no gentle breeze, no flowing water, no bounding life; only a vast, empty exapanse -- in a word, desolation.',
    'story_text_2': 'The chirp of Marcus\' integrated comm system was followed by the voice of his mission commander: "Marc, we neeed you back at base ASAP! There\'s been an incident in the lab." He shifted his gaze to the top-left corner of his suit\'s heads-up-display and keyed his mic with a blink. "Roger that, Tonia, what kind of incident?". Even as he finished speaking, Marcus began gathering and packing his instruments. "We don\'t know yet, but it doesn\'t look good.", Tonia replied, her Russian accent a little thicker than ususal, "One of the techs made a system-wide call warning everyone to stay away. The airlock is sealed and external control is disabled. We\'re still trying to establish contact." As chief science officer, Marcus knew laboratory emergency protocols better than anyone. They hadn\'t been followed. "Alright, I\'m heading back now. ETA twelve minutes. Who was scheduled for the lab today?", Marcus asked. Exactly Eleven minutes and thirty-two seconds later, as Marcus brought the rover to a stop in front of the Horizon-1 Mars Base, informally known as Alpha Point, there was still no response...'
}

player_config = {
    'name': 'Marcus'
}

levels_config = {
    'levels': {
        -1: {
            'name': 'Testing',
            'map': {
                'x_dimension': 5,
                'y_dimension': 5,
                'path_cells': [
                    {'coordinates': (0, 4), 'story_text': None},
                    {'coordinates': (0, 3), 'story_text': ('{0} breathed a sigh of relief as the airlock sealed behind him...').format(player_config['name'])},
                    {'coordinates': (0, 2), 'story_text': None},
                    {'coordinates': (1, 2), 'story_text': ('A glow emanated from the left side of the corridor ahead. "Is that a passage?", {0} wondered... ').format(player_config['name'])},
                    {'coordinates': (2, 2), 'story_text': None},
                    {'coordinates': (2, 1), 'story_text': None},
                    {'coordinates': (3, 2), 'story_text': None},
                    {'coordinates': (4, 2), 'story_text': None},
                    {'coordinates': (4, 1), 'story_text': None},
                    {'coordinates': (4, 0), 'story_text': None},
                    {'coordinates': (4, 3), 'story_text': None}
                ],
                'coord_enter': (0, 3),  # begin
                'coord_exit': (4, 0),  # end
                'orientation_enter': 0,
                'tools': [],
                'artifacts': []
            },
            'system': {
                'interfaces': [
                    {
                        'id': 0,
                        'name': 'entrance door button',
                        'description': 'button',
                        'type': 'button',
                        'enabled': True,
                        'x': 0,
                        'y': 4,
                        'orientation': 0,
                        'msg_action_verb': 'push'
                    },
                    {
                        'id': 1,
                        'name': 'door circuit toggleswitch',
                        'description': 'switch',
                        'type': 'toggleswitch',
                        'enabled': True,
                        'x': 2,
                        'y': 0,
                        'orientation': 2,
                        'msg_action_verb': 'flip'
                    },
                    {
                        'id': 2,
                        'name': 'system terminal',
                        'description': 'system terminal',
                        'type': 'terminal',
                        'enabled': True,
                        'x': 4,
                        'y': 4,
                        'orientation': 0,
                        'msg_action_verb': 'use'
                    },
                    {
                        'id': 3,
                        'name': 'exit door button',
                        'description': 'button',
                        'type': 'button',
                        'enabled': True,
                        'x': 4,
                        'y': 0,
                        'orientation': 2,
                        'msg_action_verb': 'push'
                    }
                ],
                'devices': [
                    {
                        'id': 0,
                        'name': 'entrance door',
                        'description': 'door',
                        'type': 'door',
                        'enabled': False,
                        'active': False,
                        'x': 0,
                        'y': 4,
                        'msg_action_true': 'open',
                        'msg_action_false': 'close',
                        'msg_active_true': 'The door is open.',
                        'msg_active_false': 'The door is closed.',
                        'msg_toggle_active_true': 'The door opened.',
                        'msg_toggle_active_false': 'The door closed.',
                        'msg_unmet_dependencies': 'The door is locked.',
                        'dependencies': []
                    },
                    {
                        'id': 1,
                        'name': 'door circuit switch',
                        'description': 'door circuit',
                        'type': 'switch',
                        'enabled': True,
                        'active': False,
                        'x': 2,
                        'y': 0,
                        'msg_action_true': 'close',
                        'msg_action_false': 'open',
                        'msg_active_true': 'The circuit is closed.',
                        'msg_active_false': 'The circuit is open.',
                        'msg_toggle_active_true': 'Do you hear that? It sounds like electric current.',
                        'msg_toggle_active_false': 'That electric hum went away.',
                        'msg_unmet_dependencies': 'The circuit switch isn\'t responding.',
                        'dependencies': []
                    },
                    {
                        'id': 2,
                        'name': 'exit door',
                        'description': 'door',
                        'type': 'door',
                        'enabled': True,
                        'active': False,
                        'x': 4,
                        'y': 0,
                        'msg_action_true': 'open',
                        'msg_action_false': 'close',
                        'msg_active_true': 'The door is open.',
                        'msg_active_false': 'The door is closed.',
                        'msg_toggle_active_true': 'The door opened.',
                        'msg_toggle_active_false': 'The door closed.',
                        'msg_unmet_dependencies': 'An indicator shows the door is locked.',
                        'dependencies': [
                            {'device_id': 1, 'active_state': True}
                        ]
                    },
                    {
                        'id': 3,
                        'name': 'exit door camera',
                        'description': 'security camera',
                        'type': 'camera',
                        'enabled': True,
                        'active': True,
                        'x': 4,
                        'y': 0,
                        'msg_action_true': 'turn on',
                        'msg_action_false': 'turn off',
                        'msg_active_true': 'The camera is on.',
                        'msg_active_false': 'The camera is off.',
                        'msg_toggle_active_true': 'The camera viewer flashed on and I see a man standing at a terminal.',
                        'msg_toggle_active_false': 'The camera viewer went dark.',
                        'msg_unmet_dependencies': 'The camera isn\'t responding.',
                        'dependencies': []
                    }
                ],
                'links': [
                    {'interface_id': 0, 'device_id': 0},
                    {'interface_id': 1, 'device_id': 1},
                    {'interface_id': 2, 'device_id': 1},
                    {'interface_id': 2, 'device_id': 2},
                    {'interface_id': 2, 'device_id': 3},
                    {'interface_id': 3, 'device_id': 2}
                ]
            }
        },
        0: {
            'name': 'The Void',
            'map': {
                'x_dimension': 1,
                'y_dimension': 2,
                'path_cells': [
                    {'coordinates': (0, 0), 'story_text': None},
                    {'coordinates': (0, 1), 'story_text': 'This place is not for you. Run along now...'}
                ],
                'coord_enter': (0, 1),  # begin
                'coord_exit': (0, 0),  # end
                'orientation_enter': 0,
                'tools': [],
                'artifacts': []
            },
            'system': {
                'interfaces': [],
                'devices': [],
                'links': []
            }
        },
        1: {
            'name': 'Entrance',
            'map': {
                'x_dimension': 5,
                'y_dimension': 5,
                'path_cells': [
                    {'coordinates': (2, 4), 'story_text': None},
                    {'coordinates': (2, 3), 'story_text': ('{0} stepped off the rover ladder and a faint mushroom cloud of dust bloomed out from under his boot as each particle traced a parabolic arc in slow motion. "Something is very wrong.", he thought, while surveying the environment for any sign of disaster. Everything was in place. There were no signs of an explosion or collapse. The light over the external airlock door glowed green indicating its pressure matched that of the external environment. According to his suit\'s computer, he still had active comm and telemetry links with Alpha Point but all he could hear was the sound of his own breathing. "What the hell?", Marcus wondered, as he headed toward the airlock.').format(player_config['name'])},
                    {'coordinates': (2, 2), 'story_text': None},
                    {'coordinates': (2, 1), 'story_text': None},
                    {'coordinates': (2, 0), 'story_text': None},
                    {'coordinates': (3, 3), 'story_text': None},
                    {'coordinates': (4, 3), 'story_text': None},
                    {'coordinates': (1, 1), 'story_text': None},
                    {'coordinates': (0, 1), 'story_text': None}
                ],
                'coord_enter': (2, 3),  # begin
                'coord_exit': (2, 0),  # end
                'orientation_enter': 0,
                'tools': [],
                'artifacts': []
            },
            'system': {
                'interfaces': [
                    {
                        'id': 0,
                        'name': 'airlock door button',
                        'description': 'button',
                        'type': 'button',
                        'enabled': True,
                        'x': 2,
                        'y': 0,
                        'orientation': 2,
                        'msg_action_verb': 'push'
                    }
                ],
                'devices': [
                    {
                        'id': 0,
                        'name': 'rover',
                        'description': 'rover',
                        'type': 'door',
                        'enabled': False,
                        'active': False,
                        'x': 2,
                        'y': 4,
                        'msg_action_true': 'open',
                        'msg_action_false': 'close',
                        'msg_active_true': 'The door is open.',
                        'msg_active_false': 'The door is closed.',
                        'msg_toggle_active_true': 'The door opened.',
                        'msg_toggle_active_false': 'The door closed.',
                        'msg_unmet_dependencies': 'The door is locked.',
                        'dependencies': []
                    },
                    {
                        'id': 1,
                        'name': 'solar array',
                        'description': 'solar array',
                        'type': 'door',
                        'enabled': False,
                        'active': False,
                        'x': 4,
                        'y': 3,
                        'msg_action_true': 'open',
                        'msg_action_false': 'close',
                        'msg_active_true': 'The door is open.',
                        'msg_active_false': 'The door is closed.',
                        'msg_toggle_active_true': 'The door opened.',
                        'msg_toggle_active_false': 'The door closed.',
                        'msg_unmet_dependencies': 'The door is locked.',
                        'dependencies': []
                    },
                    {
                        'id': 2,
                        'name': 'communications array',
                        'description': 'communications array',
                        'type': 'door',
                        'enabled': False,
                        'active': False,
                        'x': 0,
                        'y': 1,
                        'msg_action_true': 'open',
                        'msg_action_false': 'close',
                        'msg_active_true': 'The door is open.',
                        'msg_active_false': 'The door is closed.',
                        'msg_toggle_active_true': 'The door opened.',
                        'msg_toggle_active_false': 'The door closed.',
                        'msg_unmet_dependencies': 'The door is locked.',
                        'dependencies': []
                    },
                    {
                        'id': 4,
                        'name': 'airlock door',
                        'description': 'door',
                        'type': 'door',
                        'enabled': True,
                        'active': False,
                        'x': 2,
                        'y': 0,
                        'msg_action_true': 'open',
                        'msg_action_false': 'close',
                        'msg_active_true': 'The door is open.',
                        'msg_active_false': 'The door is closed.',
                        'msg_toggle_active_true': 'The door opened.',
                        'msg_toggle_active_false': 'The door closed.',
                        'msg_unmet_dependencies': 'The door is locked.',
                        'dependencies': []
                    }
                ],
                'links': [
                    {'interface_id': 0, 'device_id': 4}
                ]
            }
        },
        2: {
            'name': 'Airlock',
            'map': {
                'x_dimension': 5,
                'y_dimension': 3,
                'path_cells': [
                    {'coordinates': (0, 1), 'story_text': None},
                    {'coordinates': (1, 1), 'story_text': ('{0} checked his mission clock as the door sealed behind him. He was thirty minutes ahead of schedule. "Alright, focus.", he thought, "Follow the ingress procedure."').format(player_config['name'])},
                    {'coordinates': (2, 1), 'story_text': None},
                    {'coordinates': (3, 1), 'story_text': None},
                    {'coordinates': (4, 1), 'story_text': None}
                ],
                'coord_enter': (1, 1),  # begin
                'coord_exit': (4, 1),  # end
                'orientation_enter': 1,
                'tools': [],
                'artifacts': []
            },
            'system': {
                'interfaces': [
                    {
                        'id': 0,
                        'name': 'airlock pressurization button',
                        'description': 'button labeled "Pressure Control"',
                        'type': 'button',
                        'enabled': True,
                        'x': 2,
                        'y': 0,
                        'orientation': 2,
                        'msg_action_verb': 'push'
                    },
                    {
                        'id': 1,
                        'name': 'airlock pressurization handwheel',
                        'description': 'yellow handwheel labeled "Pressure Control - Manual Override"',
                        'type': 'handwheel',
                        'enabled': True,
                        'x': 2,
                        'y': 2,
                        'orientation': 0,
                        'msg_action_verb': 'turn'
                    },
                    {
                        'id': 2,
                        'name': 'exit door button',
                        'description': 'button',
                        'type': 'button',
                        'enabled': True,
                        'x': 4,
                        'y': 1,
                        'orientation': 3,
                        'msg_action_verb': 'push'
                    }
                ],
                'devices': [
                    {
                        'id': 0,
                        'name': 'entrance door',
                        'description': 'door',
                        'type': 'door',
                        'enabled': False,
                        'active': False,
                        'x': 0,
                        'y': 1,
                        'msg_action_true': 'open',
                        'msg_action_false': 'close',
                        'msg_active_true': 'The door is open.',
                        'msg_active_false': 'The door is closed.',
                        'msg_toggle_active_true': 'The door opened.',
                        'msg_toggle_active_false': 'The door closed.',
                        'msg_unmet_dependencies': 'The door is locked.',
                        'dependencies': []
                    },
                    {
                        'id': 1,
                        'name': 'airlock pressurization valve',
                        'description': 'pressurization valve',
                        'type': 'valve',
                        'enabled': True,
                        'active': False,
                        'x': 2,
                        'y': 2,
                        'msg_action_true': 'open',
                        'msg_action_false': 'close',
                        'msg_active_true': 'The valve is open.',
                        'msg_active_false': 'The valve is closed.',
                        'msg_toggle_active_true': 'My suit collapsed and the green internal door indicator reads "Airlock Pressurized".',
                        'msg_toggle_active_false': 'My suit expanded and the red internal door indicator reads "Airlock Purged".',
                        'msg_unmet_dependencies': 'The valve isn\'t responding.',
                        'dependencies': []
                    },
                    {
                        'id': 2,
                        'name': 'exit door',
                        'description': 'door',
                        'type': 'door',
                        'enabled': True,
                        'active': False,
                        'x': 4,
                        'y': 1,
                        'msg_action_true': 'open',
                        'msg_action_false': 'close',
                        'msg_active_true': 'The door is open.',
                        'msg_active_false': 'The door is closed.',
                        'msg_toggle_active_true': 'The door opened.',
                        'msg_toggle_active_false': 'The door closed.',
                        'msg_unmet_dependencies': 'The door is locked.',
                        'dependencies': [
                            {'device_id': 1, 'active_state': True}
                        ]
                    }
                ],
                'links': [
                    {'interface_id': 1, 'device_id': 1},
                    {'interface_id': 2, 'device_id': 2}
                ]
            }
        },
        3: {
            'name': 'Equipment',
            'map': {
                'x_dimension': 9,
                'y_dimension': 9,
                'path_cells': [
                    {'coordinates': (4, 0), 'story_text': None},
                    {'coordinates': (4, 1), 'story_text': None},
                    {'coordinates': (4, 2), 'story_text': None},
                    {'coordinates': (4, 3), 'story_text': None},
                    {'coordinates': (4, 4), 'story_text': None},
                    {'coordinates': (4, 5), 'story_text': None},
                    {'coordinates': (4, 6), 'story_text': None},
                    {'coordinates': (4, 7), 'story_text': None},
                    {'coordinates': (4, 8), 'story_text': 'Equipment storage story text...'},
                    {'coordinates': (3, 6), 'story_text': None},
                    {'coordinates': (2, 6), 'story_text': None},
                    {'coordinates': (1, 6), 'story_text': None},
                    {'coordinates': (5, 6), 'story_text': None},
                    {'coordinates': (6, 6), 'story_text': None},
                    {'coordinates': (7, 6), 'story_text': None},
                    {'coordinates': (3, 4), 'story_text': None},
                    {'coordinates': (2, 4), 'story_text': None},
                    {'coordinates': (1, 4), 'story_text': None},
                    {'coordinates': (5, 4), 'story_text': None},
                    {'coordinates': (6, 4), 'story_text': None},
                    {'coordinates': (7, 4), 'story_text': None},
                    {'coordinates': (3, 2), 'story_text': None},
                    {'coordinates': (2, 2), 'story_text': None},
                    {'coordinates': (1, 2), 'story_text': None},
                    {'coordinates': (5, 2), 'story_text': None},
                    {'coordinates': (6, 2), 'story_text': None},
                    {'coordinates': (7, 2), 'story_text': None}
                ],
                'coord_enter': (4, 7),  # begin
                'coord_exit': (4, 0),  # end
                'orientation_enter': 0,
                'tools': [
                    {
                        'type': 'wrench',
                        'name': 'wrench',
                        'description': 'wrench',
                        'x': 4,
                        'y': 6
                    }
                ],
                'artifacts': []
            },
            'system': {
                'interfaces': [],
                'devices': [
                    {
                        'id': 0,
                        'name': 'entrance door',
                        'description': 'door',
                        'type': 'door',
                        'enabled': False,
                        'active': False,
                        'x': 4,
                        'y': 8,
                        'msg_action_true': 'open',
                        'msg_action_false': 'close',
                        'msg_active_true': 'The door is open.',
                        'msg_active_false': 'The door is closed.',
                        'msg_toggle_active_true': 'The door opened.',
                        'msg_toggle_active_false': 'The door closed.',
                        'msg_unmet_dependencies': 'The door is locked.',
                        'dependencies': []
                    },
                    {
                        'id': 1,
                        'name': 'exit door',
                        'description': 'door',
                        'type': 'door',
                        'enabled': True,
                        'active': False,
                        'x': 4,
                        'y': 0,
                        'msg_action_true': 'open',
                        'msg_action_false': 'close',
                        'msg_active_true': 'The door is open.',
                        'msg_active_false': 'The door is closed.',
                        'msg_toggle_active_true': 'The door opened.',
                        'msg_toggle_active_false': 'The door closed.',
                        'msg_unmet_dependencies': 'The door is locked.',
                        'dependencies': []
                    }
                ],
                'links': []
            }
        }
    }
}
