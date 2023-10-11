Feature: Check the functionality of the login page.

#    Tema: - Scenariile de la 2-5.Scenario:
#          - Folositi Backround Given.

  Background:

#Scenariu 1: username corect + parola corecta
Scenario: Successful login
  Given I am on the Saucedemo login page
  When I insert a correct username and password
  And I click the login button
  Then I am logged in and I see the list of products
#Scenariu 2: username gresit + parola corecta
#Scenariu 3: username corect + parola gresita
#Scenariu 4: username corecta + parola None
#Scenariu 5: username None + parola corecta
#Scenariu 6: username incorect + parola None
#Scenariu 7: username None + parola incorecta
#Scenariu 8: username None + parola None
#Scenariu 9: username gresit + parola gresita
#Scenariu 10: username blocat (locked_out_user) + parola corecta