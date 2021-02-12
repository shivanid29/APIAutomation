Feature: Verify if books are added or deleted using Library API
  @smoke
  Scenario: Verify Add Book API functionality
    Given the book details needs to be added to the Library
    When we execute the ADD book Post API Method
    Then The book should be added to the Library
    And the statuscode of the response should be 200




  @regression
  Scenario Outline: Verify Add Book API functionality
    Given the book details needs to be added to the Library using <isbn> and <aisle>
    When we execute the ADD book Post API Method
    Then The book should be added to the Library
    Examples:
      |isbn  |aisle |
      | fferf | 768 |
      | shiva | 262 |
