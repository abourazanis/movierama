Feature: User Authentication

    Scenario: User successfully creates an account
        Given a user is on the Registration page
        When fills the form
            | field      | value     |
            | name       | Jaime     |
            | lastname   | Lannister |
            | username   | jaimelan  |
            | password   | 123asd456 |
        And he press "sign in"
        Then a MovieRama account is created for "username"
        Then user is redirected to "homepage"



    Scenario: User logs in
        Given existing user
        When user is on the Login page
        When fills the form
            | field      | value     |
            | username   | jaimelan  |
            | password   | 123asd456 |
        And he press "log in"
        Then user is redirected to "homepage"
        Then user is authenticated



    Scenario: User logs out
        Given existing user
        And user is authenticated
        When user is on the Home page
        And he press "log out"
        Then user is logged out
        Then user is redirected to "homepage"


