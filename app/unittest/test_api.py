import unittest
import requests
import json

class Test_api(unittest.TestCase):

# ----------------------user apis----------------------------------------------------

    def test_case1(self):
        request = requests.get("http://127.0.0.1:8000/allusers")
        self.assertEqual(request.status_code, 200)


    def test_case2(self):
        with open('details.json') as f:
            data = json.loads(f.read())
        request = requests.post("http://127.0.0.1:8000/signup", json=data)
        self.assertEqual(request.status_code, 200)
    

    def test_case3(self):
        request = requests.get("http://127.0.0.1:8000/data1/638054f3d046c9d88b04e11d")
        self.assertEqual(request.status_code, 200)


    def test_case4(self):
        with open('details.json') as f:
            data = json.loads(f.read())
        request = requests.put("http://127.0.0.1:8000/6389ca09e83dc6667fc2d993", json=data)
        self.assertEqual(request.status_code, 200)


    def test_case5(self):
        request = requests.delete("http://127.0.0.1:8000/6389c9747b87f776e0cc4bb1")
        self.assertEqual(request.status_code, 200)


    def test_case6(self):
        with open('details.json') as f:
            data = json.loads(f.read())
        request = requests.post("http://127.0.0.1:8000/login", json=data)
        self.assertEqual(request.status_code, 200)


# ----------------------------emp details-------------------------------------------------------


    def test_case7(self):
        with open('payload.json') as f:
            data = json.loads(f.read())
        request = requests.post("http://127.0.0.1:8000/data", json=data)
        self.assertEqual(request.status_code, 200)
    

    def test_case8(self):
        request = requests.get("http://127.0.0.1:8000/data/")
        self.assertEqual(request.status_code, 200)


    def test_case9(self):
        request = requests.get("http://127.0.0.1:8000/data/TEST1")
        self.assertEqual(request.status_code, 200)


    def test_case10(self):
        with open('payload.json') as f:
            data = json.loads(f.read())
        request = requests.put("http://127.0.0.1:8000/data/TEST1", json=data)
        self.assertEqual(request.status_code, 200)


    def test_case11(self):
        request = requests.delete("http://127.0.0.1:8000/data/TEST1")
        self.assertEqual(request.status_code, 200)


    def test_case12(self):
        request = requests.get("http://127.0.0.1:8000/emp_details/A3")
        self.assertEqual(request.status_code, 200)

# --------------------------------------MESSAGE------------------------------------------------------

    def test_case13(self):
        with open('msg.json') as f:
            data = json.loads(f.read())
        request = requests.post("http://127.0.0.1:8000/msg/", json=data)
        self.assertEqual(request.status_code, 200)


    def test_case14(self):
        request = requests.delete("http://127.0.0.1:8000/msgdlt/TESTING1")
        self.assertEqual(request.status_code, 200)

if __name__ == '__main__':
    unittest.main()
