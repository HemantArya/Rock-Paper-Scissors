# Rock-Paper-Scissors
Description

How about some brand new rules? The original game has a fairly small choice of options.

Extended versions of the game are decreasing the probability of draw, so it could be cool to play them.
This program can accept an alternative lists of options, like Rock, Paper, Scissors, Lizard, Spock, or even a list like this:

 

At this stage, before the start of the game the user will be able to choose the options that will be used. After entering his/her name, the user should provide a list of options separated by comma. For example, 

rock,paper,scissors,lizard,spock

If the user inputs an empty line, program will start the game with default options: rock. paper and scissors. 

Whatever list of options the user chooses, program will identify which option beats which, that is, the relationships between different options. First, every option is equal to itself (causing a draw if both user and computer choose the same option). Secondly, every option wins over one half of the other options of the list, and gets defeated by another half. 

For example, the user's list of options is rock,paper,scissors,lizard,spock. By looking at the list spock,rock,paper,scissors you realize that spock and rock will be beating the lizard, and paper and scissors will get defeated by it. For spock it'll be almost the same, but it'll get beaten by rock and paper, and prevail over scissors and lizard.
