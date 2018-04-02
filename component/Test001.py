import unittest
import xml.etree.ElementTree as ET
from hdfs.client import Client


class MyTestCase(unittest.TestCase):
    def test_something(self):
        client = Client("http://172.18.130.100:50070")
        with client.read("/liupei/test/template.xml") as fs:
            content = fs.read()
            print(content)


if __name__ == '__main__':
    unittest.main()
