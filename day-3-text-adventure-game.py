# write a short story that is an adventure game using if/elif/else 
# obviously write about your pets for your wife to play the game

print('''
*******************************************************************************
                             ;\ 
                            |' \ 
         _                  ; : ; 
        / `-.              /: : | 
       |  ,-.`-.          ,': : | 
       \  :  `. `.       ,'-. : | 
        \ ;    ;  `-.__,'    `-.| 
         \ ;   ;  :::  ,::'`:.  `. 
          \ `-. :  `    :.    `.  \ 
           \   \    ,   ;   ,:    (\ 
            \   :., :.    ,'o)): ` `-. 
           ,/,' ;' ,::"'`.`---'   `.  `-._ 
         ,/  :  ; '"      `;'          ,--`. 
        ;/   :; ;             ,:'     (   ,:) 
          ,.,:.    ; ,:.,  ,-._ `.     \""'/ 
          '::'     `:'`  ,'(  \`._____.-'"' 
             ;,   ;  `.  `. `._`-.  \\ 
             ;:.  ;:       `-._`-.\  \`. 
              '`:. :        |' `. `\  ) \ 
      -hrr-      ` ;:       |    `--\__,' 
                   '`      ,' 
                        ,-' 

*******************************************************************************
''')
print("Welcome to 'The Bedtime Police'")
print("Your mission is to survive the night...") 

# convert all answers to lowercase and ensure you die with explaination for every wrong or mistyped answer
# formatting was screwy so I added line breaks to make it look nicer.

print("\nIt's bedtime and you're feeling tired. You've ignored the bedtime police\n(a.k.a. the pets) for some hours now and all is quiet in the house.")
# get the choice and convert to lowercase
answer1 = input("\nDo you want to 'remain seated' or 'get up'? \n> ").lower()
if answer1 == "get up":
  print("\nYou get up and walk into the hall. You get the feeling that you're being\nwatched. You can hear Frazey whooping at the back door.")
  answer2 = input("\nDo you want to 'go upstairs' or 'feed frazey'? \n> ").lower()
  if answer2 == "feed frazey":
    print("\nGood choice, Frazey was furious that you'd left it so late without giving\nher a dentastick. You hand her the dentastick and she spits it out on the\nfloor where it will remain uneaten.\n\nYou head upstairs and into the hallway. The cats are furious that\nyou've left it so late to feed them but quickly forget about it once you've\ngiven them some food. You're almost in the clear.")
    answer3 = input("\nDo you want to go into the 'bedroom', the 'office' or the 'bathroom?' \n> ").lower()
    if answer3 == "bedroom":
      print("\nYou go into the bedroom and lie down on the bed and fall asleep. Tim is\nvery sad you didn't say goodnight.\n\nGame over. Please try again.\n")
    elif answer3 == "bathroom":
      print("\nYou open the bathroom door. Cleo the cat comes in to tell you off for being late to bed.\n\nShe accidentally cuts your head off with a playful swipe. Mow wowow. \n\nGame over. Please try again.\n")
    elif answer3 == "office":
      print("\nYou go into the office, and find a very happy Tim playing on the computer.\nHe's very happy to see you!\n\nYou both go to bed together and survive the night.\n\nWell done - you win!\n")
    else:
      print("\nYou go into the bedroom and lie down on the bed and fall asleep. Tim is\nvery sad you didn't say goodnight.\n\nGame over. Please try again.\n")
  else:
    print("\nYou try to go upstairs but Frazey leaps out looking for a playfight and bites you.\n\ Aroooooooooooooooooooo.\n\nGame over. Please try again.\n")
else:
  print("\nYou settle down to watch another movie in front of the fire and doze off\nhappily. Unfortunately, Clementine the cat wasn't happy that you didn't feed her.\nShe's now eaten your feet and you have died.\n\nGame over. Please try again.\n")
  
 
