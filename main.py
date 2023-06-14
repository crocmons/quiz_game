def main():
    print("Welcome to my quiz game")
    
    play = input('Do you want to play this game? say yes or no: ')
    
    if play.lower() != 'yes':
       return
   
    print("Let's Play the game!")
    score = 0
    
    answer = input('What country has the highest life expectancy? ')
    if answer.lower() == 'hong kong':
        print('Correct Answer')
        score +=1
    else:
        print('Incorrect answer','it should be Hong Kong')
    
    answer = input('What is the most common surname in the United States? ')
    if answer.lower() == 'smith':
        print('Correct Answer')
        score +=1
    else:
        print('Incorrect answer','it should be Smith')
    
    answer = input('What company was originally called "Cadabra"? ')
    if answer.lower() == 'amazon':
        print('Correct Answer')
        score +=1
    else:
        print('Incorrect answer','it should be Amazon')  
    
    answer = input('What character have both Robert Downey Jr. and Benedict Cumberbatch played? ')
    if answer.lower() == 'sherlock holmes':
        print('Correct Answer')
        score +=1
    else:
        print('Incorrect answer','it should be Sherlock Holmes')  
        
    answer = input('What company was initially known as "Blue Ribbon Sports"? ')
    if answer.lower() == 'nike':
        print('Correct Answer')
        score +=1
    else:
        print('Incorrect answer','it should be Nike')      
        
    
    print('Your Score is ' + str(score) + '.')    
    print('You got ' + str((score / 5) * 100) + '% out of 100%' )

if __name__ == "__main__":
    main()
