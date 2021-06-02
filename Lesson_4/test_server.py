import unittest
import time
import server


class AuthCaseFunction(unittest.TestCase):

    def testauthenticatecase200(self):
        r = server.auth_case({"action": "authenticate", "time": str(int(time.time())), "user": {
            "account_name": "Bobik_Rubika", "password": "TheblastFormThepast"}})
        self.assertEqual(r, {"response": '200', "alert": "OK"})

    def testauthenticatecase402(self):
        r = server.auth_case({"action": "authenticate", "time": str(int(time.time())), "user": {
            "account_name": "Kon_v_palto", "password": "igogo123"}})
        self.assertEqual(
            r, {"response": '402', "error": "This could be 'wrong password' or 'no account with that name'"})


class AuthCase409Function(unittest.TestCase):
    def setUp(self):
        server.known_users = {'Bobik_Rubika': 'TheblastFormThepast'}
        server.auth_users = ['Bobik_Rubika']

    def tearDown(self):
        server.auth_users = []

    def testauthincatecase409(self):
        r = server.auth_case({"action": "authenticate", "time": str(int(time.time())), "user": {
                             "account_name": "Bobik_Rubika", "password": "TheblastFormThepast"}})
        self.assertEqual(
            r, {"response": '409', "error": "Someone is already connected with the given user name"})


class RollmycasesFunction(unittest.TestCase):

    def testpresence200(self):
        data = {"action": "presence", "time": str(int(time.time())), "type": "status", "user": {
            "account_name": "Bobik_Rubika", "password": "TheblastFormThepast"}}
        r = server.roll_my_cases(data['action'])
        self.assertEqual(r, {"response": '200', "alert": "OK"})

    def testquitcase200(self):
        data = {"action": "quit"}
        r = server.roll_my_cases(data['action'])
        self.assertEqual(r, {"response": '200', "alert": "OK"})


class RollmycasesFunctionNotEqual(unittest.TestCase):

    def testquitcase(self):
        self.assertNotEqual(server.roll_my_cases("quit"), '')

    def testpresensecase(self):
        self.assertNotEqual(server.roll_my_cases("presence"), '')

    def testquitcase200(self):
        data = {"action": "qwe"}
        r = server.roll_my_cases(data['action'])
        self.assertNotEqual(r, {"response": '200', "alert": "OK"})


class AuthCaseFunctionNotEqual(unittest.TestCase):

    def testauthcase(self):
        self.assertNotEqual(server.auth_case({"action": "authenticate", "time": str(int(time.time())), "user": {
            "account_name": "Bobik_Rubika", "password": "TheblastFormThepast"}}), '')


class ErrorCaseFunctionEqual(unittest.TestCase):

    def testauthcase(self):
        r = server.roll_my_cases({"action": "destroy", "time": str(int(time.time())), "user": {
            "account_name": "Bobik_Rubika", "password": "TheblastFormThepast"}})

        self.assertEqual(r, {"response": '404', "error": "Unknown message"})


if __name__ == '__main__':
    unittest.main()
