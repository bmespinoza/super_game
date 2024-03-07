from game import Game
from mailing import create_html_email, send_simple_message

if __name__ == "__main__":
    game = Game()
    first_team_name = input("Enter a name for the first team: ")
    second_team_name = input("Enter a name for the second team: ")
    game.prepare_game(first_team_name, second_team_name)
    game.start_game()
    html_email = create_html_email(game.summary)
    email_address = input("Enter your email to receive a summary of the game: ")
    if email_address:
        send_simple_message(email_address, html_email)
    else:
        print("The end")
