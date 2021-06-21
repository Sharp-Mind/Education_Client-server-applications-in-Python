import unittest
import time
import client


class MsgAnswerChoiseFunctionAuthCase(unittest.TestCase):
    def setUp(self):
        client.s = client.connect()
        client.case = "authenticate"

    def testAnswerChoise(self):
        r = client.answer_choise({"response": "200", "alert": "OK"})
        self.assertEqual(
            r,
            {
                "action": "presence",
                "time": str(int(time.time())),
                "type": "status",
                "user": {
                    "account_name": "Bobik_Rubika",
                    "password": "TheblastFormThepast",
                },
            },
        )


class MsgAnswerChoiseFunctionPresenseCase(unittest.TestCase):
    def setUp(self):
        client.s = client.connect()
        client.case = "presence"

    def testAnswerChoise(self):
        r = client.answer_choise({"response": "200", "alert": "OK"})


class MsgAnswerChoiseFunctionQuitCase(unittest.TestCase):
    def setUp(self):
        client.s = client.connect()
        client.case = "quit"

    def testAnswerChoise(self):
        r = client.answer_choise({"response": "200", "alert": "OK"})
        self.assertNotEqual(r, {"action": "quit"})


class KeepitrollingFunctionQuitCase(unittest.TestCase):
    def setUp(self):
        client.s = client.connect()
        client.case = "quit"

    def testAnswerChoise(self):
        r = client.keepitrolling()
        self.assertEqual(client.s.fileno(), -1)


if __name__ == "__main__":
    unittest.main()
