import Functions as generalFunctions
import Variables 


Access:bool = False


if (Access == False):
    permission = generalFunctions.Permissions(prompt_text=Variables.Prompt , Choices=Variables.Choices)
    
while not Access:
    if (permission == "Yes"):
         Access = True
         generalFunctions.open_camera()
         
    elif Access== False:
        print("Permission required to run the Application \n Please Allow")
        permission = generalFunctions.Permissions(prompt_text=Variables.Prompt , Choices=Variables.Choices)
    
     
     
    


