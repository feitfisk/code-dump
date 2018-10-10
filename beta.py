import click
import random

def beta_convert(b, n):
    """Returns given n in b number system"""
    if b is 2:
        return bin(n)
    elif b is 8:
        return oct(n)
    elif b is 16:
        return hex(n)
    return n


@click.command()
def from_to():
    """Generates a random number in two different
    number systems and quizzes the user about the 
    conversion between those two. 
    """
    betas = [2, 8, 10, 16]
    beta = random.choice(betas)
    beta_2 = random.choice(betas)

    rand = random.randint(1, 500)

    while beta == beta_2:
        beta_2 = random.choice(betas)

    a = beta_convert(beta, rand)
    b = beta_convert(beta_2, rand)

    print (f"Convert {a} base {beta} to base {beta_2}")

    answer = click.prompt("Answer")

    if answer == b:
        print("Correct!")
    else:
        print(f"You answered {answer}, the correct answer is {b}")


if __name__ == '__main__':
    from_to()

