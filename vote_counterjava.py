def get_votes():
    votes = input("Enter votes for A and B ").strip().upper()
    votes_A = votes.count('A')
    votes_B = votes.count('B')
    return votes_A, votes_B


def main():
    print("Welcome to the voting system!")
    votes_A, votes_B = get_votes()
    
    print("\nVoting Result:")
    print("A Recieved", votes_A, "Votes.")
    print("B Recieved", votes_B, "Votes.")
    
    if votes_A == votes_B:
        print("It's a tie!")
    elif votes_A > votes_B:
        print("A Won!")
    else:
        print("B won!")
        
        
main()