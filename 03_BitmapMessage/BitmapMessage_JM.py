import sys

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print("Hello and Welcome, now write the message You want to use as bitmap")
message = input('> ')

# Empty message means empty image
if message == '':
    sys.exit

# Loop for moving through every line of bitmap
for line in bitmap.splitlines():
    # Loop for moving through every bit in the current line
    for i, bit in enumerate(line):
        if bit == ' ':
            print(' ',end='')
        else:
            print(message[i % len(message)], end='')
    print() # Just a new line of bitmap
        