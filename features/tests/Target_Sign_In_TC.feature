# Created by Kaique at 2/26/2024
Feature: target.com verify that when logged out user can access sign in


  Scenario: When logged out, user can access Sign in
    Given Open Target main page
    When Click Sign in
    And From right side navigation menu, click Sign In
    Then Verify Sign In form opened