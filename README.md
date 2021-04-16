# This is a test_level Program

## Intro

The dir has two major part, the User and the Server.

User contains the design for the User interface, currently mainly based on Wechat miniprogram

Server side contains the design for the server, based on Raspberry Pi(Model 3B) 

This project is meant for the software part of an intelligent-backpack design, which can recognize your item using RFID-tags, analyze your due-course using NLP and remind you about what you have left behind.

## Techniques 

There have been many try-outs and many failures, and I have came to a quite balanced solution for the usage in desire.

The hardware side we choose the arm-based development chip in the end due to the consideration of both power consumption and the connectivity. The sensor major in use is PN532, under I2C mode. It is a stable chip capable of reading messages from RFID tag.

The development has been going under the strict idea of 'keep it simple' so the current server system uses a basic ASGI model, in order to give test to its original capability, we have a further plan to switch it to WSGI using Django. The user interface also apply to the same idea, we use Miniprogram to ensure its robustness(using qt5 or other method would cost tons of energy doing deployment).

The NLP is quite simple, we managed to extract the time data from the natural language inputs.