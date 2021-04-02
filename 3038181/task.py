EPSILON = 0.001


class Vector:
    """Class defining vectors from algebra

    The Vector class is a mathematical representation of a list of numbers
    as a vector with corresponding coordinates.
    Implements operators for comparing vectors to each other.
    """

    def __init__(self, v):
        """Constructor for the Vector class

        The constructor accepts an iterable of numbers as input.

        Args:
            v (:obj:`list` of :obj:`tuple`): List of numbers
                representing the coordinates of a vector.

        """
        self.check_input(v)
        self.v = v

    @staticmethod
    def check_input(v):
        """Class method that checks if the correct data type is passed to the constructor

        Args:
            v: Object passed to constructor.

        Raises:
            TypeError: If the 'v' is not an object of the class list or tuple

        """
        if type(v) != list and type(v) != tuple:
            print(1)
            raise TypeError('expected Any[Tuple[Any[float, int]], List[Tuple[Any[float, int]]].')

        if any(type(item) != float and type(item) != int for item in v):
            print(2)
            raise TypeError('expected Any[Tuple[Any[float, int]], List[Tuple[Any[float, int]]].')

    def length(self) -> float:
        """Length of vector

        The length of a vector is calculated as
        the square root of the sum of the squares of its coordinates


        Returns:
            float: length of vector

        """
        return sum(elem ** 2 for elem in self.v) ** 0.5

    def check_length(self, other):
        """Class method that checks if two vectors can be compared with each other

        Args:
            other: The vector to compare with.

        Raises:
            ValueError: If the vectors differ in the number of coordinates

        """
        if len(self.v) != len(other.v):
            raise ValueError('vectors shape mismatch.')

    def __eq__(self, other) -> bool:
        """Class method that checks if two vectors is equal by length

        Args:
            other: The vector to compare with.

        Returns:
            bool: True on vectors is equal, False otherwise.

        """
        self.check_length(other)
        return abs(self.length() - other.length()) <= EPSILON

    def __lt__(self, other) -> bool:
        """Class method that checks that the current vector is less than the other

        Args:
            other: The vector to compare with.

        Returns:
            bool: True on success, False otherwise.

        """
        self.check_length(other)
        return other.length() - self.length() >= EPSILON

    def __le__(self, other) -> bool:
        """Class method that checks that the current vector is less than the other or equal

        Args:
            other: The vector to compare with.

        Returns:
            bool: True on success, False otherwise.

        """
        self.check_length(other)
        return self < other or self == other

    def __gt__(self, other) -> bool:
        """Class method that checks that the current vector is greater than the other

        Args:
            other: The vector to compare with.

        Returns:
            bool: True on success, False otherwise.

        """
        self.check_length(other)
        return not (self < other)

    def __ge__(self, other) -> bool:
        """Class method that checks that the current vector is greater than the other or equal

        Args:
            other: The vector to compare with.

        Returns:
            bool: True on success, False otherwise.

        """
        self.check_length(other)
        return not (self < other) or self == other