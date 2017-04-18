import copy
import unittest
import weather
import secrets

class TestWeather(unittest.TestCase):

    EVENT = {
        'request': {
            'type': "IntentRequest",
            'intent': {
                'name': "WeatherReport",
                'slots': {
                    'aspect': {
                        'name': 'aspect',
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
        'humidity': "relative humidity .*\d.\d percent",
        "moon_phase": "new moon|crescent|quarter|gibbous|full moon",
        "pressure": "pressure .*\d.\d inches of mercury",
        "rainfall": "no significant rainfall|\d.\d inches",
        "temperature": "temperature .*\d.\d degrees",
        "wind": "wind .*\d.\d miles per hour"
    }

    # def setUp(self):
    #     print("setup")
    #
    # def tearDown(self):
    #     print("teardown")

    def test_humidity(self):
        self.EVENT['request']['intent']['slots']['aspect']['value'] = "humidity"
        result = weather.weather_handler(self.EVENT, {})

        self.assertRegexpMatches(
            result['response']['outputSpeech']['text'],
            self.test_patterns['humidity']
        )

    def test_moon_phase(self):
        self.EVENT['request']['intent']['slots']['aspect']['value'] = "moon phase"
        result = weather.weather_handler(self.EVENT, {})

        self.assertRegexpMatches(
            result['response']['outputSpeech']['text'],
            self.test_patterns['moon_phase']
        )

    def test_pressure(self):
        self.EVENT['request']['intent']['slots']['aspect']['value'] = "pressure"
        result = weather.weather_handler(self.EVENT, {})

        self.assertRegexpMatches(
            result['response']['outputSpeech']['text'],
            self.test_patterns['pressure']
        )

    def test_rainfall(self):
        self.EVENT['request']['intent']['slots']['aspect']['value'] = "rainfall"
        result = weather.weather_handler(self.EVENT, {})

        self.assertRegexpMatches(
            result['response']['outputSpeech']['text'],
            self.test_patterns['rainfall']
        )

    def test_temperature(self):
        self.EVENT['request']['intent']['slots']['aspect']['value'] = "temperature"
        result = weather.weather_handler(self.EVENT, {})

        self.assertRegexpMatches(
            result['response']['outputSpeech']['text'],
            self.test_patterns['temperature']
        )

    def test_weather(self):
        self.EVENT['request']['intent']['slots']['aspect']['value'] = "weather"
        result = weather.weather_handler(self.EVENT, {})

        for name,pattern in self.test_patterns.iteritems():
            self.assertRegexpMatches(
                result['response']['outputSpeech']['text'],
                pattern,
                name
            )

    def test_wind(self):
        self.EVENT['request']['intent']['slots']['aspect']['value'] = "wind"
        result = weather.weather_handler(self.EVENT, {})

        self.assertRegexpMatches(
            result['response']['outputSpeech']['text'],
            self.test_patterns['wind']
        )

    def test_incorrect_app_id(self):
        event = copy.deepcopy(self.EVENT)
        event['session']['application']['applicationId'] = "foo bar"
        with self.assertRaises(ValueError):
            weather.weather_handler(event, {})

################################################################################
if __name__ == "__main__":
    unittest.main()
