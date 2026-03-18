"""
Mock up testing examples.
"""

import subprocess
import unittest
from unittest.mock import mock_open, patch

from white_box.mockup_exercises import (
    execute_command,
    fetch_data_from_api,
    perform_action_based_on_time,
    read_data_from_file,
)


class TestFetchDataFromApi(unittest.TestCase):
    """
    Fetch data from API unittest class
    """

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """
        Success case
        """
        # configuro la respuesta del mock
        mock_get.return_value.json.return_value = {"key": "value"}

        result = fetch_data_from_api("https://api.example.com/data")

        self.assertEqual(result, {"key": "value"})
        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)


class TestPerformActionBasedOnTime(unittest.TestCase):
    """
    Perform Action Based On Time unittest class
    """

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_based_on_time_action_a(self, mock_time):
        """
        Action A
        """
        mock_time.return_value = 5

        result = perform_action_based_on_time()

        self.assertEqual(result, "Action A")

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_based_on_time_action_b(self, mock_time):
        """
        Action B
        """
        mock_time.return_value = 15

        result = perform_action_based_on_time()

        self.assertEqual(result, "Action B")


class TestReadDataFromFile(unittest.TestCase):
    """
    Read data from file unittest class
    """

    @patch("builtins.open", new_callable=mock_open, read_data="mocked file content")
    def test_read_data_from_file_success(self, mock_file):
        """
        Success case for reading a file
        """
        filename = "test.txt"
        
        result = read_data_from_file(filename)

        self.assertEqual(result, "mocked file content")
        
        mock_file.assert_called_once_with(filename, encoding="utf-8")

    @patch("builtins.open")
    def test_read_data_from_file_not_found(self, mock_file):
        """
        FileNotFoundError exception case
        """
        mock_file.side_effect = FileNotFoundError("File not found")
        
        filename = "missing.txt"
        
        with self.assertRaises(FileNotFoundError):
            read_data_from_file(filename)


class TestExecuteCommand(unittest.TestCase):
    """
    Execute command unittest class
    """

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_success(self, mock_run):
        """
        Success case for executing a command
        """
        mock_run.return_value.stdout = "Command executed successfully\n"
        
        command = ["echo", "hello"]
        
        result = execute_command(command)

        self.assertEqual(result, "Command executed successfully\n")
        
        mock_run.assert_called_once_with(
            command, capture_output=True, check=False, text=True
        )

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_called_process_error(self, mock_run):
        """
        Exception case
        """
        command = ["ls", "-invalid"]
        
        mock_run.side_effect = subprocess.CalledProcessError(returncode=1, cmd=command)
        
        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(command)
