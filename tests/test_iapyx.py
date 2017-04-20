import copy
import unittest
import iapyx
import secrets

class TestIapyx(unittest.TestCase):

    EVENT = {
        'request': {
            'type': "IntentRequest",
            'intent': {
                'name': "TheButton",
                'slots': {
                    'action': {
                        'name': 'action',
                        'value': None
                    },
                    'product': {
                        'name': 'product',
                        'value': None
                    }
                }
            }
        },
        'session': {
            'new': True,
            'application': {
                'applicationId': secrets.APPLICATION_ID
            }
        }
    }

    test_patterns = {
        'test': "TheButton Test",
        'deploy': 'TheButton Deploy pandora',
        'spin': 'TheButton Spin'
    }

    # def setUp(self):
    #     print("setup")
    #
    # def tearDown(self):
    #     print("teardown")

    def test_test(self):
        self.EVENT['request']['intent']['slots']['action']['value'] = "test"
        result = iapyx.iapyx_handler(self.EVENT, {})

        self.assertRegexpMatches(
            result['response']['outputSpeech']['text'],
            self.test_patterns['test']
        )

    def test_deploy(self):
        self.EVENT['request']['intent']['slots']['action']['value'] = "deploy"
        self.EVENT['request']['intent']['slots']['product']['value'] = "pandora"
        result = iapyx.iapyx_handler(self.EVENT, {})

        self.assertRegexpMatches(
            result['response']['outputSpeech']['text'],
            self.test_patterns['deploy']
        )

    def test_spin(self):
        self.EVENT['request']['intent']['slots']['action']['value'] = "spin"
        result = iapyx.iapyx_handler(self.EVENT, {})

        self.assertRegexpMatches(
            result['response']['outputSpeech']['text'],
            self.test_patterns['spin']
        )

    def test_incorrect_app_id(self):
        event = copy.deepcopy(self.EVENT)
        event['session']['application']['applicationId'] = "foo bar"
        with self.assertRaises(ValueError):
            iapyx.iapyx_handler(event, {})

################################################################################
if __name__ == "__main__":
    unittest.main()
