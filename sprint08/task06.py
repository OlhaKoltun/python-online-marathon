import unittest
import unittest.mock


def file_parser(*args):
    with open(args[0], 'rt') as r_file:
        text = r_file.read()
    count = text.count(args[1])
    if len(args) == 2:
        return f'Found {count} strings'
    elif len(args) == 3:
        text = text.replace(args[1], args[2])
        with open(args[0], 'wt') as w_file:
            w_file.write(text)
        return f'Replaced {count} strings'


class ParserTest(unittest.TestCase):
    mock_file_content = """
        some string to be tested
        """

    def test_found(self):
        with unittest.mock.patch(
                'builtins.open',
                new=unittest.mock.mock_open(read_data=self.mock_file_content),
                create=True
        ) as file_mock:
            expected = 'Found 3 strings'
            actual = file_parser('/dev/null', 's')
            self.assertEqual(actual, expected)

    @unittest.mock.patch(
        'builtins.open',
        new=unittest.mock.mock_open(read_data=mock_file_content),
        create=True
    )
    def test_replace(self):
        expected = 'Replaced 3 strings'
        actual = file_parser('/dev/null', 's', 'S')
        self.assertEqual(actual, expected)

