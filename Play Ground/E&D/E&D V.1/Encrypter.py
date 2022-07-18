KEY = "6974486187003869668097048"

encrypt_code = "POlgOKhVDp"

length_of_key = len(KEY)

encrypted_word = ""

if length_of_key == 25:
    key_count = 0
    word = input("Word You Want To Encrypt: ")
    letter_count = len(word)
    for i in range(letter_count):
        key_index_shuffle = KEY[key_count]
        encrypt_code_index_shuffle = encrypt_code[int(key_index_shuffle)]
        key_count += 1
        encrypted_word += encrypt_code_index_shuffle
    print(encrypted_word)


else:
    print("Invalid key")