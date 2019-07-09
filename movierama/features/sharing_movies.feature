Feature: Movie Social Sharing

  Background:
    Given there is a set of Movies in the Database
      | title     | description   | date_created       | username |
      | Movie 1   | description 2 | 2019-07-01 10:00   | jaimelan |
      | Movie 2   | description 3 | 2019-07-02 23:00   | theongre |
      | Movie 3   | description 4 | 2019-07-02 23:30   | jonsnow  |

  Scenario: User sees a list of shared Movies in homepage
    Given user is on the Home page
    Then the page includes "Movie 1"
    Then the page includes "Movie 2"


  Scenario Outline: User sees a list of a specific user's Movies in homepage
    Given user is on the Home page
    When he clicks on the name of user "<username>"
    Then the page includes "<movie>"

    Examples: Results
    | username  | movie     |
    | jaimelan  | Movie 1   |
    | theongre  | Movie 2   |


  Scenario Outline: User can sort by "<filter>" a list of Movies
    Given user is on the Home page
    When he press "<filter>"
    Then movie with title "<movie>" should be first

    Examples: Filters
    | filter          | movie    |
    | order_by_date   | Movie 3  |
#    | order_by_likes  | Movie 2 |
#    | order_by_hates  | Movie 2 |


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
    Given existing user
    And user is authenticated
    And existing movie "Movie 3" of user "jonsnow"
    When user is on the Home page
    When he press "btn_add_movie"
    Then user is redirected to "movies:create"
    When fills the form
            | field             | value                       |
            | title             | Movie 3     |
            | description       | Lorem ipsum                 |
    And he press "btn_save"
    Then a new Movie with title "Movie 3" is not added

  Scenario: User likes a Movie
    Given existing user
    And existing movie "Movie 3" of user "jonsnow"
    When user likes Movie
    Then the number of likes of the movie is increased by "1"

  Scenario: User hates a Movie
    Given existing user
    And existing movie "Movie 3" of user "jonsnow"
    When user hates Movie
    Then the number of hates of the movie is increased by "1"

  Scenario: User cannot hate a Movie he already hates
    Given existing user
    And existing movie "Movie 3" of user "jonsnow"
    When user hates Movie
    And user hates Movie
    Then the number of hates of the movie is increased by "0"

  Scenario: User cannot like a Movie he already like
    Given existing user
    And existing movie "Movie 3" of user "jonsnow"
    When user likes Movie
    When user likes Movie
    Then the number of likes of the movie is increased by "0"

  Scenario: User remove his vote from a Movie he likes
    Given existing user
    And existing movie "Movie 3" of user "jonsnow"
    And user likes Movie
    When user removes vote
    Then the number of likes of the movie is descreased by "1"

  Scenario: User cannot like a Movie he has added
    Given existing user
    And existing movie "Movie 1" of user "jaimelan"
    When user likes Movie
    Then a movievote for "jaimelan" and "Movie 1" is not created

  Scenario: User cannot hate a Movie he has added
    Given existing user
    And existing movie "Movie 1" of user "jaimelan"
    When user hates Movie
    Then a movievote for "jaimelan" and "Movie 1" is not created


