"""
Darson Hak
October 15th, 2025
Lab #10: File Operation Test
"""

import unittest
import os
from file_operations import read_file, write_file, append_file, email_read


class TestFileOperations(unittest.TestCase):
    def setUp(self):
        # set up temporary test file name before each test
        self.filename = "test_file.txt"

    def tearDown(self):
        # remove the test file after each test
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_write_file(self):
        # test writing text to file
        msg = "Darson Hak"
        with open(self.filename, "w") as f:
            f.write(msg)

        # verify file exits and content matches
        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, "r") as f:
            result = f.read()

        self.assertEqual(result, msg)

    def test_read_file(self):
        # test reading text from a file
        expected_content = "Read me!"
        with open(self.filename, "w") as f:
            f.write(expected_content)

        with open(self.filename, "r") as f:
            data = f.read()

        self.assertEqual(data, expected_content)

    def test_append_file(self):
        # test appending text to an existing file
        initial_content = "Line one"
        append_content = "\nLine two"

        with open(self.filename, "w") as f:
            f.write(initial_content)

        with open(self.filename, "a") as f:
            f.write(append_content)

        with open(self.filename, "r") as f:
            final_data = f.read()

        self.assertEqual(final_data, initial_content + append_content)

    # LAB EXERCISE
    def test_email_read(self):
        user_email = """
                        Nick Carter, ncarter@yahoo.com
                        Vanessa Singh, vsingh@gmail.com
                        Ann Parker, aparker@gmail.com
                        Phil Chen, pchen@hotmail.com
                        Fiona Smith, fsmith@gmail.com
                        Joshue Candela, jcandela@yahoo.com
                        Carl Peterson, cpeterson@hotmail.com
                        Kevin Brook, kbrook@gmail.com 
                        Theresa Ng, tng@hotmail.com
                        Joe Hunter, jhunter@yahoo.com
                        Patricia Franco, pfranco@gmail.com
                        Marie Mansion, mmansion@gmail.com
                        Carla Lee, clee@hotmail.com
                        """

        email_file = self.filename
        report_file = "test_report.txt"

        with open(email_file, "w") as f:
            f.write(user_email)

        email_read(email_file, report_file)

        with open(report_file, "r") as f:
            lines = f.read().splitlines()

        expected = ["yahoo = 3", "gmail = 6", "hotmail = 4"]

        self.assertEqual(lines, expected)


# run the unittest automatically when the file is run
if __name__ == "__main__":
    unittest.main()
