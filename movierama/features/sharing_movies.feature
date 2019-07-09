Feature: Movie Social Sharing

  Background:
    Given there is a set of Movies in the Database
      | title     | description   | date_created       |
      | Movie 1   | description 2 | 2019-07-01 10:00   |
      | Movie 2   | description 3 | 2019-07-02 23:00   |

  Scenario: User sees a list of shared Movies in homepage
    Given user is on the Home page
    Then the page includes "Movie 1"
    Then the page includes "Movie 2"


  Scenario Outline: User sees a list of a specific user's Movies in homepage
    Given user is on the homepage
    When he clicks on the name of user "<username>"
    Then the page includes only "<movie>"

    Examples: Results
    | username  | movie
    | jaimelan  | Movie 1
    | theongre  | Movie 2


  Scenario Outline: User can sort by "<filter>" a list of Movies
    Given user is on homepage
    When user click in sort by "<filter>" button
    Then the list of shared Movies are sorted by "<filter>"

    Examples: Filters
    | filter
    | date
    | likes
    | hates


  Scenario: User adds a new Movie
    Given existing user
    And user is authenticated
    When user is on the Home page
    When he press "btn_add_movie"
    Then user is redirected to "movies:create"
    When fills the form
            | field             | value                       |
            | title             | The Empire Strikes Back     |
            | description       | Lorem ipsum                 |
    And he press "btn_save"
    Then a new Movie is added


  Scenario: User cannot add an existing Movie
    Given authenticated user is in homepage
    When he clicks on "Add Movie" button
    Then he is redirected to the New Movie page
    When he enters all the required data
    And Movie exists already
    Then a message is shown

  Scenario: User likes a Movie
    Given authenticated user is in homepage
    When user press like on a movie
    Then the number of likes of the movie is increased by 1

  Scenario: User hates a Movie
    Given authenticated user is in homepage
    When user press hate on a movie
    Then the number of hates of the movie increase by 1


  Scenario: User cannot hate a Movie he already likes
    Given authenticated user is in homepage
    When user press hate on a movie he already hates
    Then a message is shown

  Scenario: User cannot like a Movie he already like
    Given authenticated user is in homepage
    When user press like on a movie he already likes
    Then a message is shown

  Scenario: User cannot like a Movie he has added
    Given authenticated user is in homepage
    When user press like on a movie he has added
    Then a message is shown

  Scenario: User cannot hate a Movie he has added
    Given authenticated user is in homepage
    When user press hate on a movie he has added
    Then a message is shown


