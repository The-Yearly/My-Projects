import random
from tkinter import *
testwords=["Light","Cause","Point","Might","Light"]
wordle=Tk()
allwords=['ABUSE', 'ADULT', 'AGENT', 'ANGER', 'APPLE', 'AWARD', 'BASIS', 'BEACH', 'BIRTH', 'BLOCK', 'BLOOD', 'BOARD', 'BRAIN', 'BREAD', 'BREAK', 'BROWN', 'BUYER', 'CAUSE', 'CHAIN', 'CHAIR', 'CHEST', 'CHIEF', 'CHILD', 'CHINA', 'CLAIM', 'CLASS', 'CLOCK', 'COACH', 'COAST', 'COURT', 'COVER', 'CREAM', 'CRIME', 'CROSS', 'CROWD', 'CROWN', 'CYCLE', 'DANCE', 'DEATH', 'DEPTH', 'DOUBT', 'DRAFT', 'DRAMA', 'DREAM', 'DRESS', 'DRINK', 'DRIVE', 'EARTH', 'ENEMY', 'ENTRY', 'ERROR', 'EVENT', 'FAITH', 'FAULT', 'FIELD', 'FIGHT', 'FINAL', 'FLOOR', 'FOCUS', 'FORCE', 'FRAME', 'FRANK', 'FRONT', 'FRUIT', 'GLASS', 'GRANT', 'GRASS', 'GREEN', 'GROUP', 'GUIDE', 'HEART', 'HENRY', 'HORSE', 'HOTEL', 'HOUSE', 'IMAGE', 'INDEX', 'INPUT', 'ISSUE', 'JAPAN', 'JONES', 'JUDGE', 'KNIFE', 'LAURA', 'LAYER', 'LEVEL', 'LEWIS', 'LIGHT', 'LIMIT', 'LUNCH', 'MAJOR', 'MARCH', 'MATCH', 'METAL', 'MODEL', 'MONEY', 'MONTH', 'MOTOR', 'MOUTH', 'MUSIC', 'NIGHT', 'NOISE', 'NORTH', 'NOVEL', 'NURSE', 'OFFER', 'ORDER', 'OTHER', 'OWNER', 'PANEL', 'PAPER', 'PARTY', 'PEACE', 'PETER', 'PHASE', 'PHONE', 'PIECE', 'PILOT', 'PITCH', 'PLACE', 'PLANE', 'PLANT', 'PLATE', 'POINT', 'POUND', 'POWER', 'PRESS', 'PRICE', 'PRIDE', 'PRIZE', 'PROOF', 'QUEEN', 'RADIO', 'RANGE', 'RATIO', 'REPLY', 'RIGHT', 'RIVER', 'ROUND', 'ROUTE', 'RUGBY', 'SCALE', 'SCENE', 'SCOPE', 'SCORE', 'SENSE', 'SHAPE', 'SHARE', 'SHEEP', 'SHEET', 'SHIFT', 'SHIRT', 'SHOCK', 'SIGHT', 'SIMON', 'SKILL', 'SLEEP', 'SMILE', 'SMITH', 'SMOKE', 'SOUND', 'SOUTH', 'SPACE', 'SPEED', 'SPITE', 'SPORT', 'SQUAD', 'STAFF', 'STAGE', 'START', 'STATE', 'STEAM', 'STEEL', 'STOCK', 'STONE', 'STORE', 'STUDY', 'STUFF', 'STYLE', 'SUGAR', 'TABLE', 'TASTE', 'TERRY', 'THEME', 'THING', 'TITLE', 'TOTAL', 'TOUCH', 'TOWER', 'TRACK', 'TRADE', 'TRAIN', 'TREND', 'TRIAL', 'TRUST', 'TRUTH', 'UNCLE', 'UNION', 'UNITY', 'VALUE', 'VIDEO', 'VISIT', 'VOICE', 'WASTE', 'WATCH', 'WATER', 'WHILE', 'WHITE', 'WHOLE', 'WOMAN', 'WORLD', 'YOUTH', '5', 'LETTER', 'PRONOUNS', 'ALCON', 'AUGHT', 'HELLA', 'ONEÂ€™S', 'OUGHT', 'THAME', 'THERE', 'THINE', 'THINE', 'WHERE', 'WHICH', 'WHOSE', 'WHOSO', 'YOURS', 'YOURS', '5', 'LETTER', 'VERBS', 'ADMIT', 'ADOPT', 'AGREE', 'ALLOW', 'ALTER', 'APPLY', 'ARGUE', 'ARISE', 'AVOID', 'BEGIN', 'BLAME', 'BREAK', 'BRING', 'BUILD', 'BURST', 'CARRY', 'CATCH', 'CAUSE', 'CHECK', 'CLAIM', 'CLEAN', 'CLEAR', 'CLIMB', 'CLOSE', 'COUNT', 'COVER', 'CROSS', 'DANCE', 'DOUBT', 'DRINK', 'DRIVE', 'ENJOY', 'ENTER', 'EXIST', 'FIGHT', 'FOCUS', 'FORCE', 'GUESS', 'IMPLY', 'ISSUE', 'JUDGE', 'LAUGH', 'LEARN', 'LEAVE', 'LETÂ€™S', 'LIMIT', 'MARRY', 'MATCH', 'OCCUR', 'OFFER', 'ORDER', 'PHONE', 'PLACE', 'POINT', 'PRESS', 'PROVE', 'RAISE', 'REACH', 'REFER', 'RELAX', 'SERVE', 'SHALL', 'SHARE', 'SHIFT', 'SHOOT', 'SLEEP', 'SOLVE', 'SOUND', 'SPEAK', 'SPEND', 'SPLIT', 'STAND', 'START', 'STATE', 'STICK', 'STUDY', 'TEACH', 'THANK', 'THINK', 'THROW', 'TOUCH', 'TRAIN', 'TREAT', 'TRUST', 'VISIT', 'VOICE', 'WASTE', 'WATCH', 'WORRY', 'WOULD', 'WRITE', 'ABOVE', 'ACUTE', 'ALIVE', 'ALONE', 'ANGRY', 'AWARE', 'AWFUL', 'BASIC', 'BLACK', 'BLIND', 'BRAVE', 'BRIEF', 'BROAD', 'BROWN', 'CHEAP', 'CHIEF', 'CIVIL', 'CLEAN', 'CLEAR', 'CLOSE', 'CRAZY', 'DAILY', 'DIRTY', 'EARLY', 'EMPTY', 'EQUAL', 'EXACT', 'EXTRA', 'FAINT', 'FALSE', 'FIFTH', 'FINAL', 'FIRST', 'FRESH', 'FRONT', 'FUNNY', 'GIANT', 'GRAND', 'GREAT', 'GREEN', 'GROSS', 'HAPPY', 'HARSH', 'HEAVY', 'HUMAN', 'IDEAL', 'INNER', 'JOINT', 'LARGE', 'LEGAL', 'LEVEL', 'LIGHT', 'LOCAL', 'LOOSE', 'LUCKY', 'MAGIC', 'MAJOR', 'MINOR', 'MORAL', 'NAKED', 'NASTY', 'NAVAL', 'OTHER', 'OUTER', 'PLAIN', 'PRIME', 'PRIOR', 'PROUD', 'QUICK', 'QUIET', 'RAPID', 'READY', 'RIGHT', 'ROMAN', 'ROUGH', 'ROUND', 'ROYAL', 'RURAL', 'SHARP', 'SHEER', 'SHORT', 'SILLY', 'SIXTH', 'SMALL', 'SMART', 'SOLID', 'SORRY', 'SPARE', 'STEEP', 'STILL', 'SUPER', 'SWEET', 'THICK', 'THIRD', 'TIGHT', 'TOTAL', 'TOUGH', 'UPPER', 'UPSET', 'URBAN', 'USUAL', 'VAGUE', 'VALID', 'VITAL', 'WHITE', 'WHOLE', 'WRONG', 'YOUNG', 'AFORE', 'AFTER', 'BOTHE', 'OTHER', 'SINCE', 'SLASH', 'UNTIL', 'WHERE', 'WHILE', 'ABACK', 'ABAFT', 'ABOON', 'ABOUT', 'ABOVE', 'ACCEL', 'ADOWN', 'AFOOT', 'AFORE', 'AFOUL', 'AFTER', 'AGAIN', 'AGAPE', 'AGOGO', 'AGONE', 'AHEAD', 'AHULL', 'ALIFE', 'ALIKE', 'ALINE', 'ALOFT', 'ALONE', 'ALONG', 'ALOOF', 'ALOUD', 'AMISS', 'AMPLY', 'AMUCK', 'APACE', 'APART', 'APTLY', 'AREAR', 'ASIDE', 'ASKEW', 'AWFUL', 'BADLY', 'BALLY', 'BELOW', 'CANNY', 'CHEAP', 'CLEAN', 'CLEAR', 'COYLY', 'DAILY', 'DIMLY', 'DIRTY', 'DITTO', 'DRILY', 'DRYLY', 'DULLY', 'EARLY', 'EXTRA', 'FALSE', 'FATLY', 'FEYLY', 'FIRST', 'FITLY', 'FORTE', 'FORTH', 'FRESH', 'FULLY', 'FUNNY', 'GAILY', 'GAYLY', 'GODLY', 'GREAT', 'HAPLY', 'HEAVY', 'HELLA', 'HENCE', 'HOTLY', 'ICILY', 'INFRA', 'JILDI', 'JOLLY', 'LAXLY', 'LENTO', 'LIGHT', 'LOWLY', 'MADLY', 'MAYBE', 'NEVER', 'NEWLY', 'NOBLY', 'ODDLY', 'OFTEN', 'OTHER', 'OUGHT', 'PARTY', 'PIANO', 'PLAIN', 'PLONK', 'PLUMB', 'PRIOR', 'QUEER', 'QUICK', 'QUITE', 'RAMEN', 'RAPID', 'REDLY', 'RIGHT', 'ROUGH', 'ROUND', 'SADLY', 'SECUS', 'SELLY', 'SHARP', 'SHEER', 'SHILY', 'SHORT', 'SHYLY', 'SILLY', 'SINCE', 'SLEEK', 'SLYLY', 'SMALL', 'SO-SO', 'SOUND', 'SPANG', 'SRSLY', 'STARK', 'STILL', 'STONE', 'STOUR', 'SUPER', 'TALLY', 'TANTO', 'THERE', 'THICK', 'TIGHT', 'TODAY', 'TOMOZ', 'TRULY', 'TWICE', 'UNDER', 'UTTER', 'VERRY', 'WANLY', 'WETLY', 'WHERE', 'WRONG', 'WRYLY', 'ABAFT', 'ABOON', 'ABOUT', 'ABOVE', 'ADOWN', 'AFORE', 'AFTER', 'ALONG', 'ALOOF', 'AMONG', 'BELOW', 'CIRCA', 'CROSS', 'FURTH', 'MINUS', 'NEATH', 'ROUND', 'SINCE', 'SPITE', 'UNDER', 'UNTIL', 'ADIOS', 'ALACK', 'ALOHA', 'AVAST', 'BAKAW', 'BASTA', 'BEGAD', 'BLESS', 'BLIGE', 'BRAVA', 'BRAVO', 'BRING', 'CHOOK', 'DAMME', 'DILDO', 'DITTO', 'FRICK', 'FUDGE', 'GOLLY', 'GRATZ', 'HALLO', 'HASTA', 'HAVOC', 'HELLA', 'HELLO', 'HOWAY', 'HOWDY', 'HULLO', 'HUZZA', 'JESUS', 'KAPOW', 'LOOSE', 'LORDY', 'MARRY', 'MERCY', 'NIGHT', 'PLONK', 'PSYCH', 'QUITE', 'SALVE', 'SKOAL', 'SNIFF', 'SOOEY', 'THERE', 'THIAM', 'THWAP', 'TOUGH', 'TWIRP', 'VIOLA', 'VIVAT', 'WACKO', 'WAHEY', 'WHIST', 'WILMA', 'WIRRA', 'WOOPS', 'WOWIE', 'YECCH', 'YEEHA', 'YEESH', 'YOWCH']
wordle.geometry("400x480")
wordle.config(bg="Grey")
wordle.title("YORDLE")
l1p1=Label(font="Aleo",bg="White",width=4)
l1p1.place(x=50,y=50)
l1p2=Label(font="Aleo",bg="White",width=4)
l1p2.place(x=110,y=50)
l1p3=Label(font="Aleo",bg="White",width=4)
l1p3.place(x=170,y=50)
l1p4=Label(font="Aleo",bg="White",width=4)
l1p4.place(x=230,y=50)
l1p5=Label(font="Aleo",bg="White",width=4)
l1p5.place(x=290,y=50)
l2p1=Label(font="Aleo",bg="White",width=4)
l2p1.place(x=50,y=90)
l2p2=Label(font="Aleo",bg="White",width=4)
l2p2.place(x=110,y=90)
l2p3=Label(font="Aleo",bg="White",width=4)
l2p3.place(x=170,y=90)
l2p4=Label(font="Aleo",bg="White",width=4)
l2p4.place(x=230,y=90)
l2p5=Label(font="Aleo",bg="White",width=4)
l2p5.place(x=290,y=90)
l3p1=Label(font="Aleo",bg="White",width=4)
l3p1.place(x=50,y=130)
l3p2=Label(font="Aleo",bg="White",width=4)
l3p2.place(x=110,y=130)
l3p3=Label(font="Aleo",bg="White",width=4)
l3p3.place(x=170,y=130)
l3p4=Label(font="Aleo",bg="White",width=4)
l3p4.place(x=230,y=130)
l3p5=Label(font="Aleo",bg="White",width=4)
l3p5.place(x=290,y=130)
l4p1=Label(font="Aleo",bg="White",width=4)
l4p1.place(x=50,y=170)
l4p2=Label(font="Aleo",bg="White",width=4)
l4p2.place(x=110,y=170)
l4p3=Label(font="Aleo",bg="White",width=4)
l4p3.place(x=170,y=170)
l4p4=Label(font="Aleo",bg="White",width=4)
l4p4.place(x=230,y=170)
l4p5=Label(font="Aleo",bg="White",width=4)
l4p5.place(x=290,y=170)
l5p1=Label(font="Aleo",bg="White",width=4)
l5p1.place(x=50,y=210)
l5p2=Label(font="Aleo",bg="White",width=4)
l5p2.place(x=110,y=210)
l5p3=Label(font="Aleo",bg="White",width=4)
l5p3.place(x=170,y=210)
l5p4=Label(font="Aleo",bg="White",width=4)
l5p4.place(x=230,y=210)
l5p5=Label(font="Aleo",bg="White",width=4)
l5p5.place(x=290,y=210)
l6p1=Label(font="Aleo",bg="White",width=4)
l6p1.place(x=50,y=250)
l6p2=Label(font="Aleo",bg="White",width=4)
l6p2.place(x=110,y=250)
l6p3=Label(font="Aleo",bg="White",width=4)
l6p3.place(x=170,y=250)
l6p4=Label(font="Aleo",bg="White",width=4)
l6p4.place(x=230,y=250)
l6p5=Label(font="Aleo",bg="White",width=4)
l6p5.place(x=290,y=250)
yordle=Label(text="YORDLE",font=("Aleo",18),bg="Grey",fg="White")
yordle.place(x=137,y=10)
gu=1
wordindex=random.randint(0,len(allwords))
solution=allwords[wordindex]
solution=solution.upper()
print(solution)
lp=1
le=""
word1=""
p1c1="White"
p1c2="White"
p1c3="White"
p1c4="White"
p1c5="White"
p3c1=""
p3c3=""
p5c3=""
p6c4=""
def ne():
 global lp,gu,word1,l1p1,p1c1,p1c2,p1c3,p1c4,p1c5,p2c1,p2c2,p2c3,p2c4,p2c5,p3c1,p3c2,p3c3,p3c4,p3c5,p4c1,p4c2,p4c3,p4c4,p4c5
 global p4c1,p4c2,p4c3,p4c4,p4c5,p5c1,p5c2,p5c3,p5c4,p5c5,p6c1,p6c2,p6c3,p6c4,p6c5,solution,allwords,word1
 global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z
 print(word1 in allwords)
 co=0
 if lp==6:
  if gu==1:
   l1p1.config(bg=p1c1)
   l1p2.config(bg=p1c2)
   l1p3.config(bg=p1c3)
   l1p4.config(bg=p1c4)
   l1p5.config(bg=p1c5)
  if gu==2:
   l2p1.config(bg=p2c1)
   l2p2.config(bg=p2c2)
   l2p3.config(bg=p2c3)
   l2p4.config(bg=p2c4)
   l2p5.config(bg=p2c5) 
  if gu==3:
   l3p1.config(bg=p3c1)
   l3p2.config(bg=p3c2)
   l3p3.config(bg=p3c3)
   l3p4.config(bg=p3c4)
   l3p5.config(bg=p3c5)
  if gu==4:
   l4p1.config(bg=p4c1)
   l4p2.config(bg=p4c2)
   l4p3.config(bg=p4c3)
   l4p4.config(bg=p4c4)
   l4p5.config(bg=p4c5)
  if gu==5:
   l5p1.config(bg=p5c1)
   l5p2.config(bg=p5c2)
   l5p3.config(bg=p5c3)
   l5p4.config(bg=p5c4)
   l5p5.config(bg=p5c5)
  if gu==6:
   l6p1.config(bg=p6c1)
   l6p2.config(bg=p6c2)
   l6p3.config(bg=p6c3)
   l6p4.config(bg=p6c4)
   l6p5.config(bg=p6c5)
  gu+=1
  lp=1
  for ga in word1:
   print(word1[co],solution[co])
   if ga in solution:
    if word1[co]==solution[co]==ga:
     if ga=="A":
      a.config(bg="Green")
     if ga=="B":
      b.config(bg="Green")
     if ga=="C":
      c.config(bg="Green")
     if ga=="D":
      d.config(bg="Green")
     if ga=="E":
      e.config(bg="Green")
     if ga=="F":
      f.config(bg="Green")
     if ga=="G":
      g.config(bg="Green")
     if ga=="H":
      h.config(bg="Green")
     if ga=="I":
      i.config(bg="Green")
     if ga=="J":
      j.config(bg="Green")
     if ga=="K":
      k.config(bg="Green")
     if ga=="L":
      l.config(bg="Green")
     if ga=="M":
      m.config(bg="Green")
     if ga=="N":
      n.config(bg="Green")
     if ga=="O":
      o.config(bg="Green")
     if ga=="P":
      p.config(bg="Green")
     if ga=="Q":
      q.config(bg="Green")
     if ga=="R":
      r.config(bg="Green")
     if ga=="S":
      s.config(bg="Green")
     if ga=="T":
      t.config(bg="Green")
     if ga=="U":
      u.config(bg="Green")
     if ga=="V":
      v.config(bg="Green")
     if ga=="W":
      w.config(bg="Green")
     if ga=="X":
      x.config(bg="Green")
     if ga=="Y":
      y.config(bg="Green")
     if ga=="Z":
      z.config(bg="Green")
    else:
     if ga=="A":
      a.config(bg="Orange")
     if ga=="B":
      b.config(bg="Orange")
     if ga=="C":
      c.config(bg="Orange")
     if ga=="D":
      d.config(bg="Orange")
     if ga=="E":
      e.config(bg="Orange")
     if ga=="F":
      f.config(bg="Orange")
     if ga=="G":
      g.config(bg="Orange")
     if ga=="H":
      h.config(bg="Orange")
     if ga=="I":
      i.config(bg="Orange")
     if ga=="J":
      j.config(bg="Orange")
     if ga=="K":
      k.config(bg="Orange")
     if ga=="L":
      l.config(bg="Orange")
     if ga=="M":
      m.config(bg="Orange")
     if ga=="N":
      n.config(bg="Orange")
     if ga=="O":
      o.config(bg="Orange")
     if ga=="P":
      p.config(bg="Orange")
     if ga=="Q":
      q.config(bg="Orange")
     if ga=="R":
      r.config(bg="Orange")
     if ga=="S":
      s.config(bg="Orange")
     if ga=="T":
      t.config(bg="Orange")
     if ga=="U":
      u.config(bg="Orange")
     if ga=="V":
      v.config(bg="Orange")
     if ga=="W":
      w.config(bg="Orange")
     if ga=="X":
      x.config(bg="Orange")
     if ga=="Y":
      y.config(bg="Orange")
     if ga=="Z":
      z.config(bg="Orange")
   else:
    if ga=="A":
     a.config(bg="Red")
    if ga=="B":
     b.config(bg="Red")
    if ga=="C":
     c.config(bg="Red")
    if ga=="D":
     d.config(bg="Red")
    if ga=="E":
     e.config(bg="Red")
    if ga=="F":
     f.config(bg="Red")
    if ga=="G":
     g.config(bg="Red")
    if ga=="H":
     h.config(bg="Red")
    if ga=="I":
     i.config(bg="Red")
    if ga=="J":
     j.config(bg="Red")
    if ga=="K":
     k.config(bg="Red")
    if ga=="L":
     l.config(bg="Red")
    if ga=="M":
     m.config(bg="Red")
    if ga=="N":
     n.config(bg="Red")
    if ga=="O":
     o.config(bg="Red")
    if ga=="P":
     p.config(bg="Red")
    if ga=="Q":
     q.config(bg="Red")
    if ga=="R":
     r.config(bg="Red")
    if ga=="S":
     s.config(bg="Red")
    if ga=="T":
     t.config(bg="Red")
    if ga=="U":
     u.config(bg="Red")
    if ga=="V":
     v.config(bg="Red")
    if ga=="W":
     w.config(bg="Red")
    if ga=="X":
     x.config(bg="Red")
    if ga=="Y":
     y.config(bg="Red")
    if ga=="Z":
     z.config(bg="Red")
   co+=1
  if gu>6:
    final=Label(text="The Correct Answer Is ",font="Aleo",bg="Grey")
    fa=Label(text=solution,font="Aleo",bg="Grey")
    final.place(x=40,y=300)
    fa.place(x=200,y=300)
  print("gu",gu)
  if gu==2:
   word1=""
  if gu==3:
   word1="" 
  if gu==4:
   word1=""
  if gu==5:
   word1=""
  if gu==6:
   word1=""  
def clear():
 global lp,gu,word1
 lp-=1
 if lp==0:
  lp=1
 if gu==1:
  if lp==1:
   l1p1.config(text=" ")
  if lp==2:
   l1p2.config(text=" ") 
  if lp==3:
   l1p3.config(text=" ")
  if lp==4:
   l1p4.config(text=" ")
  if lp==5:
   l1p5.config(text=" ")
  word1=word1[:-1] 
 if gu==2:
  if lp==1:
   l2p1.config(text=" ")
  if lp==2:
   l2p2.config(text=" ") 
  if lp==3:
   l2p3.config(text=" ")
  if lp==4:
   l2p4.config(text=" ")
  if lp==5:
   l2p5.config(text=" ")
  word1=word1[:-1]
 if gu==3:
  if lp==1:
   l3p1.config(text=" ")
  if lp==2:
   l3p2.config(text=" ") 
  if lp==3:
   l3p3.config(text=" ")
  if lp==4:
   l3p4.config(text=" ")
  if lp==5:
   l3p5.config(text=" ")
  word1=word1[:-1] 
 if gu==4:
  if lp==1:
   l4p1.config(text=" ")
  if lp==2:
   l4p2.config(text=" ") 
  if lp==3:
   l4p3.config(text=" ")
  if lp==4:
   l4p4.config(text=" ")
  if lp==5:
   l4p5.config(text=" ")
  word1=word1[:-1]
 if gu==5:
  if lp==1:
   l5p1.config(text=" ")
  if lp==2:
   l5p2.config(text=" ") 
  if lp==3:
   l5p3.config(text=" ")
  if lp==4:
   l5p4.config(text=" ")
  if lp==5:
   l5p5.config(text=" ")  
  word1=word1[:-1]
 if gu==6:
  if lp==1:
   l6p1.config(text=" ")
  if lp==2:
   l6p2.config(text=" ") 
  if lp==3:
   l6p3.config(text=" ")
  if lp==4:
   l6p4.config(text=" ")
  if lp==5:
   l6p5.config(text=" ")  
  word1=word1[:-1]
def a():
 global le,word1
 le="A"
 word1+=le
 sub()
def b():
 global le,word1   
 le="B"
 word1+=le
 sub()
def c():
 global le,word1
 le="C"
 word1+=le
 sub()
def d():
 global le,word1   
 le="D"
 word1+=le
 sub()
def e():
 global le,word1   
 le="E"
 word1+=le
 sub()
def f():
 global le,word1   
 le="F"
 word1+=le
 sub()
def g():
 global le,word1
 le="G"
 word1+=le
 sub()
def h():
 global le,word1   
 le="H"
 word1+=le
 sub()
def i():
 global le,word1
 le="I"
 word1+=le
 sub()
def j():
 global le,word1
 le="J"
 word1+=le
 sub()
def k():
 global le,word1   
 le="K"
 word1+=le
 sub()
def l():
 global le,word1   
 le="L"
 word1+=le
 sub()
def m():
 global le,word1   
 le="M"
 word1+=le
 sub()
def n():
 global le,word1   
 le="N"
 word1+=le
 sub()
def o():
 global le,word1   
 le="O"
 word1+=le
 sub()
def p():
 global le,word1   
 le="P"
 word1+=le
 sub()
def q():
 global le,word1   
 le="Q"
 word1+=le
 sub()
def r():
 global le,word1   
 le="R"
 word1+=le
 sub()
def s():
 global le,word1   
 le="S"
 word1+=le
 sub()
def t():
 global le,word1   
 le="T"
 word1+=le
 sub()
def u():
 global le,word1   
 le="U"
 word1+=le
 sub()
def v():
 global le,word1   
 le="V"
 word1+=le
 sub()
def w():
 global le,word1   
 le="W"
 word1+=le
 sub()
def x():
 global le,word1   
 le="X"
 word1+=le
 sub()
def y():
 global le,word1   
 le="Y"
 word1+=le
 sub()
def z():
 global le,word1   
 le="Z"
 word1+=le
 sub() 
def sub():
 global lp,gu,word1,p1c1,p1c2,p1c3,p1c4,p1c5,p2c1,p2c2,p2c3,p2c4,p2c5,p3c1,p3c2,p3c3,p3c4,p3c5,p4c2,p4c3,p4c4,p4c5
 global p4c1,p5c1,p5c2,p5c3,p5c4,p5c5,p6c1,p6c2,p6c3,p6c4,p6c5
 print(gu)
 if len(word1)==6:
  word1=word1[:-1]
 if word1[len(word1)-1] in solution:
  if word1[len(word1)-1]==solution[len(word1)-1]:
   print(word1[len(word1)-1],"Exact spot")
   if gu==1:
    if lp==1:
     p1c1="Green"
    if lp==2:
     p1c2="Green"
    if lp==3:
     p1c3="Green"
    if lp==4:
     p1c4="Green"
    if lp==5:
     p1c5="Green"    
   if gu==2:
    if lp==1:
     p2c1="Green"
    if lp==2:
     p2c2="Green"
    if lp==3:
     p2c3="Green"
    if lp==4:
     p2c4="Green"
    if lp==5:
     p2c5="Green"
   if gu==3:
    if lp==1:
     p3c1="Green"
    if lp==2:
     p3c2="Green"
    if lp==3:
     p3c3="Green"
    if lp==4:
     p3c4="Green"
    if lp==5:
     p3c5="Green"  
    if lp==5:
     p2c5="Green"
   if gu==4:
    if lp==1:
     p4c1="Green"
     print(p4c1)
    if lp==2:
     p4c2="Green"
     print("2")
    if lp==3:
     p4c3="Green"
    if lp==4:
     p4c4="Green"
    if lp==5:
     p4c5="Green"  
   if gu==5:
    if lp==1:
     p5c1="Green"
     print(p4c1)
    if lp==2:
     p5c2="Green"
     print("2")
    if lp==3:
     p5c3="Green"
    if lp==4:
     p5c4="Green"
    if lp==5:
     p5c5="Green"
   if gu==6:
    if lp==1:
     p6c1="Green"
     print(p4c1)
    if lp==2:
     p6c2="Green"
     print("2")
    if lp==3:
     p6c3="Green"
    if lp==4:
     p6c4="Green"
    if lp==5:
     p6c5="Green"
  else:
   print(word1[len(word1)-1],"NoT exact")
   if gu==1:
    if lp==1:
     p1c1="Orange"
    if lp==2:
     p1c2="Orange"
    if lp==3:
     p1c3="Orange"
    if lp==4:
     p1c4="Orange"
    if lp==5:
     p1c5="Orange"  
   if gu==2:
    if lp==1:
     p2c1="Orange"
    if lp==2:
     p2c2="Orange"
    if lp==3:
     p2c3="Orange"
    if lp==4:
     p2c4="Orange"
    if lp==5:
     p2c5="Orange"  
   if gu==3:
    if lp==1:
     p3c1="Orange"
    if lp==2:
     p3c2="Orange"
    if lp==3:
     p3c3="Orange"
    if lp==4:
     p3c4="Orange"
    if lp==5:
     p3c5="Orange" 
   if gu==4:
    if lp==1:
     p4c1="Orange"
    if lp==2:
     p4c2="Orange"
    if lp==3:
     p4c3="Orange"
    if lp==4:
     p4c4="Orange"
    if lp==5:
     p4c5="Orange"
   if gu==5:
    if lp==1:
     p5c1="Orange"
    if lp==2:
     p5c2="Orange"
    if lp==3:
     p5c3="Orange"
    if lp==4:
     p5c4="Orange"
    if lp==5:
     p5c5="Orange"
     p4c5="Orange"
   if gu==6:
    if lp==1:
     p6c1="Orange"
    if lp==2:
     p6c2="Orange"
    if lp==3:
     p6c3="Orange"
    if lp==4:
     p6c4="Orange"
    if lp==5:
     p6c5="Orange"
 if word1[len(word1)-1] not in solution:
  print(word1[len(word1)-1],"Not In")
  if gu==1:
    if lp==1:
     p1c1="Red"
    if lp==2:
     p1c2="Red"
    if lp==3:
     p1c3="Red"
    if lp==4:
     p1c4="Red"
    if lp==5:
     p1c5="Red"    
  if gu==2:
    if lp==1:
     p2c1="Red"
    if lp==2:
     p2c2="Red"
    if lp==3:
     p2c3="Red"
    if lp==4:
     p2c4="Red"
    if lp==5:
     p2c5="Red" 
  if gu==3:
    if lp==1:
     p3c1="Red"
    if lp==2:
     p3c2="Red"
    if lp==3:
     p3c3="Red"
    if lp==4:
     p3c4="Red"
    if lp==5:
     p3c5="Red" 
  if gu==4:
    if lp==1:
     p4c1="Red"
    if lp==2:
     p4c2="Red"
    if lp==3:
     p4c3="Red"
    if lp==4:
     p4c4="Red"
    if lp==5:
     p4c5="Red" 
  if gu==5:
    if lp==1:
     p5c1="Red"
    if lp==2:
     p5c2="Red"
    if lp==3:
     p5c3="Red"
    if lp==4:
     p5c4="Red"
    if lp==5:
     p5c5="Red"
  if gu==6:
    if lp==1:
     p6c1="Red"
    if lp==2:
     p6c2="Red"
    if lp==3:
     p6c3="Red"
    if lp==4:
     p6c4="Red"
    if lp==5:
     p6c5="Red"
  print(p6c4)
 if gu==1:
  if lp==1:
   l1p1.config(text=le)
  if lp==2:
   l1p2.config(text=le) 
  if lp==3:
   l1p3.config(text=le)
  if lp==4:
   l1p4.config(text=le)
  if lp==5:
   l1p5.config(text=le) 
 if gu==2:
  if lp==1:
   l2p1.config(text=le)
  if lp==2:
   l2p2.config(text=le) 
  if lp==3:
   l2p3.config(text=le)
  if lp==4:
   l2p4.config(text=le)
  if lp==5:
   l2p5.config(text=le)
 if gu==3:
  if lp==1:
   l3p1.config(text=le)
  if lp==2:
   l3p2.config(text=le) 
  if lp==3:
   l3p3.config(text=le)
  if lp==4:
   l3p4.config(text=le)
  if lp==5:
   l3p5.config(text=le)  
 if gu==4:
  if lp==1:
   l4p1.config(text=le)
  if lp==2:
   l4p2.config(text=le) 
  if lp==3:
   l4p3.config(text=le)
  if lp==4:
   l4p4.config(text=le)
  if lp==5:
   l4p5.config(text=le)  
 if gu==5:
  if lp==1:
   l5p1.config(text=le)
  if lp==2:
   l5p2.config(text=le) 
  if lp==3:
   l5p3.config(text=le)
  if lp==4:
   l5p4.config(text=le)
  if lp==5:
   l5p5.config(text=le)
 if gu==6:
  if lp==1:
   l6p1.config(text=le)
  if lp==2:
   l6p2.config(text=le) 
  if lp==3:
   l6p3.config(text=le)
  if lp==4:
   l6p4.config(text=le)
  if lp==5:
   l6p5.config(text=le)     
 if lp<6:
  lp+=1
 if lp==6:
  lp=6
 print(lp)
 print(word1)
a=Button(text="A",command=a)
a.place(x=65,y=380)
b=Button(text="B",command=b)
b.place(x=195,y=420)
c=Button(text="C",command=c)
c.place(x=145,y=420)
d=Button(text="D",command=d)
d.place(x=115,y=380)
e=Button(text="E",command=e)
e.place(x=96,y=340)
f=Button(text="F",command=f)
f.place(x=140,y=380)
g=Button(text="G",command=g)
g.place(x=165,y=380)
h=Button(text="H",command=h)
h.place(x=190,y=380)
i=Button(text="I",command=i)
i.place(x=220,y=340)
j=Button(text="J",command=j)
j.place(x=215,y=380)
k=Button(text="K",command=k)
k.place(x=240,y=380)
l=Button(text="L",command=l)
l.place(x=265,y=380)
m=Button(text="M",command=m)
m.place(x=245,y=420)
n=Button(text="N",command=n)
n.place(x=220,y=420)
o=Button(text="O",command=o)
o.place(x=245,y=340)
p=Button(text="P",command=p)
p.place(x=270,y=340)
q=Button(text="Q",command=q)
q.place(x=45,y=340)
r=Button(text="R",command=r)
r.place(x=145,y=340)
s=Button(text="S",command=s)
s.place(x=90,y=380)
t=Button(text="T",command=t)
t.place(x=120,y=340)
u=Button(text="U",command=u)
u.place(x=195,y=340)
v=Button(text="V",command=v)
v.place(x=170,y=420)
w=Button(text="W",command=w)
w.place(x=70,y=340)
x=Button(text="X",command=x)
x.place(x=120,y=420)
y=Button(text="Y",command=y)
y.place(x=170,y=340)
z=Button(text="Z",command=z)
z.place(x=95,y=420)
back=Button(text="Clear",command=clear)
back.place(x=300,y=380)
nex=Button(text="Next",command=ne)
nex.place(x=300,y=340)
wordle.mainloop()
