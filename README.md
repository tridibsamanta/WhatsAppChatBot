# WhatsAppChatBot ©tridibsamanta
WhatsApp Automation using Python

***** FOLLOW THE INSTRUCTIONS *****

● Check whether python is installed in the system. 
  Open the cmd and write : 
  python -V
  
● Check whether pip is installed in the system.
  In cmd write :
  pip -V
  
● Open python IDLE and write the following statement
  import pyautogui as p
  If import is not successful, install the pyautogui library using the command- pip install pyautogui , in cmd.
  
● Open WhatsApp Web (https://web.whatsapp.com) and place the mouse cursor on the "search" box, now dont move the mouse cursor from there and open the IDLE. Don't use the mouse, use Alt+Tab to open IDLE.

● Now write the following statement 
  p.position()
  Sample output will be like - Point(x=190,y=150)

● Open the WhatsAppChatBot.py in an editor and edit the line 38
  p.click(put the value of x,put the value of y)

● Now open WhatsApp Web, and open a chat which has a last message sent by receiver, move the mouse cursor the top of the last message and then place the cursor there and take the position of the cursor in the same way as explained above in IDLE.

● Put the values of x and y in line no 44

● Now move the cursor to the position where the message ends and navigate to the IDLE and take the position of the cursor using p.position() statement.

● Now substract the values of x and y in line no. 44 from the newly obtained x and y values in the previous step.

● Put the resultant x and y values obtained after substraction in line 45
  p.dragRel(Substracted x value, Substracted y value, 0.5)

● I have used the pyttsx3, the Text-to-speech library which will even send a recorded voice message as specfied in the code.

● Go to WhatsApp Web, place the mouse cursor on the microphone icon beside type a message box, and in the same way as mentioned above get the position of the mouse cursor the in the IDLE.

● Put the obtained value of x and y in line 136 and line 139. This turns on the recording, meanwhile the text is read and then sends the recording to the receiver.

● In line 39, type the name of the receiver in the p.typewrite("Name of receiver here\n") statement.

● I have added a few basic questions, keep on adding more. There's a lots to improve here, keep thinking and suggest edits. Happy developing and keep codes open source and help others to learn. 

******MADE WITH ♥ BY TRIDIB SAMANTA******
