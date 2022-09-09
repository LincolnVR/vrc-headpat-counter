import unittest
from osc_counter.usersettings import UserSettings


class TestUserSettings(unittest.TestCase):

    def setUp(self):
       self.user_settings = UserSettings()

    def test_force_minimum(self):
        user_set_min = -2
        desired_min = 1
        result: int = self.user_settings.force_minimum(user_set_min, desired_min)
        self.assertEqual(result, desired_min)

        user_set_min = 30
        desired_min = 1
        result: int = self.user_settings.force_minimum(user_set_min, desired_min)
        self.assertEqual(result, user_set_min)


if __name__ == '__main__':
    unittest.main()