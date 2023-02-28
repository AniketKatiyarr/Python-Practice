from Script import pick_random_word
#print(pick_random_word())

def print_current_state(current_word_state,attempts_remaining):


 def play_game(attempt=5):
    selected_word = pick_random_word()
    
    current_word_state = ""
    for i in selected_word:
        if i ==' ' or i =='a' or i=='o'or i=='i'or i=='e' or i=='u':
           current_word +=i
        else:
            current_word_state += "_"
    attempts_remaining = attempts
    print_current_state()
    
if __name__ == "__main__":
    play_game()
    