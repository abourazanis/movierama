Feature: Movie Social Sharing

  Background:
    Given there is a set of Movies in the Database
      | id | title     | description   | date_published     | likes | hates  | username
      | 1  | Movie 1   | description 2 | 2019-07-01 10:00   | 2     | 5      | jaimelan
      | 2  | Movie 2   | description 3 | 2019-07-02 23:00   | 4     | 1      | theongre

  Scenario: User sees a list of shared Movies in homepage
    Given user is on the homepage
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
    Given authenticated user is in homepage
    When he clicks on "Add Movie" button
    Then he is redirected to the New Movie page
    When he enters all the required data
    And Movie does not exists already
    And clicks on "Save"
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


