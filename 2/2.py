

def is_valid_product(productId: str) -> bool:
    # you can find the invalid IDs by looking for any ID which is made only of some sequence of digits 
    # repeated twice. 
    # So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.
    # 
    firstHalf = productId[:len(productId)//2]
    secondHalf = productId[len(productId)//2:]

    return False if firstHalf == secondHalf else True



def is_valid_product_v2(productId: str) -> bool:
    # Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. 
    # So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times),
    #  and 1111111 (1 seven times) are all invalid IDs.

    # odd
    # 99999 invalid
    # 90909 valid
    # 12312 valid
    # 123123123 invalid
    # even
    # 11 invalid
    # 1212 invalid
    # 121212 invalid
    # 123123 invalid

    left = 0
    right = 0
    mid = len(productId) // 2
    while right < mid:
        # test a substring of chars
        segment = productId[left:right + 1]
        # build what we think it should look like
        expectedString = segment * (len(productId) // len(segment))
        if expectedString == productId:
            return False
        right += 1

    return True



def run_part1():
    with open('input.txt') as f:
        data = f.readline().strip()
        ranges = data.split(',')
        invalid_ranges = []
        for r in ranges:
            start, end = r.split('-')
            for productId in range(int(start), int(end) + 1):
                if not is_valid_product_v2(str(productId)):
                    invalid_ranges.append(productId)
        
        sum_of_invalids = sum(invalid_ranges)
        print(f"Sum of invalid product IDs: {sum_of_invalids}")
                


if __name__ == "__main__":
    run_part1()


    # 1227775554 too low