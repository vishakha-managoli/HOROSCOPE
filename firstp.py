zodiac =True
while zodiac == True:
    print("22 SEPTEMBER,TUESDAY")
    print("hey do you want to know how is your day going to be based on your zodiac sign")
    print('''
    1 for ARIES
    2 for TAURUS
    3 for GEMINI
    4 for CANCER
    5 for LEO
    6 for VIRGO
    7 for LIBRA
    8 for SCORPIO
    9 for SAGITTARIUS
    10 for CAPRICORN
    11 for AQUARIUS
    12 for PISCES 
    ''')
    s=int(input("pick your sign based on the number given"))
    if(s==1):
       print("ARIES")
       print(" Feeling useful will suddenly be extremely important to you. Right now you're feeling that it doesn't really matter whether you get what you want today when you see so many others who don't have anything at all. If you can be of service to someone today, you will make yourself feel valuable, like you're able to do just about anything. You are a positive force in people's lives, even the people who don't know you very well yet.")
    elif(s==2):
       print("TAURUS")
       print(" Your feelings are just under the surface today, which you could choose to see as a good thing or a bad thing. If you're looking for the courage to say something tough to someone who needs to hear it, your trigger temper could help you say it once and for all. But if you're going to be around sensitive folks you need to impress today, said temper could lead to problems. A sudden emotional reaction won't go over well, so watch your tongue and be ready to hold it.")
    elif(s==3):
       print("GEMINI")
       print("One of those charming (if a bit eccentric) characters currently in your life is getting a bit too nosy right now. Your business is yours. If you want to spare yourself some future exasperation, tell this busybody to mind their own business. Be polite, but prepare to repeat yourself because they aren't likely to get the hint right off the bat. Your life is going to be much more fascinating to other people than it is to you right now, believe it or not.")
    elif(s==4):
       print("CANCER")
       print("Don't flinch if someone delivers you some disappointing news today. Deep down, you probably knew it was coming. And if you weren't prepared enough to handle this news with ease, don't worry about how things will turn out. Instead, focus on the smaller issues that you can do something about. There are actions you can take to ease the sting of this news. Don't let yourself get drawn into the drama. Pick yourself up, dust yourself off, and carry on.")
    elif(s==5):
       print("LEO")
       print("Much to your surprise, your finances seem to be slowly falling into place. This is good news, but it doesn't mean you should go back to your old ways of shopping and (not) tracking your costs. Now that you have everything under control, don't give up! You're used to living life with a tighter belt, and there is still a lot you can learn about how to trim the fat. Keep going and you'll be very proud of what you can save in just a few months.")
    elif(s==6):
       print("VIRGO")
       print(" A group effort is the best effort today. If you want results, you need to get the help of the people who can make it happen. Align yourself with the people who know what they're doing even if they aren't your favorite people on earth. This isn't about making friends; it's about making progress on one of your life goals. These others will be able to provide all the details that make a big impression in the end. Trust their judgment.")
    elif(s==7):
       print("LIBRA")
       print("A recent spat might have left a bad taste in your mouth, but as far as everyone else is concerned, your name has no black mark on it. There have been no grudges held, so you need to do yourself a favor and forget about the unpleasantness that occurred. Focus on the future and put your best foot forward. They've already forgotten all about it, so how about you doing the same thing? Guilt won't get you where you need to go.")
    elif(s==8):
       print("SCORPIO")
       print("Today should be a good day, especially if you plan to follow up on someone's progress. They're much further along than you expected, and it will warm your heart to see how they're thriving. However, details regarding a project might escape you right now if you aren't paying careful attention. You should ask someone else to double-check your work. It will give them the opportunity to feel useful, and it will help you know what to look out for next time.")
    elif(s==9):
       print("SAGITTARIUS")
       print("What you've been waiting for is about to come your way, but the catch is you shouldn't let others see just how deliriously happy you are about it! Play it coy and play it cool. Make sure you don't rush ahead of everyone else to snatch this opportunity from their hands! Being too eager will put you at a disadvantage. Follow the lead of other people, and you will find yourself in a very advantageous position. Your patience will pay off big time.")
    elif(s==10):
       print("CAPRICORN")
       print("You need to step up to bat today, because your friends or co-workers are in desperate need of a leader like you! Right now your brain is sharp, your convivial energy is strong, and you have a fantastic ability to find out what the real facts are that underlie any current intrigue. He said/she said conflicts won't last long when you're team captain. People need you! Volunteer to take over. Everyone, including you, will be glad you did.")
    elif(s==11):
       print("AQUARIUS")
       print("One of your partners—either in romance, life, or work—may have a different agenda than you do right now. This is totally fine and won't cause any conflict, but it is something you should be aware of. A joint decision needs to be made soon, and they're leaning in the direction opposite yours. They won't understand your point of view unless you explain it to them, so speak up in a calm way. Luckily, you're good at communicating what you need.")
    elif(s==12):
       print("PISCES")
       print("Being more analytical about your emotions might sound counterintuitive, but it's the perfect approach right now, especially since your brain is humming along much more efficiently than your slightly confused heart. Examine any problems you're dealing with now. Think about them objectively. Put yourself in the position of a judge overseeing the details of a case. Once you remove your own bias from the situation, you will quickly see an easy answer.")
    else:
       print("wrong number entered")
    zodiac = True if input("shall we do it again? (yes/no)")=="yes" else False