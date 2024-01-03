import hashlib
import base64
import random
import time
import curses

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def xor_decrypt(data, key):
    return bytes([b ^ ord(key[i % len(key)]) for i, b in enumerate(data)])

def matrix_rain(window):
    sh, sw = window.getmaxyx()
    window.nodelay(True)
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    letters = list('ﾊﾐﾋｰｳｼﾅﾓﾆｻﾜﾂｵﾘｱﾎﾃﾏｹﾒｴｶｷﾑﾕﾗｾﾈｽﾀﾇﾍ012345789ZTHEMATRIX:・."=*+-<>¦｜╌日ｦｲｸｺｿﾁﾄﾉﾌﾔﾖﾙﾚﾛﾝçﾘZABCDEFGHIJKLMNOPQRSTUVXYZABCDEFGHIJKLMNOPQRSTUVXYZ')
    max_length = 10
    column_chars = [random.choice(letters) for _ in range(sw)]
    drops = [0] * sw

    while True:
        window.clear()

        for i in range(sw):
            if drops[i] < 0:
                drops[i] += 1
            else:
                if random.random() > 0.95:
                    drops[i] = -max_length

                if 0 <= drops[i] < sh - 1:  # Change sh to sh - 1
                    window.addch(drops[i], i, column_chars[i], curses.color_pair(2))
                for j in range(1, min(drops[i], max_length)):
                    if 0 <= drops[i] - j < sh - 1:  # Change sh to sh - 1
                        window.addch(drops[i] - j, i, column_chars[i], curses.color_pair(1))

                column_chars[i] = random.choice(letters)
                drops[i] += 1

        window.refresh()
        time.sleep(0.05)

        if window.getch() != -1:
            break

def main():
    # Riddle
    print("Solve the following riddle to continue (you can put your own custom riddle here):")
    riddle = ("In a field where giants fight,\n"
              "A boy, without sword or shield.\n"
              "With only a sling and some courage,\n"
              "Who defeated the giant, as the story reveals?")
    answer_hash = hash_password(input(f"{riddle}\nYour answer: ").upper())

    # Hashed answer for the riddle
    hashed_answer_riddle = 'ZTBkMWVmZDMxOTk2MjQ0MjM1OGY1ZjAzNDk1ZjE4Mzc='

    if answer_hash != base64.b64decode(hashed_answer_riddle).decode():
        print("Wrong answer, try again!")
        curses.wrapper(matrix_rain)
        return

    # Encoded hash for the password
    encoded_hash = 'Nzg2Y2ViNmRkNmY1MTdjMzljZWM2YTRhYjMzNzBmZjc='
    hidden_password_hash = base64.b64decode(encoded_hash).decode()

    # Base64 lalalalaaaaaa
    base64_encrypted_link = 'put your base 64 XOR encrypted Google drive link here, I used an image of a white rabbit with custom EXIF data with a second Google drive link in there to my CV'
    xor_encrypted_link_bytes = base64.b64decode(base64_encrypted_link)
    key = 'rabbit'

    user_input = input("Enter the password & follow the white rabbit: ")

    if hash_password(user_input) == hidden_password_hash:
        print("Correct! All you now need to do is, Follow the white rabbit:")
        decrypted_link_bytes = xor_decrypt(xor_encrypted_link_bytes, key)
        decrypted_link = decrypted_link_bytes.decode('latin1')
        print(decrypted_link)
    else:
        print("Incorrect password, try again! Tip: PUT YOUR TIP TO SOLVE PW HERE")
        curses.wrapper(matrix_rain)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

