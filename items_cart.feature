Feature: SwagLabs Web Browsing
  As a web surfer,
  I want to find products online,
  So I can add to cart and buy it.

  Background:
    Given the SwagLabs home page is displayed


  Scenario Outline: AddItems
    When I type the username "<username>" and password "<password>"
    And I click on login button
    And The result page is displayed
    Then I click on random items that needs to be added
    And I move to cart page
    And I click on checkout button


    Examples:
      | username      | password     |
      | standard_user | secret_sauce |

  Scenario Outline: RemoveItems
    When I type the username "<username>" and password "<password>"
    And I click on login button
    And The result page is displayed
    Then I click on random items that needs to be added
    And I move to cart page
    And I remove items in the cart page


    Examples:
      | username      | password     |
      | standard_user | secret_sauce |


  Scenario Outline: Add_RemoveItems
    When I type the username "<username>" and password "<password>"
    And I click on login button
    And The result page is displayed
    Then I click on random items that needs to be added and click remove


    Examples:
      | username      | password     |
      | standard_user | secret_sauce |