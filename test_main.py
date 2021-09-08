from main import Operations

input_file = "abc.txt"

with open(input_file, mode='r', encoding='UTF-8') as f:
    r = Operations(f)


    def test_palindrome():
        assert r.palindrome_fn("rotator") == True
        assert r.palindrome_fn("baby") == False


    def test_end_ing_fn():
        assert r.end_ing_fn("making") == True
        assert r.end_ing_fn("make") == False


    def test_prefix_to_fn():
        assert r.prefix_to_fn("tomorrow") == True
        assert r.prefix_to_fn("failure") == False


    def test_split_vowels():
        assert r.split_vowels_fn("vowels") == ['v', 'w', 'ls']


    def test_cap_third_fn():
        assert r.cap_third_fn("hello") == 'heLlo'

    # def test_get_content():
    #     assert r.get_content() == True
