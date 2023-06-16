import random

def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input("piedra, papel o tijera -> ")
  user_option = user_option.lower()
  if not user_option in options:
    print('Esa opcion no es valida')
    return None, None
  computer_option = random.choice(options)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('empate')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print("piedra gana a tijera")
      print("el usuario gano")
      user_wins += 1
    else:
      print("papel gana a piedra")
      print("computer gano")
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('gano usuario')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computer wins')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print("Tijera gana a papel")
      print('El usuario gano')
      user_wins += 1
    else:
      print("Piedra gana a tijera")
      print("El computador gano")
      computer_wins += 1

  return user_wins, computer_wins

def check_winner(user_wins, computer_wins):
  winner = None, False
  if computer_wins == 2:
    winner = "El ganador es la computadora", True

  if user_wins == 2:
    winner = "El ganador es el usuario", True

  return winner

def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1
  while True:

    print('*' * 100)
    print(f'ROUNDS {rounds}')
    print('*' * 100)

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    message, winner = check_winner(user_wins, computer_wins)
    if winner:
      print(message)
      break

    print(f'computer_wins => {computer_wins}')
    print(f'user_wins => {user_wins}')
    rounds += 1

run_game()
