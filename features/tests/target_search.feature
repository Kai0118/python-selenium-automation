# Created by Kaique at 2/17/2024
Feature: target.com verifying that the “Your cart is empty” message is shown when clicking on the cart icon


  Scenario: User can get the “Your cart is empty” message is shown when clicking on the cart icon
    Given Open Target main page
    When Clicking on the cart icon
    Then "Your cart is empty" message is shown


#Feature: target.com verifying that the “Your cart is empty” message is shown when clicking on the cart icon
#
#
#  Scenario: User can get the “Your cart is empty” message is shown when clicking on the cart icon
#    Given open Target main page
#    When Clicking on the cart icon
#    Then "Your cart is empty" message is shown
