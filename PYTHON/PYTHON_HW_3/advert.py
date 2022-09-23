import keyword


class ColorizeMixin:

    def __str__(self):

        str_to_colorize = super().__str__()
        return f'\033[1;{self.repr_code_color}m {str_to_colorize}'


class JsonParser:

    def __init__(self, mapping):

        for key, value in mapping.items():

            new_attr_name = None
            new_attr_value = None

            if keyword.iskeyword(key):
                new_attr_name = key + '_'
            else:
                new_attr_name = key

            if self.__check_attr_value(value):
                new_attr_value = value
            else:
                new_attr_value = JsonParser(value)

            setattr(self, new_attr_name, new_attr_value)

    # check if attr_value is dict of strings - if so we create nested object
    def __check_attr_value(self, attr_value):
        is_simple_value = False

        if type(attr_value) == dict:

            for key in attr_value.keys():

                if type(key) != str:
                    is_simple_value = True
                    break
        else:
            is_simple_value = True

        return is_simple_value


class Advert(ColorizeMixin):

    repr_code_color = 1  # default color code - white

    def __init__(self, data):

        parsed_json = JsonParser(data)

        if 'title' not in parsed_json.__dict__.keys():
            raise AttributeError("There is no title in advert")

        if parsed_json.price < 0:
            raise ValueError('Price must be non negative.')

        for attribute_key in parsed_json.__dict__.keys():

            self.__dict__[attribute_key] = parsed_json.__dict__[attribute_key]

    def __setattr__(self, key, value):

        if key == 'price' and value < 0:
            raise ValueError("Price must be non negative.")

        if key == 'repr_code_color':
            super().__setattr__('repr_code_color', value)

    def __repr__(self):

        return f'{self.title} | {self.price} \u20bd'
