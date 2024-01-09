import customtkinter as ctk
import pickle
import json
import numpy as np

'''
If the GUI version of the Spam filter is wanted, initialize_gui should be set to 0.
For API requests, initialize gui should not be set to 0 to prevent the GUI instantiation. 
'''
initialize_gui=0
  
class App(ctk.CTk):
     def __init__(self,*args, **kwargs):
          if initialize_gui == 0:
               super().__init__(*args, **kwargs)

               self.title("App")
               self.geometry("1000x700")

               #Setting GUI general theme
               ctk.set_appearance_mode("dark")
               ctk.set_default_color_theme("dark-blue") 

               #Title Label
               self.titleLabel = ctk.CTkLabel(self, text="Spam Or Not Classification",
                                                  font=('Georgia', 30), fg_color='#a0d2eb',
                                                  text_color='#0049B7')
               self.titleLabel.place(relx=.5, rely=.05, 
                                        anchor="center")

               #Email text entry box
               self.entryTextBox = ctk.CTkTextbox(self,height=400,
                                                  width=650,border_width=3,
                                                  border_color='#ffffff')
               self.entryTextBox.place(relx=.5, rely=.4, 
                                        anchor="center")
               
               #Submit Button
               self.submitButton = ctk.CTkButton(self, text="Enter",
                                                  width=653,
                                                  command=self.evaluateForSpam)
               self.submitButton.place(relx=.5, rely=.71, 
                                        anchor="center")
               
               self.classificationLabel = ctk.CTkLabel(self, text="Classification:",
                                                  font=('Georgia', 40), fg_color='#F9E795',
                                                  text_color='#0049B7')
               self.classificationLabel.place(relx=.3, rely=.85, 
                                        anchor="center")
               
               #Spam or not result
               self.resultLabel = ctk.CTkLabel(self, text="None",
                                                  font=('Georgia', 40), fg_color='#F96167',
                                                  text_color='#0049B7')
               self.resultLabel.place(relx=.6, rely=.85, 
                                        anchor="center")

     #Loading model
     def get_model(self):
          pickle_in = open("stack_model.pickle","rb")
          model = pickle.load(pickle_in)

          return model

     #Loading columns
     def get_columns(self):
          f = open("word_columns.json") 
          columns = json.load(f)
          col_list =  columns["data_columns"]
          
          return col_list

     #Collecting the word data passed and adding it accordingly to an array based on the column it needs to be in
     def prepare_df(self, col_list, words):
          print("RUNNING")
          data = np.zeros(len(col_list))

          preposition_list = ['for', 'to','of','at', 'in',
                              'with','at','by','as','above','about', 
                              'after','around','before','between','down', 
                              'from','in','into','of','off','on',  
                              'out','over','under','up','but','like', 
                              'regarding','since','within']
          
          pronouns_list = ['i','we','you','he','she', 
                           'it','they','me','us','you','her', 
                           'him','it','them','mine','our','your',
                           'her','his','their','my','myself',
                           'yourself','itself','both','each','either',
                           'everyone','everything','few','one','other',
                           'others','some','someone','such','most']
          
          interjection_list = ['hi','ok']

          conjunction_list = ['and','or','nor','because','if','although','than','that','though', 
                              'till','unless','until','when','where','while','or','whether']
          
          for word in words:
               if word in preposition_list:
                    data[-4] += 1
               elif word in pronouns_list:
                    data[-3] += 1
               elif word in interjection_list:
                    data[-2] += 1
               elif word in conjunction_list:
                    data[-1] += 1
               elif word in col_list[:-4]:
                    ind = col_list.index(word)
                    data[ind] += 1
          
          return data
     
     #Gathering and preparing data for spam classification and returning the classification to the GUI
     def evaluateForSpam(self):
          model = self.get_model()
          col_list = self.get_columns()
          inp = self.entryTextBox.get(1.0, "end-1c")
          df = self.prepare_df(col_list, inp.lower().split())

          result = ""
          if model.predict([df])[0] == 1:
               result = "SPAM"
               self.resultLabel.configure(text = result, fg_color='#F96167')
          else:
               result = "Not Spam"
               self.resultLabel.configure(text = result, fg_color ='#3A6B35')

#Displaying GUI
if __name__ == "__main__":
     app = App()
     #Runs the app
     app.mainloop()   

     
