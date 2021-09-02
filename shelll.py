Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range (6):
	for j in range (0,i):
		print(j+1, end='')
	print('\n')

	


1

12

123

1234

12345

>>> for i in range(6):
	for j in range(i):
		print(i,end='')
	print('\n')

	


1

22

333

4444

55555

>>> for i in range(6):
	for j in range (6):
		if(j<=5-1):
			print(' ',end='')
		else:
			print('*',end='')
	print('\n')

	
     *

     *

     *

     *

     *

     *

>>> for i in range(6):
	for j in range (6):
		if(j<=5-i):
			print(' ',end='')
		else:
			print('*',end='')
	print('\n')

	
      

     *

    **

   ***

  ****

 *****

>>> 