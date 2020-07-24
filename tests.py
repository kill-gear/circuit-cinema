from hypothesis import given, strategies as st
from screen_reader import encode_rgb, parse_inp
import unittest

rgb_val = st.integers(min_value=0, max_value=255)
frames = st.lists(st.tuples(rgb_val, rgb_val, rgb_val), min_size=0)
class TestAdd(unittest.TestCase):

    @given(frames)
    def test_encode_decode(self, frame):
        encoded = encode_rgb(frame)
        decoded = parse_inp(encoded)
        self.assertEqual(decoded, frame) 
