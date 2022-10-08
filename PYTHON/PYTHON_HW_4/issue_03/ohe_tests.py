from one_hot_encoder import fit_transform
import unittest


class TestOneHotEncoder(unittest.TestCase):
    def test_fit_transform(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_fit_transform_with_one_arg(self):
        cities = 'Moscow'
        exp_transformed_cities = [('Moscow', [1])]
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_fit_transform_with_equal_arg(self):
        cities = ['Moscow', 'Moscow']
        exp_transformed_cities = [
            ('Moscow', [1]),
            ('Moscow', [1]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_fit_transform_with_empty_arg(self):
        cities = ['']
        exp_transformed_cities = [('', [1])]
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_with_wrong_arg_type(self):
        with self.assertRaises(TypeError):
            fit_transform(1)

    def test_check_output_type(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        transformed_cities = fit_transform(cities)
        self.assertIsInstance(transformed_cities, list)


if __name__ == '__main__':
    unittest.main()
