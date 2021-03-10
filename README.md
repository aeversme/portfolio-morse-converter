# **Morse Code Converter**

### A #100DaysOfCode Portfolio Project

This is a simple, text-based program that takes a string input and converts it into formatted Morse code. Mirroring 
Morse convention, letters are separated by three spaces and words are separated by seven spaces.

The conversion dictionary includes letters, numbers, and punctuation. The program uses error-handling to catch 
characters that are not part of International Morse Code.

Dictionary reference: <a href="https://en.wikipedia.org/wiki/Morse_code">'Morse code' on Wikipedia</a>

### **Reflection**

When presented with this challenge, I first took a few minutes to write down the requirements for this program in the 
form of TODOs - for example, receive a user input; handle exceptions; and format the output to be readable. I looked up 
Morse code and wrote an initial dictionary in a separate module, and then dove into coding the logic.

The only major change I ended up making to my initial attempt was to move exception handling out of the converter 
function and into the interface function, at the recommendation of my mentor (letting the converter function throw is 
fine; it doesn't need to know what happens if its process fails).