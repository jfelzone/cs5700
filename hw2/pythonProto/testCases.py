import unittest
from observers import *
from readData import Subject
import smtplib


class TestMethods(unittest.TestCase):

    def test_subscribe(self):
        test = Subscriber('test')
        self.assertEqual(test.name, 'test')
        print "test completed"

    def test_register(self):
        test = Subscriber('test')
        sub = Subject()
        sub.register(test)
        self.assertEqual(len(sub.subscribers), 1) 
        print "test completed"
         

    def test_register_multiple(self):
        test = Subscriber('test')
        sub = Subject()
        sub.register(test)
        test2 = Subscriber('test2')
        sub.register(test2)
        self.assertEqual(len(sub.subscribers), 2)   
        print "test completed"
        
    
    def test_register_multiples(self):
        test = Subscriber('test')
        sub = Subject()
        sub.register(test)
        test2 = Subscriber('test2')
        sub.register(test2)
        test3 = Subscriber('test3')
        sub.register(test3)
        self.assertEqual(len(sub.subscribers),3)   
        print "test completed"
        

    def test_streamer(self):
        listbox = Listbox()
        test = streamer("name", listbox)
        data = ["hello", "test"]
        self.assertEqual(test.getString(data), "test")
        print "test completed"
        

    def test_decorator(self):
        listbox = Listbox()
        test = streamer("name", listbox)
        data = ["hello", "test"]
        test = decorator(test)
        self.assertEqual(test.getString(data), "hello test")
        print "test completed"
        

    def test_guiTicker1(self):
        canvas = Canvas()
        test = guiTicker("test", canvas,0,0,12,9000,300)
        self.assertEqual(test.name, "test")
        print "test completed"
        
        
    def test_guiTicker2(self):
        canvas = Canvas()
        test = guiTicker("test", canvas,0,0,12,9000,300)
        self.assertEqual(test.jerseynumber,12)
        print "test completed"
        

    def test_guiTicker3(self):
        canvas = Canvas()
        test = guiTicker("test", canvas,0,0,12,9000,300)
        self.assertEqual(test.totaldistance,9000)
        print "test completed"
        

    def test_guiTicker4(self):
        canvas = Canvas()
        test = guiTicker("test", canvas,0,0,12,9000,300)
        self.assertEqual(test.totalwindowsize, 300)
        print "test completed"
        

    def test_guiTicker5(self):
        canvas = Canvas()
        test = guiTicker("test", canvas,0,0,12,9000,300)
        self.assertEqual(test.calculateMovement(300), 10)
        print "test completed"


if __name__ == '__main__':
    unittest.main()