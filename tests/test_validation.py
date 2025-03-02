from functions.user_validation import validate_numeric
from functions.user_validation import validate_coordinates

def run_tests():
    print("Testing validate_numeric:")
    print(validate_numeric("350", allow_decimal=False))  
    print(validate_numeric("3.5", allow_decimal=True))   
    print(validate_numeric("-10", allow_decimal=False))  
    print(validate_numeric("abc", allow_decimal=False))  
    print(validate_numeric("10.5", allow_decimal=False)) 

    print("\nTesting validate_coordinates:")
    print(validate_coordinates("53.5511,9.9937"))  
    print(validate_coordinates("-45.123,179.999"))  
    print(validate_coordinates("0,0"))  
    print(validate_coordinates("53.5511;9.9937")) 
    print(validate_coordinates("abc,9.9937"))  
    print(validate_coordinates("53.5511,abc")) 
    print(validate_coordinates("100,50"))

if __name__ == "__main__":
    run_tests()
