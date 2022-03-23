from encodedecode import encode_text
from encodedecode import decode_text
from error_detection_and_correction import error_detection
from error_detection_and_correction import error_correction
encoding = encode_text("HELLO WORLD")
encoding[0][1] = 0
encoding[1][1] = 0
encoding[2][3] = 1
detected = error_detection(encoding)
print(detected)
corrected = error_correction(encoding, detected)
print(corrected)
decoded = decode_text(corrected)
print(decoded)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
