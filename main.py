#############################################################################
# 				      Documentation	- Double DES                            #
#############################################################################

# Author:       Muhammad Sadaqat Janjua [1]
# Co-Author:    Waseem Ahmad [2]
# Date:         December 30, 2021
# Version:      1.0.0
# License:      Public Domain - free to do as you wish
# Email(s):     [1] mjanjua@asu.edu [2] waseem.ahmad@uos.edu.pk
#
# This is a pure python implementation of the Double DES encryption algorithm.
# It is pure python to avoid cross-platform issues, since most 2-DES implementations
# are programmed in C (for optimization reasons).
#
# Requirements:
# Latest version of Python (only)
# Thanks to:
#  * Assistant Professor Dr. Khalid Mahmood for ideas, comments and suggestions.
#  * Waseem Ahmad for providing the optimization technique.

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


ascii_plaintext = input("Enter Plaintext?")
plaintext = []
for character in ascii_plaintext:
    plaintext.append(bin(ord(character))[2:].zfill(8))
# ---------------------- #
# adding_padding_shading #
# ---------------------- #
padding_flag = len(plaintext)
while (padding_flag % 8) > 0:
    plaintext.append(bin(0)[2:].zfill(8))
    padding_flag = padding_flag + 1
left = plaintext[:4]
right = plaintext[4:8]
print(f'Plain Text Block is: {plaintext}')
print(f'Left is: {left}')
print(f'Right is: {right}')
# -------------------- #
#    Key-Schedule      #
# -------------------- #
ascii_key_1 = input("Enter First Secret key (Must be 8-Characters):")
ascii_key_2 = input("Enter Second Secret key (Must be 8-Characters):")
np_key_1 = []
np_key_2 = []
for characters in ascii_key_1:
    np_key_1.append(bin(ord(characters))[2:])
for characters in ascii_key_2:
    np_key_2.append(bin(ord(characters))[2:])

print(f'First Key without Parity Bit: {np_key_1}')
print(f'Second Key without Parity Bit: {np_key_2}')

parity_1 =[]
parity_2 =[]
for values in np_key_1:
    parity_1.append((int(values[:1]) + int(values[1:2]) + int(values[2:3]) + int(values[3:4]) + int(values[4:5]) + int(values[5:6]) + int(values[6:])) % 2)
print(f'Parity Bit list: {parity_1}')
parity_str_1 = str(parity_1)
for values in np_key_2:
    parity_2.append((int(values[:1]) + int(values[1:2]) + int(values[2:3]) + int(values[3:4]) + int(values[4:5]) + int(values[5:6]) + int(values[6:])) % 2)
print(f'Parity Bit list: {parity_2}')
parity_str_2 = str(parity_2)

p_key_1 = []
p_key_2 = []
i_1 = 0
i_2 = 0
j_1 = 1
j_2 = 1

while (i_1 < 8) & (j_1 < 23):
    p_key_1.append((np_key_1[i_1] + parity_str_1[j_1]))
    i_1 += 1
    j_1 += 3
print(f'First Key with Parity Bit: {p_key_1}')

while (i_2 < 8) & (j_2 < 23):
    p_key_2.append((np_key_2[i_2] + parity_str_2[j_2]))
    i_2 += 1
    j_2 += 3
print(f'Second Key with Parity Bit: {p_key_2}')
# |NOTE|-- Up till now we just added the Parity Bits in the input key --|NOTE|

# --- Key Permutation 1--- #
kp_1_table = [56, 48, 40, 32, 24, 16, 8,
              0, 57, 49, 41, 33, 25, 17,
              9, 1, 58, 50, 42, 34, 26,
              18, 10, 2, 59, 51, 43, 35,
              62, 54, 46, 38, 30, 22, 14,
              6, 61, 53, 45, 37, 29, 21,
              13, 5, 60, 52, 44, 36, 28,
              20, 12, 4, 27, 19, 11, 3
              ]
single_key_1 = ""
single_key_2 = ""

for m in p_key_1:
    single_key_1 += m
print(f'String Format Value of Key-1: {single_key_1}')
for n in p_key_2:
    single_key_2 += n
print(f'String Format Value of Key-2: {single_key_2}')

single_perm_bit_1 = []
single_perm_bit_2 = []

for item_k_1 in kp_1_table:
    single_perm_bit_1 += single_key_1[item_k_1]
single_perm_key_1 = ""
for iter_k_1 in single_perm_bit_1:
    single_perm_key_1 += iter_k_1
print(f'Key-1 Permuted Sequence: {single_perm_key_1}')

for item_k_2 in kp_1_table:
    single_perm_bit_2 += single_key_2[item_k_2]
single_perm_key_2 = ""
for iter_k_2 in single_perm_bit_2:
    single_perm_key_2 += iter_k_2
print(f'Key-2 Permuted Sequence: {single_perm_key_2}')

# |NOTE|-- Up till Key Permutation-1 is Done! --|NOTE|
up_perm_key_k1 = single_perm_key_1[:28]
dn_perm_key_k1 = single_perm_key_1[28:]

up_perm_key_k2 = single_perm_key_2[:28]
dn_perm_key_k2 = single_perm_key_2[28:]
# Split down in to two halves
print(f'KEY_1 UP Output of Key Permutation-1 (keyUP): {up_perm_key_k1}')
print(f'KEY_1 DN Output of Key Permutation-1 (keyDN): {dn_perm_key_k1}')

print(f'KEY_2 UP Output of Key Permutation-1 (keyUP): {up_perm_key_k2}')
print(f'KEY_2 DN Output of Key Permutation-1 (keyDN): {dn_perm_key_k2}')
sec_permutation_keys_1 = []
sec_permutation_keys_2 = []
# For R1,R2,R9,R16 we left shift by 1-bit both halves of Permuted 8-Bytes
# For R3,R4,R5,R6,R7,R8,R10,R11,R12,R13,R14,R15 we left shift by 2-bit both halves of Permuted 8-Bytes
ctrlRound_K1 = 1
ctrlRound_K2 = 1
oneLS = 1
twoLS = 2



def CalcRoundsLS_K1(keyUP, keyDN, ctrlRound1, upInd, dnInd):
    if ctrlRound1 == 1 or ctrlRound1 == 2 or ctrlRound1 == 9 or ctrlRound1 == 16:
        sec_permutation_keys_1.append(keyUP[oneLS:] + keyUP[:oneLS])
        sec_permutation_keys_1.append(keyDN[oneLS:] + keyDN[:oneLS])
    else:
        sec_permutation_keys_1.append(keyUP[twoLS:] + keyUP[:twoLS])
        sec_permutation_keys_1.append(keyDN[twoLS:] + keyDN[:twoLS])
    ctrlRound1 += 1
    if ctrlRound1 < 17:
        CalcRoundsLS_K1(sec_permutation_keys_1[len(sec_permutation_keys_1)-2], sec_permutation_keys_1[len(sec_permutation_keys_1)-1], ctrlRound1, upInd + 2, dnInd + 2)


def CalcRoundsLS_K2(keyUP, keyDN, ctrlRound2, upInd, dnInd):
    if ctrlRound2 == 1 or ctrlRound2 == 2 or ctrlRound2 == 9 or ctrlRound2 == 16:
        sec_permutation_keys_2.append(keyUP[oneLS:] + keyUP[:oneLS])
        sec_permutation_keys_2.append(keyDN[oneLS:] + keyDN[:oneLS])
    else:
        sec_permutation_keys_2.append(keyUP[twoLS:] + keyUP[:twoLS])
        sec_permutation_keys_2.append(keyDN[twoLS:] + keyDN[:twoLS])
    ctrlRound2 += 1
    if ctrlRound2 < 17:
        CalcRoundsLS_K2(sec_permutation_keys_2[len(sec_permutation_keys_2)-2], sec_permutation_keys_2[len(sec_permutation_keys_2)-1], ctrlRound2, upInd + 2, dnInd + 2)

CalcRoundsLS_K1(up_perm_key_k1, dn_perm_key_k1, ctrlRound_K1, 0, 1)
CalcRoundsLS_K2(up_perm_key_k2, dn_perm_key_k2, ctrlRound_K2, 0, 1)


round_permutations_k1 = []
round_permutations_k2 = []


def keyperm(key,keysec):
    x = 0
    y = 1
    while y < 17:
        print(f'Permuted Key for Round {y} is: {keysec[x]+keysec[x+1]}')
        key.append(keysec[x]+keysec[x+1])
        y += 1
        x += 2
    print(f'Round Permutation Array: {key}')

print(f'_______________KEY-1__________________')
keyperm(round_permutations_k1,sec_permutation_keys_1)
print(f'______________________________________')
print(f'_______________KEY-2__________________')
keyperm(round_permutations_k2,sec_permutation_keys_2)
print(f'______________________________________')

# -------------------- #
#  Key-Permutation 2   #
# -------------------- #
kp_2_table = [13, 16, 10, 23, 0, 4, 2, 27,
              14, 5, 20, 9, 22, 18, 11, 3,
              25, 7, 15, 6, 26, 19, 12, 1,
              40, 51, 30, 36, 46, 54, 29, 39,
              50, 44, 32, 47, 43, 48, 38, 55,
              33, 52, 45, 41, 49, 35, 28, 31
              ]

second_perm_keys_K1 = ''
second_perm_keys_K2 = ''
_roundkey_arr_K1 = []
_roundkey_arr_K2 = []

def secondperm(key,roundstore, roundperm):
    for b in range(16):
        for a in kp_2_table:
            key += roundperm[b][a]
    print(f'Round Keys Sequence: {key}')
    u = 0
    q = 1
    while q < 17:
        roundstore.append(key[48 * u:48 * q])
        u += 1
        q += 1
    print(f'Round Keys are: {roundstore}')


print(f'_______________KEY-1__________________')
secondperm(second_perm_keys_K1,_roundkey_arr_K1,round_permutations_k1)
print(f'______________________________________')
print(f'_______________KEY-2__________________')
secondperm(second_perm_keys_K2,_roundkey_arr_K2, round_permutations_k2)
print(f'______________________________________')
# ---------- S-BOXES ---------- #
__sbox = [
    # S1
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    # S2
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    # S3
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    # S4
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    # S5
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    # S6
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    # S7
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    # S8
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]],
]
# -------------- P-Box --------------- #
__p = [
        15, 6, 19, 20, 28, 11, 27, 16,
        0, 14, 22, 25, 4, 17, 30, 9,
        1, 7, 23, 13, 31, 26, 2, 8,
        18, 12, 29, 5, 21, 10, 3, 24
        ]

def feistelfunc(right, roundkey, rkref):
    print(f'{bcolors.WARNING}Right BEFORE Feistel Function in Round key{roundkey.index(roundkey[d_counter]) + 1} is: {right}')
    print(f'Left BEFORE Feistel Function in Round key{roundkey.index(roundkey[d_counter]) + 1} is: {left}')
    string_right = ''
    for ind in range(4):
        string_right += right[ind]
    expanded_right = string_right[-1:]+string_right[:5]+string_right[3:9]+string_right[7:13]+string_right[11:17]+string_right[15:21]+string_right[19:25]+string_right[23:29]+string_right[27:32]+string_right[:1]
    print(f'{bcolors.ENDC}Expanded Right (48-Bits) is: {expanded_right}')
    # Calculating XOR!
    num3 = int(roundkey, 2) ^ int(expanded_right, 2)
    xor_result = bin(num3)[2:].zfill(48)
    print(f'XOR of Right with Round Key: {xor_result}')
    partiotioned_xor_data =[]
    _u = 0
    _q = 1
    while _q < 9:
        partiotioned_xor_data.append(xor_result[6 * _u:6 * _q])
        _u += 1
        _q += 1
    print(partiotioned_xor_data)

    s1_row = int(partiotioned_xor_data[0][:1]+partiotioned_xor_data[0][-1:], 2)
    s2_row = int(partiotioned_xor_data[1][:1]+partiotioned_xor_data[1][-1:], 2)
    s3_row = int(partiotioned_xor_data[2][:1]+partiotioned_xor_data[2][-1:], 2)
    s4_row = int(partiotioned_xor_data[3][:1]+partiotioned_xor_data[3][-1:], 2)
    s5_row = int(partiotioned_xor_data[4][:1]+partiotioned_xor_data[4][-1:], 2)
    s6_row = int(partiotioned_xor_data[5][:1]+partiotioned_xor_data[5][-1:], 2)
    s7_row = int(partiotioned_xor_data[6][:1]+partiotioned_xor_data[6][-1:], 2)
    s8_row = int(partiotioned_xor_data[7][:1]+partiotioned_xor_data[7][-1:], 2)
    s1_col = int(partiotioned_xor_data[0][1:5], 2)
    s2_col = int(partiotioned_xor_data[1][1:5], 2)
    s3_col = int(partiotioned_xor_data[2][1:5], 2)
    s4_col = int(partiotioned_xor_data[3][1:5], 2)
    s5_col = int(partiotioned_xor_data[4][1:5], 2)
    s6_col = int(partiotioned_xor_data[5][1:5], 2)
    s7_col = int(partiotioned_xor_data[6][1:5], 2)
    s8_col = int(partiotioned_xor_data[7][1:5], 2)
    substituted_bits = []

    substituted_bits.append(bin(__sbox[0][s1_row][s1_col])[2:].zfill(4))
    substituted_bits.append(bin(__sbox[1][s2_row][s2_col])[2:].zfill(4))
    substituted_bits.append(bin(__sbox[2][s3_row][s3_col])[2:].zfill(4))
    substituted_bits.append(bin(__sbox[3][s4_row][s4_col])[2:].zfill(4))
    substituted_bits.append(bin(__sbox[4][s5_row][s5_col])[2:].zfill(4))
    substituted_bits.append(bin(__sbox[5][s6_row][s6_col])[2:].zfill(4))
    substituted_bits.append(bin(__sbox[6][s7_row][s7_col])[2:].zfill(4))
    substituted_bits.append(bin(__sbox[7][s8_row][s8_col])[2:].zfill(4))

    print(f'Substituted Bytes 8-S Boxes (48->32): {substituted_bits}')
    string_sub_bits = ''
    for __ind in range(8):
        string_sub_bits += substituted_bits[__ind]
    print(f'Substituted Bytes String: {string_sub_bits} ')

    # P-Box Permutation:
    __out_pbox =''
    for _indices in __p:
        __out_pbox += string_sub_bits[_indices]
    print(f'Output of Feistel Function for Round key {rkref.index(rkref[0]) + 1} is: {__out_pbox}')
    _output_bin_ff = bin(int(__out_pbox, 2))[2:].zfill(32)
    print(f'{bcolors.OKBLUE}Right AFTER Feistel Function in Round key{roundkey.index(roundkey[d_counter]) + 1} is: {right}')
    print(f'Left AFTER Feistel Function in Round key{roundkey.index(roundkey[d_counter]) + 1} is: {left}')

    return _output_bin_ff


counter = 0


def encrypt(lf, ri, __roundkey):
    string_left = ''
    for ind in range(4):
        string_left += lf[ind]
    temp_ri = ri
    global counter
    global right, left

    tempo1 = int(string_left, 2)
    tempo2 = int(feistelfunc(ri, __roundkey[counter],__roundkey), 2)
    right_str = bin(tempo1 ^ tempo2)[2:].zfill(32)
    right_list = []
    _e = 0
    _r = 1
    while _r < 5:
        right_list.append(right_str[8 * _e:8 * _r])
        _e += 1
        _r += 1
    right = right_list
    left = temp_ri

    counter += 1
    if counter < 16:
        encrypt(left,right,__roundkey)
    else:
        temp = left
        left = right
        right = temp
        counter = 0     # Reset Counter to make this function work for rest of calls


# Decrypt::::
d_counter = 15   # Counter Set


def decrypt(d_lf, d_ri, __d_roundkey):
    d_string_left = ''
    for d_ind in range(4):
        d_string_left += d_lf[d_ind]
    d_temp_ri = d_ri
    global d_counter
    global right, left

    d_tempo1 = int(d_string_left, 2)
    d_tempo2 = int(feistelfunc(d_ri, __d_roundkey[d_counter], __d_roundkey), 2)
    d_right_str = bin(d_tempo1 ^ d_tempo2)[2:].zfill(32)
    d_right_list = []
    d_e = 0
    d_r = 1
    while d_r < 5:
        d_right_list.append(d_right_str[8 * d_e:8 * d_r])
        d_e += 1
        d_r += 1
    right = d_right_list
    left = d_temp_ri

    d_counter -= 1
    if d_counter >-1:
        decrypt(left,right,__d_roundkey)
    else:
        temp = left
        left = right
        right = temp
        d_counter = 15      # Reset Counter to make this function work for rest of calls

# Encrypting with K1
encrypt(left, right, _roundkey_arr_K1)

par_ciphertext = left + right
print(f'{bcolors.OKGREEN}Partially Ciphered Text in Bits is: {par_ciphertext}')
st_par_cipher = ''
_binary_par = []
for _bytes in range(8):
    _binary_par.append(int(par_ciphertext[_bytes], 2))
    st_par_cipher += chr(_binary_par[_bytes])

print(f'Partially Ciphered Text in ASCII Characters is:{st_par_cipher}')
print(f'{bcolors.OKCYAN}Left at the end of Partial Encryption is:{left}')
print(f'Right at the end of Partial Encryption is:{right}')

# Encrypting with K2
encrypt(left, right, _roundkey_arr_K2)
ciphertext = left + right
print(f'{bcolors.OKGREEN}Cipher Text in Bits is: {ciphertext}')
st_cipher = ''
_binary = []
for _bytes_f in range(8):
    _binary.append(int(ciphertext[_bytes_f], 2))
    st_cipher += chr(_binary[_bytes_f])

print(f'Cipher Text in ASCII Characters is:{st_cipher}')

print(f'{bcolors.OKCYAN}Left at the end of Encryption is:{left}')
print(f'Right at the end of Decryption is:{right}')

print(f'{bcolors.BOLD}___________________________DECRYPTION PHASE______________________________')
# Decryption with K2
decrypt(left, right, _roundkey_arr_K2)  # calling decrypt method for cipher text!!!

p_d_plantext = left + right
print(f'{bcolors.OKGREEN}Partial Plain Text (by Key-2) in Bits is: {p_d_plantext}')
pd_st_plain = ''
pd_binary = []
for pd_bytes in range(8):
    pd_binary.append(int(p_d_plantext[pd_bytes], 2))
    pd_st_plain += chr(pd_binary[pd_bytes])

print(f'Partial Plain Text (by Key-2) in ASCII Characters is:{pd_st_plain}')
print(f'{bcolors.OKCYAN}Left at the end of Dec is:{left}')
print(f'Right at the end of Dec is:{right}')

# Decryption with K1
decrypt(left,right,_roundkey_arr_K1)

f_d_plantext = left + right
print(f'{bcolors.OKGREEN}Required Plaintext in Bits is: {f_d_plantext}')
fd_st_plain = ''
fd_binary = []
for fd_bytes in range(8):
    fd_binary.append(int(f_d_plantext[fd_bytes], 2))
    fd_st_plain += chr(fd_binary[fd_bytes])

print(f'Required Plaintext in ASCII Characters is:{fd_st_plain}')
print(f'{bcolors.OKCYAN}Left at the end of Whole Decryption is:{left}')
print(f'Right at the end of whole Decryption is:{right}')