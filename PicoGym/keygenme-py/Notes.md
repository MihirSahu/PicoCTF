Study the code and find what the functions do
We find that the first part of the flag is visible 'picoCTF{1n_7h3_|<3y_of_' but we need to find the 8 character that come after it
The enter_license() fuction calls the check_key() function, which checks certain hex values of the sha256 checksum of b"FREEMAN"
If we emulate what the program does in a python shell we get:
>bUsername_trial = b"FREEMAN"                                                                      
>key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
>key_part_dynamic1_trial = "xxxxxxxx"
>key_part_static2_trial = "}"
>hashlib.sha256(bUsername_trial).hexdigest()[4]
>'0'
>hashlib.sha256(bUsername_trial).hexdigest()[5]                                                    
>'d'
>hashlib.sha256(bUsername_trial).hexdigest()[3]                                                    
>'2'
>hashlib.sha256(bUsername_trial).hexdigest()[6]                                                    
>'0'
>hashlib.sha256(bUsername_trial).hexdigest()[2]                                                    
>'8'
>hashlib.sha256(bUsername_trial).hexdigest()[7]                                                    
>'3'
>hashlib.sha256(bUsername_trial).hexdigest()[1]                                                    
>'9'
>hashlib.sha256(bUsername_trial).hexdigest()[8]                                                    
>'2'

Now if we simple append these to the original visible flag we get 'picoCTF{1n_7h3_|<3y_of_0d208392}'
