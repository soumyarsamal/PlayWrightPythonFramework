from jsonpath_ng import parse


class JsonResponseValidator:
    """
    A class to validate JSON responses using JSONPath with chaining support.
    """

    def __init__(self, json_response):
        """
        Initialize the validator with a JSON response.

        :param json_response: The JSON object to validate
        """
        self.json_response = json_response

    def assert_json(self, json_path, expected_value):
        """
        Asserts that the value at the given JSONPath in the JSON response matches the expected value.

        :param json_path: The JSONPath string to locate the field
        :param expected_value: The expected value to compare
        :return: Self (for chaining)
        :raises AssertionError: If the JSONPath is not found or the value does not match
        """
        jsonpath_expression = parse(json_path)  # Parse the JSONPath
        match = jsonpath_expression.find(self.json_response)  # Find matches in the JSON

        assert match, f"No match found for JSONPath: {json_path}"  # Ensure the path exists
        actual_value = match[0].value  # Get the value from the first match
        assert actual_value == expected_value, (
            f"Assertion failed for JSONPath: {json_path}. "
            f"Expected: {expected_value}, Found: {actual_value}"
        )
        print(f"Assertion passed for {json_path}: {expected_value}")
        return self  # Return self to enable chaining
