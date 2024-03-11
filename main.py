import modules.user_interface as user_interface

def main():
    try:
        while True:
            user_interface.play_game()
            if not user_interface.play_again():
                break
    except KeyboardInterrupt:
        print('\nGame interrupted. Exiting...')
        exit()
        

if __name__ == "__main__":
    main()