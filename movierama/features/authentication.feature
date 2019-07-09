Feature: User Authentication

    Scenario: User successfully creates an account
        Given a user is on the Registration page
        When fills the form
            | field             | value     |
            | first_name        | Jaime     |
            | last_name         | Lannister |
            | username          | jaimelan  |
            | password1         | 123asd456 |
        And he press "btn_signup"
        Then a MovieRama account is created for "jaimelan"
        Then user is redirected to "homepage"



    Scenario: User logs in
        Given existing user
        When user is on the Login page
        When fills the form
            | field         | value     |
            | login         | jaimelan  |
            | password      | 123asd456 |
        And he press "btn_login"
        Then user is redirected to "homepage"
        Then user is authenticated



    Scenario: User logs out
        Given existing user
        And user is authenticated
        When user is on the Home page
        And he press "btn_logout"
        Then user is logged out
        Then user is redirected to "homepage"


