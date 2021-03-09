Feature: SwagLabs Web Browsing
  As a web surfer,
  I want to find products online,
  So I can add to cart and buy it.

  Background:
    Given the SwagLabs home page is displayed


  Scenario Outline: Login
    When I type the username "<username>" and password "<password>"
    And I click on login button
    Then Validate the result page with Page Title


    Examples:
      | username      | password     |
      | standard_user | secret_sauce |

  Scenario Outline: Login Error
    When I type the username "<username>" and password "<password>"
    And I click on login button
    Then Validate the error message


    Examples:
      | username        | password     |
      | locked_out_user | secret_sauce |


