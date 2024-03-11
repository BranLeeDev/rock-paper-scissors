import modules.user_interface as user_interface

def main():
    while True:
        user_interface.play_game()
        if not user_interface.play_again():
            break

if __name__ == "__main__":
    main()